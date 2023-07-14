import openai

API_KEY = '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'
openai.api_key = API_KEY

question = input("This is the most basic ChatBot ChatGPT based project.\n Ask anything that I'll answer!\n ->")
answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": question}
    ]
)

print(answer)
print(type(answer))
res_a = answer["choices"][0]["message"]["content"]
print(res_a)
print(type(res_a))