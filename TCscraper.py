from bs4 import BeautifulSoup
from datetime import datetime
# from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
# db = client.TopChef_db
# collection = db.episodes

stub = open('./wiki/TopChef_Season6.html',encoding="utf8")
count = len(open('./wiki/TopChef_Season6.html',encoding="utf8").readlines())
soup = BeautifulSoup(stub, 'html.parser')
chefarray=[]
episodearray=[]
tag=soup.tbody.td
print(tag)
season=6
try:
    while True:
        entry={'season':season}
        entry['name']=tag.string
        tag=tag.next_sibling.next_sibling
        entry['hometown']=tag.text
        tag=tag.next_sibling.next_sibling
        entry['current_residence']=tag.string
        tag=tag.next_sibling.next_sibling
        entry['age']=int(tag.string)
        chefarray.append(entry)
        print(chefarray)
        tag=tag.parent.next_sibling.next_sibling.td
except:
    pass
print(chefarray)
tag=soup.tbody.parent.next_sibling.next_sibling.next_sibling.next_sibling
try:
    while True:
        entry={'season':season}
        

print(tag)
# result=collection.insert_many(entryarray)