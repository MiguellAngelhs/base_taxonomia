from extraccion.models import  Taxonomia
import mysql.connector  as sql

db =sql.connect(
            host = "localhost",
            user = "sammy",
            passwd ="password",
            database="pb_taxonomia"
        )

def search(q):
    q=str(q)
    salida = []  
    cur = db.cursor()
    sql = f"SELECT *, MATCH(file,directory,transcription) AGAINST ('%''{q}''%'  IN NATURAL LANGUAGE MODE) AS relevance_score FROM extraccion_taxonomia WHERE MATCH(file,directory,transcription) AGAINST('%''{q}''%' IN NATURAL LANGUAGE MODE) ORDER BY relevance_score DESC;"
    cur.execute(sql)
    elements = list(cur.fetchall())
    for row in elements:
        test_file = {}
        test_file["id"] = row[0]
        test_file["file"] = row[1]
        test_file["directory"] = row[5]
        test_file["transcription"] = row[7]
        salida.append(test_file)   
    return salida
