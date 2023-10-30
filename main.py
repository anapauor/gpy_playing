
from gpt_functions import create_content, resume_text

def main():
    
    tokens = int(input(" Tokens: "))
    temperature = int(input("Set Temperature from 1 to 10: ")) /10
    topic = input("Topic: ")
    created_article = create_content(topic, tokens, temperature)
    print (create_content)
    # original = input("Text or Article:")

    tokens_abstract = int(input(" Tokens for abstract: "))
    abstract = resume_text(created_article, tokens_abstract, temperature)
    print(abstract)

if __name__ == "__main__":
    main()