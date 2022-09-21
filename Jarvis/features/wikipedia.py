import requests
import json



def wikipedia():
    url = 'https://en.wikipedia.org/w/api.php'
    wikipedia = requests.get(url).text
    news_dict = json.loads(wikipedia)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getwikipediaUrl():
    return 'https://en.wikipedia.org/w/api.php'