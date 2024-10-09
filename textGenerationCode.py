from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def generate_text(input_text, max_len = 1000):
    generated_text = generator(input_text, max_length = max_len)
    return generated_text[0]['generated_text']