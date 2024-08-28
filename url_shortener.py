pip install pyshorteners

import pyshorteners

def shorten_url(long_url):
    # Initialize the Shortener
    shortener = pyshorteners.Shortener()

    # Shorten the URL using TinyURL (you can choose other services)
    short_url = shortener.tinyurl.short(long_url)

    return short_url

if __name__ == "__main__":
   
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    print(f"Shortened URL: {short_url}")
