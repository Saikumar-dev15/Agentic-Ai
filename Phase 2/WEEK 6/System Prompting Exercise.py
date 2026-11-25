import os

from dotenv import load_dotenv #type: ignore
from google import genai
from google.genai import types #type: ignore

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY_1")

if not api_key:
    raise ("API Key is missing")

Client = genai.Client(api_key=api_key)

try:
    response = Client.models.generate_content(
        model = "gemini-3.5-flash",
        config = types.GenerateContentConfig(
            system_instruction = """
            You are a sentiment classification assistant.

            Rules:
            1. Classify text into Positive, Negative or Neutral.
            2. Never provide explanations.
            3. Return only one classification.
            4. If the text is ambiguous, return Neutral.
            
            """   
        ),
        contents = """
        1. I absolutely love this product.
        
        2. The product is terrible.
        
        3. The product is okay, nothing special.
        
        4. The product is excellent, but delivery was disappointing.
        """
    )
    print(response.text)
    
except Exception as e:
    ValueError ("something went wrong")
    print(e)
    
finally:
    Client.close()