import requests

response = requests.get("https://news.ycombinator.com/")

print(response.text)