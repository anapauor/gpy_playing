import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def create_content(topic, tokens, temperature, model="text-davinci-002"):
    prompt = f"Please write an abstract abount {topic} \n\n"
    respuesta = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperature
    )
    return respuesta.choices[0].text.strip()

def resume_text(text, tokens, temperature, model="text-davinci-002"):
    prompt=f"Por favor resume el siguiente texto: {text}\n\n"
    respuesta = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperature
    )
    return respuesta.choices[0].text.strip()

