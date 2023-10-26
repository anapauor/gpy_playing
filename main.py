
from gpt_program import create_content, resume_text

def main():
    
    tokens = int(input(" Tokens: "))
    temperature = int(input("Set Temperature from 1 to 10")) /10
    topic = input("Topic: ")
    created_article = create_content(topic, tokens, temperature)
    
    # original = input("Text or Article:")

    resumen = resume_text(created_article, tokens, temperature)
    return created_article, resumen

if __name__ == "__main__":
    main()