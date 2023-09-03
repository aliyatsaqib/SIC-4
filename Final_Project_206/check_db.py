from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://aliyatsaqib:WAEh6i11rr1GCwT6@iopark.u3958vi.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
db = client['surakarta206'] # ganti sesuai dengan nama database kalian
my_collections = db['user'] # ganti sesuai dengan nama collections kalian

def checkid(id_card):
	try : 
		
		id=my_collections.find({ "id_card": id_card })
		for data in id: 
			print(data)
		return data, True
	except: 
		print(id_card)
		return id_card, False
		
