from pymongo import MongoClient

client = MongoClient("theory.cpe.ku.ac.th", username="user07", password="pass07")
db = client.examples
olympics = db.olympics

gcount = olympics.count_documents({"country":"THA", "medal":"Gold"})
scount = olympics.count_documents({"country":"THA", "medal":"Silver"})
bcount = olympics.count_documents({"country":"THA", "medal":"Bronze"})
print('Thailand has', gcount, 'golds, ', scount, 'silvers, and', bcount, 'bronzes.')

"""
for m in olympics.find({"country": "THA"}):
    if m ['sport'] != 'Boxing':
        print(m["athlete"])

"""