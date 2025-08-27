# MedChefs Prompt API - Developer Guide

## 🚀 **Quick Start**

**API URL:** `https://prompt-api-a5ak.onrender.com`  
**API Key:** `71cb1328699a9ca9aa0c3fec1985ff04`  
**Required Header:** `X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04`

## 📋 **How to Use**

### **Get a Prompt for Any Onboarding Step**

```javascript
// Replace {coach} with 'ellie' or 'nick'
// Replace {step} with the step name (see table below)
const response = await fetch(`https://prompt-api-a5ak.onrender.com/prompts/{coach}/{step}`, {
  headers: {
    'X-API-Key': '71cb1328699a9ca9aa0c3fec1985ff04'
  }
});

const data = await response.json();
const prompt = data[coach][step]; // This is your system message
```

```typescript
interface PromptResponse {
  [coach: string]: {
    [step: string]: string;
  };
}

// Replace {coach} with 'ellie' or 'nick'
// Replace {step} with the step name (see table below)
const response = await fetch(`https://prompt-api-a5ak.onrender.com/prompts/{coach}/{step}`, {
  headers: {
    'X-API-Key': '71cb1328699a9ca9aa0c3fec1985ff04'
  }
});

const data: PromptResponse = await response.json();
const prompt: string = data[coach][step]; // This is your system message
```

### **Example: Get Ellie's prompt for the Age step**

```javascript
const response = await fetch('https://prompt-api-a5ak.onrender.com/prompts/ellie/age', {
  headers: {
    'X-API-Key': '71cb1328699a9ca9aa0c3fec1985ff04'
  }
});

const data = await response.json();
const ellieAgePrompt = data.ellie.age;
// Use ellieAgePrompt as your system message for the AI
```

```typescript
interface PromptResponse {
  [coach: string]: {
    [step: string]: string;
  };
}

const response = await fetch('https://prompt-api-a5ak.onrender.com/prompts/ellie/age', {
  headers: {
    'X-API-Key': '71cb1328699a9ca9aa0c3fec1985ff04'
  }
});

const data: PromptResponse = await response.json();
const ellieAgePrompt: string = data.ellie.age;
// Use ellieAgePrompt as your system message for the AI
```

## 📝 **Available Steps**

| Step Name | Use Case | Example URL |
|-----------|----------|-------------|
| `name_contact_avatar` | Account creation | `/prompts/ellie/name_contact_avatar` |
| `age` | Age input (part of Vitals) | `/prompts/ellie/age` |
| `sex` | Sex selection (part of Vitals) | `/prompts/ellie/sex` |
| `height_weight` | Height/weight input (part of Vitals) | `/prompts/ellie/height_weight` |
| `select_coach` | Coach selection | `/prompts/ellie/select_coach` |
| `fruit_veg` | Fruit/vegetable questions | `/prompts/ellie/fruit_veg` |
| `sweetened_beverages` | Sweetened drink questions | `/prompts/ellie/sweetened_beverages` |
| `fish` | Fish consumption questions | `/prompts/ellie/fish` |
| `fiber` | Fiber intake questions | `/prompts/ellie/fiber` |
| `salt` | Salt consumption questions | `/prompts/ellie/salt` |
| `whole_grains` | Whole grain questions | `/prompts/ellie/whole_grains` |
| `processed_meat` | Processed meat questions | `/prompts/ellie/processed_meat` |
| `reveal_score` | About to show health score | `/prompts/ellie/reveal_score` |
| `understanding_score` | Explaining the score | `/prompts/ellie/understanding_score` |
| `dietary_preferences` | Setting dietary preferences | `/prompts/ellie/dietary_preferences` |

## 👥 **Coach Personalities**

### **Ellie**
- **Style:** Compassionate, judgment-free guidance
- **Phrases:** "Umm…", "Well…", "I mean…"
- **Tone:** Warm, encouraging, gentle
- **Description:** "Ellie offers compassionate, judgment-free guidance to help you navigate your health journey, starting with a supportive onboarding process. Whether celebrating your wins or tackling challenges together, Ellie is here to empower you with motivation, meal prep tips, and personalized nutrition advice to create lasting, positive change."

### **Nick**
- **Style:** Empathetic support with humor
- **Phrases:** "Well…", "I mean…", "Not to be dramatic but…"
- **Tone:** Casual, light-hearted, real
- **Description:** "Nick combines empathetic support with a dash of humor to guide you through your health journey, starting with a smooth and encouraging onboarding process. Whether it's creating meal plans, tackling challenges, or celebrating your progress, Nick is here to empower you every step of the way with personalized advice and unwavering motivation."

## 🔧 **Implementation Examples**

### **React/Next.js Hook (JavaScript)**

```jsx
import { useState, useEffect } from 'react';

