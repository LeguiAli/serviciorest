import mysql.connector
mydb = None


def createConnection():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="basebasica"
    )
    print(mydb)
createConnection()

def create_articles(name='', link='', cosa=''):
    cursor = mydb.cursor()
    sql = "Insert into articles (name, link, otracosa) values (%s, %s, %s)"
    val = (name, link, cosa)
    cursor.execute(sql, val)
    mydb.commit()
    jsonResult = []
    jsonResult.append({'Amount': cursor.rowcount,'Message': "record inserted."
                       })
    return jsonResult

def get_articles(keyword=''):
    cursor = mydb.cursor()
    cursor.execute("Select * from articles where name like '%"+keyword+"%'")
    articles = cursor.fetchall()
    jsonResult = []
    for article in articles:
        jsonResult.append({
            'ArticleName':article[1],
            'ArticleCosa': article[2],
            'ArticleLink':article[3]
        })
    return jsonResult