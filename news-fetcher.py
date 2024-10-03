import requests
from colorama import Fore, Style, init

# Initialize colorama on Windows
init()

# Global counter to keep track of the article number
article_counter = 0

def display_news(api_key, keyword, count):
    global article_counter

    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    response = requests.get(url)

    while True:
        if response.status_code == 200:
            articles = response.json().get('articles', [])

            if not articles:
                print("No articles found.")
                return  # No need to continue if no articles are found

            for i, article in enumerate(articles[(article_counter):(count+article_counter)]):
                title = article.get('title', 'No Title')
                content = article.get('content', 'No Content')
                article_url = article.get('url', 'No URL')  # Get the article URL
                article_counter += 1
                print(Fore.RED + f"{article_counter}. Title: {title}\n" + Style.RESET_ALL)
                paragraphs = content.split('\n')
                for paragraph in paragraphs:
                    print(paragraph)
                print(f"(*--URL--*: {article_url})\n")
                print('-' * 20)

        else:
            print(f"Error: {response.status_code}")
            break

        show_more = input("Do you want to see more topics? (y=yes, else it will exit): ").lower()

        if show_more != 'y':
            article_counter = 0
            print('-' * 50)
            print('-' * 50)
            print(Fore.CYAN+ "----Going Back to the Search Bar----" +Style.RESET_ALL)
            print('-' * 50)
            print(('-' * 50)+"\n")    
            break
        else:
            print('-' * 20)
            

# Set api_key before entering the loop
api_key = '6a13bd76c7b141499c3a30955a057862'

while True:
    response = input(Fore.MAGENTA+"What News Are You Interested In? (-e:exit):"+Style.RESET_ALL)
    if response != "-e":
        keyword = response.replace(" ", "-")
        initial_display_count = 10 #at default we receive only 100 articles at once, we just show 5 at once, then load accordingly.
        display_news(api_key, keyword, initial_display_count)
    else:
        break
