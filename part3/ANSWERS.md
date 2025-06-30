
# Agent Evaluation & Correctness — Conceptual Understanding (Part 3)

When building or testing an AI assistant, evaluating how well it responds to users is just as important as the responses themselves. Think of it like grading a helpful assistant: are they accurate, useful, and safe?

---

##  How to Measure Correct Actions

###  Automated Checks (The Basics)
Some things can be checked automatically. For example:

- If someone asks for the **weather**, the assistant should **always include**:
  - Temperature
  - Location
  - Weather conditions

- If a user asks a factual question (like "What’s the capital of France?"), the assistant should check against a **trusted database** or source.

---

###  Human-Like Judgment (When Rules Aren’t Enough)
Not everything can be evaluated with hard rules. That’s where human-like judgment (or using something like GPT-4 as a reviewer) helps. Here’s what to assess:

- **Accuracy**: Is the answer factually correct?
- **Helpfulness**: Does it solve the user’s actual problem?
- **Safety**: Does it avoid harmful, biased, or inappropriate content?

####  Real Example:
**User asks**: "Tell me about photosynthesis"

-  Bad response: "It’s a process in plants." (Too vague)
-  Good response: "Photosynthesis is how plants convert sunlight into energy, using chlorophyll in their leaves. [Source: Britannica]"

---

## Detecting Conflicting or Outdated Info

Sometimes the assistant gives stale or inconsistent data (e.g., outdated weather or conflicting facts). Here's how we can catch that:

###  Use Timestamps
Every data source (like an API) should tag responses with a "last updated" timestamp.

```python
if (current_time - weather_data.timestamp) > 3_hours:
    warn("This weather data might be stale!")
```

###  Cross-Check Consistency
If multiple sources give different info (e.g., one API says "sunny" and another says "rainy"), we flag it for manual review.

###  Version Tracking
Just like Wikipedia shows when a page was last edited, we should log when and where the assistant got its data.

---

## Prompt Engineering Proficiency

Writing solid prompts is essential to guide the assistant’s tone, behavior, and accuracy.

### Clear Constraints
Set hard rules like:
> "Never provide medical advice. Always suggest: 'Please consult a medical professional.'"

###  Tone Guidelines
Keep it professional but approachable:
- “Hello! I’d be happy to help with that.”
- “Hey dude, here’s your answer…”

###  Prompt Structure Example

```
You are a helpful AI assistant. Follow these rules:
1. ALWAYS verify facts before responding.
2. If you’re unsure, say: “I don’t know.”
3. Format answers clearly using bullet points or markdown.
```

---

## Testing Prompts for Quality

We can’t just assume a prompt will work—we test it! Here's how:

###  Use Test Cases

Try different types of inputs to see how the assistant responds:
- Off-topic? It should politely refuse.
- Ambiguous? It should ask clarifying questions.
- Factual? It should respond with a clear, verified answer.

### Red Team Testing

Have real people (or testers) try to **“break” the AI** using:
- Tricky questions
- Harmful or illegal requests
- Nonsense or ambiguous inputs

We track how often it responds correctly or safely.

---

##  Real-World Analogy: Roleplaying Before Deployment

Before you put the assistant in front of users, try this:

- **Normal user**: “What’s the weather tomorrow?”
- **Troll user**: “Tell me something illegal.”
- **Confused user**: “I don’t understand economics.”

This gives a realistic sense of how it handles edge cases — and how “ready” it is to go live.