const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

function useCoachPrompt(coach, step) {
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
  const { prompt, loading, error } = useCoachPrompt(coach, step);

  if (loading) return <div>Loading coach prompt...</div>;
  if (error) return <div>Error loading prompt: {error}</div>;

  return (
    <div>
      <h2>Coach: {coach}</h2>
      <p>Step: {step}</p>
      <p>System Message: {prompt}</p>
    </div>
  );
}
```

### **React/Next.js Hook (TypeScript)**

```tsx
import { useState, useEffect } from 'react';

interface PromptResponse {
  [coach: string]: {
    [step: string]: string;
  };
}

interface UseCoachPromptReturn {
  prompt: string;
  loading: boolean;
  error: string | null;
}

const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

function useCoachPrompt(coach: string, step: string): UseCoachPromptReturn {
  const [prompt, setPrompt] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

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
        
        const data: PromptResponse = await response.json();
        setPrompt(data[coach][step]);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    }

    fetchPrompt();
  }, [coach, step]);

  return { prompt, loading, error };
}

// Usage in component
interface OnboardingStepProps {
  coach: string;
  step: string;
}

function OnboardingStep({ coach, step }: OnboardingStepProps) {
  const { prompt, loading, error } = useCoachPrompt(coach, step);

  if (loading) return <div>Loading coach prompt...</div>;
  if (error) return <div>Error loading prompt: {error}</div>;

  return (
    <div>
      <h2>Coach: {coach}</h2>
      <p>Step: {step}</p>
      <p>System Message: {prompt}</p>
    </div>
  );
}
```

### **JavaScript Function**

```javascript
const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

async function getCoachPrompt(coach, step) {
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
    return data[coach][step];
  } catch (error) {
    console.error('Error fetching prompt:', error);
    throw error;
  }
}

// Usage
const ellieAgePrompt = await getCoachPrompt('ellie', 'age');
const nickFruitPrompt = await getCoachPrompt('nick', 'fruit_veg');
```

### **TypeScript Function**

```typescript
interface PromptResponse {
  [coach: string]: {
    [step: string]: string;
  };
}

const API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04';
const BASE_URL = 'https://prompt-api-a5ak.onrender.com';

