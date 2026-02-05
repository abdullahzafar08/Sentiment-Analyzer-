
```markdown
# ⚡ Gemini 3 Sentiment Engine

> *"The degree and kind of a person's sexuality reach up into the ultimate pinnacle of their spirit."*  
> — Friedrich Nietzsche

A sentiment analysis engine that doesn't patronize you with explanations. It listens, it thinks, it outputs structured truth—because chaos deserves interpretation, not commentary.

---

## 🎭 Philosophy

Traditional sentiment tools treat text like a problem to solve. This engine treats it like a confession to understand.

**Input**: Raw human expression—messy, contradictory, real.  
**Process**: Gemini 3 Flash tears through the noise.  
**Output**: Clean JSON. No bullshit. Just signal.

---

## ⚙️ Architecture

```
User Rant → Gemini 3 Flash → Structured Schema → Timestamped Archive
```

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Inference** | Google Gemini 3 Flash | State-of-the-art language understanding |
| **Environment** | `uv` Package Manager | Dependency hell, abolished |
| **Security** | `.env` Zero-Leak Design | API keys stay buried |
| **Persistence** | JSON Timestamped Storage | Every analysis, catalogued |

---

## 🚀 Quickstart

### Prerequisites
- Python 3.14+
- A Gemini API key ([get one here](https://ai.google.dev))
- `uv` installed ([installation guide](https://github.com/astral-sh/uv))

### Installation

```bash
# Clone the existential dread
git clone https://github.com/abdullahzafar08/sentiment-analyzer-ai.git
cd sentiment-analyzer-ai

# Sync dependencies (the civilized way)
uv sync
```

### Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

> **Note**: This key is your private cipher. Guard it like Kafka guarded his manuscripts.

### Execution

```bash
uv run python main.py
```

---

## 📊 Sample Output

**Input**:  
*"idk why my professors are mad all the time like chill bro"*

**Output**:
```json
{
  "sentiment": "Negative",
  "score": 7,
  "summary": "User expresses confusion and frustration regarding perceived hostility from authority figures.",
  "reasoning": "Phrases like 'mad all the time' and 'idk why' indicate perceived aggression combined with a lack of causal understanding. The informal tone ('chill bro') suggests emotional distance and mild resentment."
}
```

---

## 🏗️ Project Structure

```
sentiment-analyzer-ai/
├── main.py                 # Entry point
├── .env                    # API configuration (git-ignored)
├── pyproject.toml          # Dependency manifest
├── uv.lock                 # Locked environment state
├── analyses/               # Timestamped JSON archives
└── README.md               # You are here
```

---

## 🧩 Why This Exists

Because most sentiment tools are built for marketing teams who want to "track engagement." This is built for people who want to **understand human expression** without the corporate veneer.

- ✅ No training required
- ✅ No model fine-tuning circus
- ✅ No cloud vendor lock-in
- ✅ Just raw, interpretable insight

---

## 🛡️ Security

API keys are managed via `.env` and **never** committed to version control. The `.gitignore` is preconfigured to protect your credentials.

---

## 🎨 Design Principles

1. **Minimalism**: No bloated UI. Terminal-first.
2. **Speed**: `uv` keeps dependencies lean and fast.
3. **Transparency**: Every analysis saved locally. Your data, your disk.
4. **Rebellion**: Built with tools that respect your time (no `npm install` nightmares).

---

## 🤝 Contributing

Pull requests welcome. But remember:  
*"One must still have chaos in oneself to be able to give birth to a dancing star."*

Keep your chaos **structured**.

---

## 📜 License

MIT License. Do whatever you want. Just don't blame me if your professors get analyzed.

---

## 🔗 Links

- **Repository**: [github.com/abdullahzafar08/sentiment-analyzer-ai](https://github.com/abdullahzafar08/sentiment-analyzer-ai)
- **Gemini API**: [ai.google.dev](https://ai.google.dev)
- **uv Package Manager**: [github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---




