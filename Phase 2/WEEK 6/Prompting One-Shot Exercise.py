import os

from dotenv import load_dotenv #type: ignore
from google import genai
from google.genai import types #type: ignore

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY_1")

if not api_key:
    raise ("API Key is misiing")

Client = genai.Client(api_key=api_key)

try:
    response = Client.models.generate_content(
        model = "gemini-3.5-flash",
        contents = """
        You are a sentiment classification assistant.
        you should describe every review as Positive,Negative,Neutral
        inputs:
        1. I absolutely love this product.
        2. The product is terrible.
        3. The product is okay, nothing special.
        4. The product is excellent, but delivery was disappointing.
        """
    )
    print(response.text)
    
except Exception as e:
    ValueError ("Something went wrong..")
    print(e)
    
finally :
    Client.close()
    
    