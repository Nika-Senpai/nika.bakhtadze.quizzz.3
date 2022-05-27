import requests
import json
import sqlite3
key = "DTViVC1VX6F2leDBVltF95NsA9XgbNQri6Xp4oEK"
url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

r = requests.get(url)

print(r.status_code)
print(r.headers)
print(r.text)


result_json = r.text
res = json.loads(result_json)
res_struct = json.dumps(res, indent=3)
print(res_struct)
e = res['explanation']
t = res['title']
print("სატურნის გიგანტური მთვარე: ", e)




conn = sqlite3.connect('baza.sqlite')
cursor = conn.cursor()

cursor.execute('''create table if not exists baza
(explanation varchar (300), title varchar (25));''')

cursor.execute('insert into baza (explanation, title)'             
               ' VALUES(?,?)',  (e, t))
conn.commit()
conn.close()





