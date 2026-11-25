import os

from dotenv import load_dotenv #type: ignore
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY_1")

if not api_key:
    raise ("API key is missing..")

Client = genai.Client(api_key= api_key)

try:
    response = Client.models.generate_content(
        model = "gemini-3.5-flash",
        contents = """
        you are sentimate classification assistent.
        
        you should describe every review based on Positive , Negative , Neutral.
        for example:
        1. input: The product is amazing.like good comments.
           output: Positive
           
        2. input : the product is worst. like negative comments.
           output : Negative
           
        3.input : the product is good , but the delivery was late.
           output : Neutral 
           
        Inputs: 
        1. I absolutely love this product.

        2. The product is terrible.

        3. The product is okay, nothing special.

        4. The product is excellent, but delivery was disappointing.
        """
        
    )
    print(response.text)
    
except Exception as e:
    ValueError ("SOmething went wrong")
    print(e)
    
finally:
    Client.close()