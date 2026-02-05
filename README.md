# 🚀 Gemini 3 Sentiment Engine

A high-performance sentiment analysis tool that transforms unstructured text into structured, validated JSON data. Built with the cutting-edge Gemini 3 Flash model and managed with the `uv` package manager for maximum speed.

## 🛠 Tech Stack
- **Model**: Gemini 3 Flash (via Google Generative AI SDK)
- **Environment**: Python 3.12+ (Optimized for `uv`)
- **Validation**: Strict JSON schema output

## 📦 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/abdullahzafar08/sentiment-analyzer-ai.git](https://github.com/abdullahzafar08/sentiment-analyzer-ai.git)
   cd sentiment-analyzer-ai

   uv sync

   GEMINI_API_KEY=your_actual_api_key_here

   python main.py

   {
  "sentiment": "Negative",
  "score": 8,
  "summary": "The user is expressing frustration with a technical process.",
  "reasoning": "Keywords like 'pissed' and 'won't run' indicate a high level of dissatisfaction."
}

4.  **Paste it** into your `README.md` and **Save** (`Ctrl + S`).

---

### Step 2: Push the Update
Now, go to your terminal (the "outside the box" commands) and run these to send the shiny new README to GitHub:

```powershell
git add README.md
git commit -m "docs: upgrade README with professional structure"
git push origin main
