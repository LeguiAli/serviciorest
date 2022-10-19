import mysql.connector
from typing import List


def create_connection() -> mysql.connector.MySQLConnection:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="basebasica"
    )
    print(mydb)
    return mydb


def create_articles(mydb: mysql.connector.MySQLConnection, name='', link='', cosa=''):
    cursor = mydb.cursor()
    sql = "Insert into articles (name, link, otracosa) values (%s, %s, %s)"
    val = (name, link, cosa)
    cursor.execute(sql, val)
    mydb.commit()
    json_result = [{'Amount': cursor.rowcount, 'Message': "record inserted."
                    }]
    return json_result


def get_articles(mydb: mysql.connector.MySQLConnection, keyword: str = '') -> List[dict]:
    cursor = mydb.cursor()
    cursor.execute("Select * from articles where name like '%" + keyword + "%'")
    articles = cursor.fetchall()
    json_result = []
    for article in articles:
        json_result.append({
            'ArticleName': article[1],
            'ArticleCosa': article[2],
            'ArticleLink': article[3]
        })
    return json_result
