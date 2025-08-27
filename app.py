from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Path to your prompts file; default is 'prompts.json' in the project directory.
PROMPTS_FILE = os.environ.get('PROMPTS_FILE', 'prompts.json')
# Optional API key to restrict access
API_KEY = os.environ.get('PROMPT_API_KEY', '')

def load_prompts():
    """Read the JSON file and return a dict of prompts."""
    try:
        with open(PROMPTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/prompts/<persona>', methods=['GET'])
def get_persona_prompt(persona: str):
    """
    Return all prompts for a given persona (coach).
    Requires a matching 'X-API-Key' header if PROMPT_API_KEY is set.
    """
    # Check API key if provided
    if API_KEY:
        token = request.headers.get('X-API-Key', '')
        if token != API_KEY:
            return jsonify({'error': 'Unauthorized'}), 401

    prompts = load_prompts()
    persona_prompts = prompts.get(persona.lower())
    if not persona_prompts:
        return jsonify({'error': 'Persona not found'}), 404

    return jsonify({persona: persona_prompts})

@app.route('/prompts/<persona>/<step>', methods=['GET'])
def get_persona_step_prompt(persona: str, step: str):
    """
    Return the system prompt for a specific persona and step.
    Requires a matching 'X-API-Key' header if PROMPT_API_KEY is set.
    """
    # Check API key if provided
    if API_KEY:
        token = request.headers.get('X-API-Key', '')
        if token != API_KEY:
            return jsonify({'error': 'Unauthorized'}), 401

    prompts = load_prompts()
    persona_prompts = prompts.get(persona.lower())
    if not persona_prompts:
        return jsonify({'error': 'Persona not found'}), 404

    step_prompt = persona_prompts.get(step.lower())
    if not step_prompt:
        return jsonify({'error': 'Step not found'}), 404

    return jsonify({persona: {step: step_prompt}})

@app.route('/prompts', methods=['GET'])
def list_prompts():
    """
    List all personas and their available steps.
    """
    if API_KEY:
        token = request.headers.get('X-API-Key', '')
        if token != API_KEY:
            return jsonify({'error': 'Unauthorized'}), 401

    prompts = load_prompts()
    return jsonify(prompts)

@app.route('/steps', methods=['GET'])
def list_steps():
    """
    List all available steps for onboarding.
    """
    if API_KEY:
        token = request.headers.get('X-API-Key', '')
        if token != API_KEY:
            return jsonify({'error': 'Unauthorized'}), 401

    steps = [
        "name_contact_avatar",
        "age", 
        "sex",
        "height_weight",
        "select_coach",
        "fruit_veg",
        "sweetened_beverages",
        "fish",
        "fiber",
        "salt",
        "whole_grains",
        "processed_meat",
        "reveal_score",
        "understanding_score",
        "dietary_preferences"
    ]
    
    return jsonify({"steps": steps})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
