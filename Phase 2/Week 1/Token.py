import tiktoken

encoding = tiktoken.get_encoding("o200k_base")

text = "I Love You too Vyshnavi"

tokens = encoding.encode(text)

#print(tokens)
#print(len(tokens))


def tokenizer(text):
    
    encoding = tiktoken.get_encoding("o200k_base")
    
    token = encoding.encode(text)
    
    print(f"Text : {text}")
    print(f"Tokens: {token}")
    print(f"Length of the tokens : {len(token)}")
    
user_input = input("Enter a text: ")

tokenizer(user_input)