import numpy as np

loggits = np.array([4.0 , 0.2, 0.2])

temp = 0.5

scaled_val = loggits/temp
expected_val = np.exp(scaled_val)
probability = expected_val/ np.sum(expected_val)
 
#print(f"Probability of Tokens: {probability}")
#print(f"Probability of Token 1: {probability[0]:.4f}")
#print(f"Probability of Token 2: {probability[1]:.4f}")
#print(f"Probability of Token 3: {probability[2]:.4f}")


#Greedy Decoding

prob = [0.70 , 0.20, 0.10]

selected = max(range(len(prob)), key=lambda i: prob[i])

#print(selected)


from google import genai

client = genai.Client(api_key="")

prompt = "Write a short story about a robot that discovers emotions."

temperatures = [0.2, 0.7, 1.2]

for temp in temperatures:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config={"temperature": temp}
    )
    
    print("Temperature : ", temp)
    print(response.text)
    print("-" * 50)