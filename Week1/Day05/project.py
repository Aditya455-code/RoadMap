import requests
import pandas as pd
from collections import defaultdict

post_url="https://jsonplaceholder.typicode.com/posts"
comment_url="https://jsonplaceholder.typicode.com/comments"

posts=requests.get(post_url).json()
comments=requests.get(comment_url).json()

comment_count=defaultdict(int)

for comment in comments:
    post_id=comment["postId"]
    comment_count['post_id']+=1

for post in posts:
    post_id=post['id']
    post['comment_count']=comment_count[post_id]

df=pd.DataFrame(posts)
df.to_csv("postandcommentcount.csv",index=False)
print(df.head())


