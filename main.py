import requests
from bs4 import BeautifulSoup

target_url = "https://www.enchantedlearning.com/wordlist/food.shtml"

response = requests.get(target_url)

soup = BeautifulSoup(response.text, "html.parser")

items = []

for i in soup.find_all(class_= "wordlist-item"):
    items.append(i.text)

export_path = target_url.split("/")[-1].split(".")[0] + ".txt"

with open(export_path, mode = "w") as file:
    file.write("\n".join(items))