import pymongo
import pandas as pd
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://analytics:analytics-password@mflix.2pq79.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = cluster['sample_airbnb']
collection = db['listingsAndReviews']
df = pd.read_csv('movies_initial.csv')
df = df.sample(frac=0.005, replace=True, random_state=1)
data = df.to_dict('record')
collection.insert_many(data)
x = input('Insert the year:\n')
results = collection.find({"year": x}, { "awards": 1, "title": 1,"_id": 0})
a = list(results)
if a == []:
    print('Enter a valid movie name,how about entering The miracle')
df = pd.DataFrame(a)

print(df)
