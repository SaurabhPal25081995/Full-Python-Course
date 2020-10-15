# Akhbaar padhke sunaao
import requests
import json
import pyttsx3

def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=dd7b7621e5494acb991477c25c103d0a"
    news = requests.get(url).text
    # print("News-",news)
    # print(type(news))
    news_dict = json.loads(news)
    # print("News_dict",news_dict)
    # print(type(news_dict))

    arts = news_dict['articles']

    # for article in arts:
    #     print(article['title'])
    #     speak(article['title'])
    #     speak("Moving on to the next news..Listen Carefully")

    #Give top 10 news
    for i in range(0,11):
        print(news_dict['articles'][i]['title'])
        speak(news_dict['articles'][i]['title'])
