import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = r"C:\Users\samuel\Desktop\python screens\programs\IBM projects\top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count=0
page=requests.get('https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films')
src_code=page.content
soup=BeautifulSoup(src_code,'html.parser')
tables=soup.find_all("tbody")
rows=tables[0].find_all("tr")
print(len(rows))
for i in rows:
    if count<50:
        column=i.find_all("td")
        if len(column)!=0:
            dict={"Average Rank":int(column[0].contents[0]),"Film":str(column[1].contents[0]),"Year":int(column[2].contents[0])}
            df1=pd.DataFrame(dict,index=[0])
            df=pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break
print(df)
df.to_csv(csv_path)
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()