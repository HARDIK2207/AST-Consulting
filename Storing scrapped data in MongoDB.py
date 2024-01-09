from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
df = pd.read_csv('cleaned job data.csv')
data_dict = df.to_dict(orient='records')
uri = "mongodb+srv://hardikcs2207:wind123@cluster0.qjtbwsv.mongodb.net/"
client = MongoClient(uri)
db = client['Indeedjobs']
collection = db['pythondeveloper']

collection.insert_many(data_dict)
print(collection.count_documents({}))