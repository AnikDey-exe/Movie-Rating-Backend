import pandas as pd
import numpy as np

df2 = pd.read_csv('final.csv')

# content_shared = df1[(df1['eventType'] == 'CONTENT SHARED')].shape[0]
# print(content_shared)

articles = df2.copy().loc[1:]

def count(x):
  view = x[(df2['eventType'] == 'VIEW')].shape[0]
  follow = x[(df2['eventType'] == 'FOLLOW')].shape[0]
  like = x[(df2['eventType'] == 'LIKE')].shape[0]
  bookmark = x[(df2['eventType'] == 'BOOKMARK')].shape[0]
  comment_created = x[(df2['eventType'] == 'COMMENT CREATED')].shape[0]

  return view + follow + like + bookmark + comment_created

articles['score'] = articles.apply(count, axis=0)
articles = articles.sort_values('score', ascending=False)