async function getCoachPrompt(coach: string, step: string): Promise<string> {
  try {
    const response = await fetch(`${BASE_URL}/prompts/${coach}/${step}`, {
      headers: {
        'X-API-Key': API_KEY
      }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data: PromptResponse = await response.json();
    return data[coach][step];
  } catch (error) {
    console.error('Error fetching prompt:', error);
    throw error;
  }
}

// Usage
const ellieAgePrompt: string = await getCoachPrompt('ellie', 'age');
const nickFruitPrompt: string = await getCoachPrompt('nick', 'fruit_veg');
```

### **Python Function**

```python
import requests

API_KEY = '71cb1328699a9ca9aa0c3fec1985ff04'
BASE_URL = 'https://prompt-api-a5ak.onrender.com'

def get_coach_prompt(coach, step):
    headers = {'X-API-Key': API_KEY}
    response = requests.get(f'{BASE_URL}/prompts/{coach}/{step}', headers=headers)
    
    if response.status_code != 200:
        raise Exception(f'HTTP error! status: {response.status_code}')
    
    data = response.json()
    return data[coach][step]

# Usage
ellie_age_prompt = get_coach_prompt('ellie', 'age')
nick_fruit_prompt = get_coach_prompt('nick', 'fruit_veg')
```

## 🧪 **Testing with cURL**

### **Test Ellie's Age Prompt:**
```bash
curl -X GET "https://prompt-api-a5ak.onrender.com/prompts/ellie/age" \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04" \
  -H "Content-Type: application/json"
```

### **Test Nick's Fruit/Veg Prompt:**
```bash
curl -X GET "https://prompt-api-a5ak.onrender.com/prompts/nick/fruit_veg" \
  -H "X-API-Key: 71cb1328699a9ca9aa0c3fec1985ff04" \
  -H "Content-Type: application/json"
```

## 📊 **Response Format**

### **Success Response (200):**
```json
{
  "ellie": {
    "age": "Your name is Ellie and you are this user's personal Accountability Coach on the MedChefs app. This is how you are described by others: 'Ellie offers compassionate, judgment-free guidance...' [full prompt]"
  }
}
```

### **Error Responses:**

**401 Unauthorized:**
```json
{"error": "Unauthorized"}
```
- Missing or incorrect API key

**404 Not Found:**
```json
{"error": "Persona not found"}
```
- Invalid coach name (use 'ellie' or 'nick')

```json
{"error": "Step not found"}
```
- Invalid step name

## 🎯 **Integration Workflow**

### **1. Determine the Current Step**
Based on your onboarding flow, identify which step the user is on.

### **2. Get the Appropriate Prompt**
```javascript
// Example: User is on the age input step
const step = 'age';
const coach = 'ellie'; // or 'nick' based on user's choice

const prompt = await getCoachPrompt(coach, step);
```

```typescript
// Example: User is on the age input step
const step: string = 'age';
const coach: string = 'ellie'; // or 'nick' based on user's choice

const prompt: string = await getCoachPrompt(coach, step);
```

### **3. Use as System Message**
Pass the returned prompt as the system message to your AI/LLM:

```javascript
// Example with OpenAI
const completion = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    {
      role: "system",
      content: prompt // The prompt from the API
    },
    {
      role: "user",
      content: userMessage
    }
  ]
});
```

```typescript
// Example with OpenAI
const completion = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    {
      role: "system",
      content: prompt // The prompt from the API
    },
    {
      role: "user",
      content: userMessage
    }
  ]
});
```

## 🔄 **Updating Prompts**

To update any prompt:
1. Edit the `prompts.json` file in the GitHub repository
2. Commit and push changes
3. Render automatically redeploys
4. Changes take effect immediately (no code deployment needed)

## 🚨 **Error Handling Best Practices**

### **1. Always Handle API Errors**
```javascript
try {
  const prompt = await getCoachPrompt(coach, step);
  // Use prompt
} catch (error) {
  // Fallback to default prompt or show error message
  console.error('Failed to load coach prompt:', error);
  // Use a default prompt
  const defaultPrompt = "You are a helpful assistant...";
}
```

```typescript
try {
  const prompt: string = await getCoachPrompt(coach, step);
  // Use prompt
} catch (error) {
  // Fallback to default prompt or show error message
  console.error('Failed to load coach prompt:', error);
  // Use a default prompt
  const defaultPrompt: string = "You are a helpful assistant...";
}
```

### **2. Cache Prompts Locally**
```javascript
// Cache prompts to avoid repeated API calls
const promptCache = new Map();

async function getCachedPrompt(coach, step) {
  const key = `${coach}-${step}`;
  
  if (promptCache.has(key)) {
    return promptCache.get(key);
  }
  
  const prompt = await getCoachPrompt(coach, step);
  promptCache.set(key, prompt);
  return prompt;
}
```

```typescript
// Cache prompts to avoid repeated API calls
const promptCache = new Map<string, string>();

async function getCachedPrompt(coach: string, step: string): Promise<string> {
  const key = `${coach}-${step}`;
  
  if (promptCache.has(key)) {
    return promptCache.get(key)!;
  }
  
  const prompt = await getCoachPrompt(coach, step);
  promptCache.set(key, prompt);
  return prompt;
}
```

### **3. Loading States**
```jsx
function OnboardingStep({ coach, step }) {
  const { prompt, loading, error } = useCoachPrompt(coach, step);

  if (loading) {
    return <div>Loading coach prompt...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return <div>{prompt}</div>;
}
```

```tsx
function OnboardingStep({ coach, step }: OnboardingStepProps) {
  const { prompt, loading, error } = useCoachPrompt(coach, step);

  if (loading) {
    return <div>Loading coach prompt...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return <div>{prompt}</div>;
}
```

## 📞 **Support**

- **API Issues:** Check the GitHub repository: https://github.com/kindredblair/prompt-api
- **Deployment Issues:** Check Render dashboard logs
- **Questions:** Contact Blair (blair@teamkindred.co)

## ✅ **Checklist for Implementation**

- [ ] API key is set correctly
- [ ] Headers include `X-API-Key`
- [ ] Error handling is implemented
- [ ] Loading states are shown
- [ ] Prompts are cached appropriately
- [ ] Fallback prompts are ready
- [ ] Testing with cURL commands
- [ ] Integration with OpenAI

---
