from pymongo import MongoClient
user= 'root'
password = 'MTc5MTkta2F4****'
host='localhost'

connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 

db = connection.training

# select the 'mongodb_glossary' collection 

collection = db.mongodb_glossary

doc = {"database":"a database contains collections"},

{"collection":"a collection stores the documents"},

{"document":"a document contains the data in the form or key value pairs."}

# insert a sample document

print("Inserting documents into collection.")

db.collection.insert_many(doc)

# query for all documents in 'training' database and 'python' collection

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()
