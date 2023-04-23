import openai
import tweepy
import os


def lambda_handler(event, context):
    generated_tweet = generate_tweet()
    post_tweet(generated_tweet)


def generate_tweet():
    prompt = "You are running a funny and positive twitter account about your life. Please respond only with a positive, funny, and relatable tweet, sometimes with a few weird details. Do not tweet about spilled coffee please."

    openai.organization = os.getenv("OPEN_AI_ORGANIZATION")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=160,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=1
    )

    return clean_response(response)


def clean_response(response):
    generated_tweet = response["choices"][0]["text"].strip()

    if generated_tweet[0] == '"':
        generated_tweet = generated_tweet[1:]
    if generated_tweet[-1] == '"':
        generated_tweet = generated_tweet[:-1]

    return generated_tweet


def post_tweet(tweet):
    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    client.create_tweet(
        text=tweet
    )
