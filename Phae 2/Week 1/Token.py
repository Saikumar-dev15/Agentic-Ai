import tiktoken

encoding = tiktoken.get_encoding("o200k_base")

text = "I Love You Vyshnavi"

tokens = encoding.encode(text)

print(tokens)
print(len(tokens))