import requests
import json
import pandas as pd
from fake_useragent import UserAgent

# choose keyword
keyword = "bitcoin"
keyword.replace(" ", "+")


# create url
myurl = "http://suggestqueries.google.com/complete/search?output=chrome&hl=en&gl=us&q=" + keyword

# create the user_agent to request
ua = UserAgent()
headers = {"user-agent": ua.chrome}
response = requests.get(myurl, headers=headers, verify=False)
suggestions = json.loads(response.text)

# create a list with response
keyword_list = []
keyword_suggestion_list = []
for i in range(1, 6):
    keyword_list.append(keyword)
    keyword_suggestion_list.append(suggestions[1][i])

print("keyword_suggestion_list: ", keyword_suggestion_list)