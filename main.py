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


def analyze_vibe():
    user_input = input("Enter text to analyze: ").strip()

    class UserInput(BaseModel):
        text: constr(min_length=1, strip_whitespace=True, max_length=2000)

    try:
        validated = UserInput(text=user_input)
    except ValidationError as e:
        print("❌ Input validation error:")
        print(e)
        return

    print(f"\n🚀 Sending to Gemini 3 Flash (The Edge of AI)...")

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

        print(f"✅ Success! Saved results to {filename}")
        print(json.dumps(data, indent=2))

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    analyze_vibe()
