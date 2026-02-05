```markdown
# ⚡ Gemini 3 Sentiment Engine

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://python.org)
[![Model](https://img.shields.io/badge/Model-Gemini_3_Flash-orange.svg)](https://ai.google.dev)
[![Manager](https://img.shields.io/badge/Package_Manager-uv-purple.svg)](https://github.com/astral-sh/uv)

A high-performance sentiment analysis engine powered by Google's Gemini 3 Flash. Transforms raw text into structured JSON with validated sentiment scoring and reasoning.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="25" /> **Core Functionality**

```
Raw Text Input → Gemini 3 Flash Processing → Structured JSON Output → Local Archive
```

- **AI Model**: Google Gemini 3 Flash (latest generation)
- **Output Format**: Validated JSON schema with sentiment classification
- **Storage**: Timestamped local `.json` files for every analysis
- **Security**: Environment-based API key management

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Desktop%20Computer.png" width="25" /> **Tech Stack**

| Component | Technology |
|-----------|-----------|
| **AI Core** | Google Gemini 3 Flash SDK |
| **Package Manager** | `uv` (Rust-powered, faster than pip) |
| **Environment** | Python 3.14+ |
| **Data Format** | JSON with strict schema validation |
| **Security** | `.env` configuration |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" width="25" /> **Installation**

### Prerequisites
- Python 3.14 or higher
- Gemini API key ([Get one here](https://ai.google.dev))
- `uv` package manager ([Installation guide](https://github.com/astral-sh/uv))

### Setup

```bash
# Clone repository
git clone https://github.com/abdullahzafar08/sentiment-analyzer-ai.git
cd sentiment-analyzer-ai

# Install dependencies
uv sync
```

### Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Writing%20Hand.png" width="25" /> **Usage**

```bash
uv run python main.py
```

### Example Session

```
C:\Users\Hp\sentiment-analyzer\main.py:5: FutureWarning:
https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

    import google.generativeai as genai
Enter text to analyze: Jack of all trades master of none but often times better than one.

🚀 Sending to Gemini 3 Flash (The Edge of AI)...
✅ Success! Saved results to analysis_20260205_190654.json
{
  "sentiment": "Positive",
  "score": 7,
  "summary": "A positive subversion of a common idiom that praises versatility over narrow specialization.",
  "reasoning": "While the phrase 'master of none' is often used as a critique, the addition of the final clause 'often times better than one' reframes the statement. It elevates the status of a generalist above that of a single-subject specialist, creating an affirming and empowering sentiment."
}
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/File%20Folder.png" width="25" /> **Project Structure**

```
sentiment-analyzer-ai/
├── main.py                 # Core application entry point
├── .env                    # API key configuration (git-ignored)
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
├── analyses/               # Timestamped JSON output storage
└── README.md               # Documentation
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" width="25" /> **Output Schema**

Each analysis generates a JSON file with the following structure:

```json
{
  "sentiment": "Positive|Negative|Neutral",
  "score": 1-10,
  "summary": "Brief interpretation of the input text",
  "reasoning": "Detailed explanation of sentiment classification"
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `sentiment` | String | Classification: Positive, Negative, or Neutral |
| `score` | Integer | Intensity rating from 1 (weak) to 10 (strong) |
| `summary` | String | Concise analysis of the input text |
| `reasoning` | String | Detailed justification for the classification |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Locked.png" width="25" /> **Security**

- API keys stored in `.env` (excluded from version control)
- No external data transmission beyond Gemini API calls
- Local-first architecture—all analyses saved on your machine

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="25" /> **Features**

✅ Real-time sentiment analysis  
✅ Structured JSON output with validation  
✅ Timestamped persistent storage  
✅ Zero-dependency inference (powered by Gemini SDK)  
✅ Fast package management with `uv`  
✅ Secure API key handling

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Link.png" width="25" /> **Links**

- **Repository**: [github.com/abdullahzafar08/sentiment-analyzer-ai](https://github.com/abdullahzafar08/sentiment-analyzer-ai)
- **Gemini API Documentation**: [ai.google.dev](https://ai.google.dev)
- **uv Package Manager**: [github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" width="25" /> **Contributing**

Pull requests welcome. Please ensure:
- Code follows existing style conventions
- All tests pass before submission
- Commit messages are descriptive

---


