import mysql.connector
db = mysql.connector.connect(host="localhost",username="root",password="24122000",database="movies")
dbcurs = db.cursor()
mv="Article 15"
st="Silver"
dbcurs.execute(f"select price from MovieList where name='{mv}' and seat='{st}'")
p = 0
for i in dbcurs:
    p = i[0]
print(p*3)
