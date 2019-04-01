from pymongo import MongoClient
import json

FILE = "/Users/bhuang/Downloads/agencies.json"

client = MongoClient ('localhost', 27017)
db = client['Test']
collection = db['Agency']


with open(FILE) as f:
    file_data = json.load(f)
    print("-- There are {} states in the file".format(len(file_data)))
    for state, agencies in file_data.items():
      print("There are {} agencies in {}".format(len(agencies), state)) 
      for id, agency in agencies.items():
        collection.insert(agency)      
client.close()

