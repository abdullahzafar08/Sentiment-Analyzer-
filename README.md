I get it, that's incredibly annoying. The "break" happens because most LLMs are programmed to explain things step-by-step, so they close the code block, write a sentence of "helpful" text, and then start a new block. This completely ruins a single-file copy-paste.

Since you want **zero** interference and a single file for your BSCS project, here is the **one and only** block you need. I have removed all the conversational filler between the sections so it stays as one continuous Markdown document.

```markdown
# 🚀 Gemini 3 Sentiment Engine

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://python.org)
[![Model](https://img.shields.io/badge/Model-Gemini_3_Flash-orange.svg)](https://ai.google.dev)
[![Manager](https://img.shields.io/badge/Package_Manager-uv-purple.svg)](https://github.com/astral-sh/uv)

A high-performance sentiment analysis agent that transforms messy user rants into clean, structured JSON. Built for speed, reliability, and the edge of AI technology using Google's latest Gemini 3 architecture.

---

## 🧠 How it Works

1. **User Input**: Captures raw text (quotes, rants, or feedback).
2. **AI Inference**: Processes the text via the **Gemini 3 Flash** model.
3. **Structured Output**: Uses a strict JSON schema to force the AI to return validated data.
4. **Local Archive**: Saves a timestamped `.json` file for every analysis.

---

## 🛠 Tech Stack

- **AI Core**: Google Gemini 3 Flash (Direct SDK)
- **Environment**: Managed via `uv` (Faster than pip/poetry)
- **Security**: Zero-leak `.env` architecture for API safety
- **Data**: JSON-based persistent storage

---

## 📦 Getting Started

### 1. Installation
Clone the repo and sync dependencies using `uv`:
```bash
git clone [https://github.com/abdullahzafar08/sentiment-analyzer-ai.git](https://github.com/abdullahzafar08/sentiment-analyzer-ai.git)
cd sentiment-analyzer-ai
uv sync

```

### 2. Configuration

Create a `.env` file in the root directory and add your key:

```text
GEMINI_API_KEY=your_actual_api_key_here

```

### 3. Usage

Run the engine using `uv`:

```bash
uv run python main.py

```

### Example Output

```json
{
  "sentiment": "Negative",
  "score": 7,
  "summary": "The user is confused and frustrated by the temperament of their professors.",
  "reasoning": "Terms like 'mad all the time' and 'idk why' show perceived hostility and a lack of understanding."
}

```

```

