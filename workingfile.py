import requests

api_key = "2a852a20f8114ebe854104f7d2b8902d"

def news():
   
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(main_url).json()
    #print(news)
    article=news["articles"]
    #print(article)

    news_article=[]
    for arti in article:
        news_article.append(arti['title'])
       # print(news_article)

    for i in range(len(news_article)):
        print(i+1,news_article[i])

news()