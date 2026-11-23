import os

from dotenv import load_dotenv # type: ignore
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY_1")

if not api_key:
    raise ("API key is missing..")

Client = genai.Client(api_key=api_key)

try:
    response = Client.models.generate_content(
        model = "gemini-3.8-flash",
        contents = "Explain python decorators in simple words."
    )
    print(response.text)

except Exception as e:
    ValueError ("Something Went wrong.")
    print(e)
    
finally :
    Client.close()