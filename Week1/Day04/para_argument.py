import requests

url="https://api.github.com/search/repositories"

params={
    "q":"python",
    "sort":"stars"
}
response=requests.get(url,params=params)
data=response.json()
for repo in data["items"][:3]:
    print(repo["name"])