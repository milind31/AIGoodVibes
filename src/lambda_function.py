import openai
import tweepy
import os


def lambda_handler(event, context):
    openai.organization = os.getenv("OPEN_AI_ORGANIZATION")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write a quirky and funny, but positive tweet",
        temperature=0.8,
        max_tokens=160,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=1
    )

    generated_tweet = response["choices"][0]["text"]

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    response = client.create_tweet(
        text=generated_tweet
    )
