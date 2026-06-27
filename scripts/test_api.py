from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-7B-Instruct",
    device_map="auto"
)

prompt = "Generate a Gherkin scenario for: As a user, I want to login."

result = pipe(
    prompt,
    max_new_tokens=200,
    do_sample=False
)

print(result[0]["generated_text"])