import os
import json
from datetime import datetime
from dotenv import load_dotenv
from pydantic import BaseModel, constr, ValidationError
import google.generativeai as genai

# 1. Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

class UserInput(BaseModel):
    text: constr(min_length=1, strip_whitespace=True, max_length=2000)

def analyze_text(text: str):
    """Analyzes the sentiment of the text using Gemini."""
    try:
        validated = UserInput(text=text)
    except ValidationError as e:
        return {"error": f"Input validation error: {e}"}

    try:
        # 2. Using the model explicitly listed for your key
        model = genai.GenerativeModel("gemini-3-flash-preview")

        # 3. Request structured JSON
        prompt = (
            f"Analyze the sentiment of this text: '{validated.text}'. "
            "Return ONLY a JSON object with these keys: "
            "'sentiment' (Positive/Negative/Neutral), 'score' (1-10), "
            "'summary', and 'reasoning'."
        )

        response = model.generate_content(
            prompt, generation_config={"response_mime_type": "application/json"}
        )

        # 4. Parse and Save
        data = json.loads(response.text)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analysis_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        
        return data

    except Exception as e:
        return {"error": f"Error: {e}"}

def analyze_vibe():
    user_input = input("Enter text to analyze: ").strip()
    
    print(f"\n🚀 Sending to Gemini 3 Flash (The Edge of AI)...")
    
    result = analyze_text(user_input)
    
    if "error" in result:
        print(f"❌ {result['error']}")
    else:
        print(f"✅ Success! Saved results.")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    analyze_vibe()
