import os

import openai
import praw
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


reddit = praw.Reddit(client_id=client_id, # the App ID retreived from the reddit application
                     client_secret=client_secret, # the secret retreived from the reddit application
                     user_agent="sentiment analysis  (by anapauorri)"  # add your reddit name
                    )

# reddit instance to obtain public information from reddit!
subreddit_stocks = reddit.subreddit("stocks")


def get_titles_and_comments(subreddit="stocks", sub_instance="hot", limit=10, num_comments=2, skip_first=2):
    subreddit = reddit.subreddit(subreddit)
    titles_and_comments = {}
    for c, post in enumerate(getattr(subreddit, sub_instance)(limit=limit)):
        
        if c < skip_first:
            continue
        
        c+=(1-skip_first)
        
        titles_and_comments[c] = ""

        submission = reddit.submission(post.id)
        title = post.title
        
        titles_and_comments[c] += "Title: " + title  + "\n\n"
        titles_and_comments[c] += "Comments: \n\n"
        
        comment_counter = 0
        for comment in submission.comments:
            comment = comment.body
            if not comment == "[deleted]":
                titles_and_comments[c] += comment + "\n"
                comment_counter+=1
            if comment_counter == num_comments:
                break

    return titles_and_comments


def create_prompt(title_and_comments):

    task = "Return the stock ticker or company in the following heading and comments and classify the sentiment. If no ticker or company is mentioned write 'No company mentioned':\n\n"
    return task + title_and_comments


##### EXECUTION ##### 


titles_and_comments = get_titles_and_comments(subreddit="stocks", limit=12)


# for key, title_and_comments in titles_and_comments.items():
    
#     prompt = create_prompt(title_and_comments)
    
#     response = openai.chat.completions.create(
#                     model="gpt-3.5-turbo-16k",
#                     messages=[{ "role": "user", "content": prompt}],
#                     max_tokens=256,
#                     temperature=0,
#                     top_p=1.0,
#                     frequency_penalty=0.0,
#                     presence_penalty=0.0)
#     print(title_and_comments)
#     print("Sentiment: " + response.choices[0].message.content )
#     print("-"*30)

    
    
with open("output.txt", "w") as file:
    for key, title_and_comments in titles_and_comments.items():
        prompt = create_prompt(title_and_comments)
        
        response = openai.chat.completions.create(
                        model="gpt-3.5-turbo-16k",
                        messages=[{ "role": "user", "content": prompt}],
                        max_tokens=256,
                        temperature=0,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0)

        # Escribe en el archivo
        file.write(title_and_comments + "\n")
        file.write("Sentiment: " + response.choices[0].message.content + "\n")
        file.write("-"*30 + "\n")

        # También imprime en la consola si lo deseas
        print(title_and_comments)
        print("Sentiment: " + response.choices[0].message.content)
        print("-"*30)