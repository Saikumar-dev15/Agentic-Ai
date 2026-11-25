import os
from google import genai
from dotenv import load_dotenv #type: ignore 

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY_1")

if not api_key:
    raise "API Key is Missing."

Client = genai.Client(api_key=api_key)

try:
    response = Client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = """
        Explain Python Dictionaries
        
        give:
        1.what is Dictionaries.
        2.syntax
        3.explain line by line code
        4.give 3 practice problems
        """
        
    )
    print(response.text)
    
except Exception as e:
    ValueError ("There is something wrong..")
    print(e) 
    
finally: 
    Client.close()
    
    
#System Prompting....
from google.genai import types # type: ignore

try :
    response = Client.models.generate_content(
        model = "gemini-3.5-flash",
        config =types.GenerateContentConfig(
            system_instruction ="""
            you are python programming tutor.
            
            Explain concepts of python to begginer.
            explain the code line by line to user.
            give three practice problems.
            Don't go to advance level until the user instruct.
            make master in the programming from basics.
            """
        ),
        contents = "Explain the Python dictionaries."
    )
    print(response.text)
    
except Exception as e:
    ValueError ("Something went wrong")
    print(e)
    
finally:
    Client.close()