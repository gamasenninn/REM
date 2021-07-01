import sqlite3
import sys

if len(sys.argv) > 2:
    db_name = sys.argv[1]   
    sql_file = sys.argv[2]
elif len(sys.argv) > 1:
    db_name = ":memory:"
    sql_file = sys.argv[1]
elif len(sys.argv) == 1:
    db_name = ":memory:"
    sql_file = "make_db.sql"
    

#------ SQL ファイルの読み込み-------
try:
    with open(sql_file,"r") as f:
        sqlall = f.read()

except Exception as e:
    print(e)
    sys.exit()
    

#------ スクリプト実行 -------

conn = sqlite3.connect(db_name)

c = conn.cursor()

c.executescript(sqlall)

#------ 確認 -------
    
c = conn.cursor()
c.execute("select name from sqlite_master where type='table'" )
ret = c.fetchall()
print ("ret:",ret)


conn.commit();
conn.close();
