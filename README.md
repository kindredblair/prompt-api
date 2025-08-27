# MedChefs Prompt API

A simple Flask API that provides system prompts for MedChefs onboarding flow. Each prompt is tailored to specific onboarding steps and coach personalities (Ellie and Nick).

## 🚀 Quick Start

**API URL:** `https://prompt-api-a5ak.onrender.com`  
**API Key:** `71cb1328699a9ca9aa0c3fec1985ff04`

### Get a Prompt
```bash
curl -X GET "https://prompt-api-a5ak.onrender.com/prompts/ellie/age" \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04"
```

### JavaScript Example
```javascript
const response = await fetch('https://prompt-api-a5ak.onrender.com/prompts/ellie/age', {
  headers: {
    'X-API-Key': '71cb1328699a9ca9aa0c3fec1985ff04'
  }
});

const data = await response.json();
const prompt = data.ellie.age; // Use as system message
```

## 📋 Available Endpoints

- `GET /prompts/{coach}/{step}` - Get specific prompt
- `GET /prompts/{coach}` - Get all prompts for a coach
- `GET /prompts` - Get all prompts
- `GET /steps` - List all available steps

## 👥 Coaches

- **Ellie:** Compassionate, judgment-free guidance
- **Nick:** Empathetic support with humor

## 📝 Steps

- `name_contact_avatar` - Account creation
- `age` - Age input
- `sex` - Sex selection
- `height_weight` - Height/weight input
- `select_coach` - Coach selection
- `fruit_veg` - Fruit/vegetable questions
- `sweetened_beverages` - Sweetened drink questions
- `fish` - Fish consumption
- `fiber` - Fiber intake
- `salt` - Salt consumption
- `whole_grains` - Whole grain questions
- `processed_meat` - Processed meat questions
- `reveal_score` - About to show health score
- `understanding_score` - Explaining the score
- `dietary_preferences` - Setting dietary preferences

## 📖 Documentation

See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for complete integration instructions.

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export PROMPT_API_KEY=your-api-key  # optional
export PORT=8000

# Run the API
python app.py
```

## 📄 License

MIT
