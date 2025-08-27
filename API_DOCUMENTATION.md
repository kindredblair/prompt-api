# Prompt API Documentation for MedChefs

## Overview

The Prompt API provides system messages for Ellie and Nick, the accountability coaches in the MedChefs app. Each coach has unique prompts for different steps of the onboarding process.

**Base URL:** `https://prompt-api-a5ak.onrender.com`  
**API Key:** `71cb1328699a9ca9aa0c3fec1985ff04`  
**Required Header:** `X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04`

## API Endpoints

### 1. Get All Steps for a Coach
**GET** `/prompts/{coach}`

Returns all available prompts for a specific coach (Ellie or Nick).

**Example:**
```bash
curl https://prompt-api-a5ak.onrender.com/prompts/ellie \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04"
```

**Response:**
```json
{
  "ellie": {
    "name_contact_avatar": "You are Ellie, the user's personal Accountability Coach...",
    "age": "You are Ellie, the user's personal Accountability Coach...",
    "sex": "You are Ellie, the user's personal Accountability Coach...",
    // ... all other steps
  }
}
```

### 2. Get Specific Step Prompt
**GET** `/prompts/{coach}/{step}`

Returns the system prompt for a specific coach and onboarding step.

**Example:**
```bash
curl https://prompt-api-a5ak.onrender.com/prompts/ellie/age \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04"
```

**Response:**
```json
{
  "ellie": {
    "age": "You are Ellie, the user's personal Accountability Coach in the MedChefs app. The user is entering their age. Speak casually and compassionately, using phrases like 'Umm…' or 'Honestly…'. Keep responses short and simple (one or two sentences) and focus on being supportive. Age is just a number for health - what matters is taking care of yourself at any stage of life."
  }
}
```

### 3. List All Available Steps
**GET** `/steps`

Returns a list of all available onboarding steps.

**Example:**
```bash
curl https://prompt-api-a5ak.onrender.com/steps \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04"
```

**Response:**
```json
{
  "steps": [
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
}
```

### 4. List All Coaches and Their Prompts
**GET** `/prompts`

Returns all prompts for all coaches.

**Example:**
```bash
curl https://prompt-api-a5ak.onrender.com/prompts \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04"
```

## Onboarding Steps

The following steps are available for both Ellie and Nick:

| Step | Description |
|------|-------------|
| `name_contact_avatar` | User enters basic information (name, contact, avatar) |
| `age` | User enters their age |
| `sex` | User selects their biological sex |
| `height_weight` | User enters height and weight |
| `select_coach` | User chooses between Ellie and Nick |
| `fruit_veg` | Questions about fruit and vegetable intake |
| `sweetened_beverages` | Questions about sweetened beverage consumption |
| `fish` | Questions about fish consumption |
| `fiber` | Questions about fiber intake |
| `salt` | Questions about salt consumption |
| `whole_grains` | Questions about whole grain consumption |
| `processed_meat` | Questions about processed meat consumption |
| `reveal_score` | User is about to see their health score |
| `understanding_score` | User is learning about what their score means |
| `dietary_preferences` | User sets dietary preferences and restrictions |

## Coach Personalities

### Ellie
- **Style:** Compassionate and supportive
- **Phrases:** "Umm…", "Honestly…"
- **Tone:** Warm, encouraging, gentle
- **Focus:** Emotional support and gentle guidance

### Nick
- **Style:** Humorous and empathetic
- **Phrases:** "Well…", "I mean…", "Not to be dramatic but…"
- **Tone:** Casual, light-hearted, real
- **Focus:** Practical advice with humor

## Implementation Examples

### JavaScript/TypeScript
```javascript
const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

// Get prompt for specific step
async function getPrompt(coach, step) {
  const response = await fetch(`${BASE_URL}/prompts/${coach}/${step}`, {
    headers: {
      'X-API-Key': API_KEY
    }
  });
  
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  
  const data = await response.json();
  return data[coach][step];
}

// Usage
const ellieAgePrompt = await getPrompt('ellie', 'age');
const nickFruitPrompt = await getPrompt('nick', 'fruit_veg');
```

### Python
```python
import requests

API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04'
BASE_URL = 'https://prompt-api-a5ak.onrender.com'

def get_prompt(coach, step):
    headers = {'X-API-Key': API_KEY}
    response = requests.get(f'{BASE_URL}/prompts/{coach}/{step}', headers=headers)
    
    if response.status_code != 200:
        raise Exception(f'HTTP error! status: {response.status_code}')
    
    data = response.json()
    return data[coach][step]

# Usage
ellie_age_prompt = get_prompt('ellie', 'age')
nick_fruit_prompt = get_prompt('nick', 'fruit_veg')
```

### React/Next.js
```jsx
import { useState, useEffect } from 'react';

const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

function usePrompt(coach, step) {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchPrompt() {
      try {
        const response = await fetch(`${BASE_URL}/prompts/${coach}/${step}`, {
          headers: {
            'X-API-Key': API_KEY
          }
        });
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        setPrompt(data[coach][step]);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchPrompt();
  }, [coach, step]);

  return { prompt, loading, error };
}

// Usage in component
function OnboardingStep({ coach, step }) {
  const { prompt, loading, error } = usePrompt(coach, step);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Coach Prompt</h2>
      <p>{prompt}</p>
    </div>
  );
}
```

## Error Handling

### Common Error Responses

**401 Unauthorized**
```json
{"error": "Unauthorized"}
```
- Missing or incorrect API key

**404 Not Found**
```json
{"error": "Persona not found"}
```
- Invalid coach name (use 'ellie' or 'nick')

```json
{"error": "Step not found"}
```
- Invalid step name

## Best Practices

1. **Cache Prompts:** Store prompts locally to avoid repeated API calls
2. **Error Handling:** Always handle API errors gracefully
3. **Loading States:** Show loading indicators while fetching prompts
4. **Fallback Prompts:** Have default prompts ready in case the API is unavailable
5. **Rate Limiting:** Be mindful of API call frequency

## Updating Prompts

To update prompts:
1. Edit the `prompts.json` file in the GitHub repository
2. Commit and push changes
3. Render will automatically redeploy with updated prompts
4. Changes take effect immediately (no code deployment needed)

## Support

For API issues or questions:
- Check the GitHub repository: https://github.com/kindredblair/prompt-api
- Review the deployment logs in Render dashboard
- Contact the API maintainer
