
import mysql.connector
from flask import Flask, request, Response, render_template, jsonify


mydb=mysql.connector.connect(host="localhost",database="dispositivos",
user="root",password="")

app=Flask(__name__)
cursor=mydb.cursor()
cursor.execute('select conexion from ventiladores;')
resultado=cursor.fetchall()
print(resultado)
cursor.close()
mydb.close()

@app.route('/', methods=['GET','UPDATE'])
def Dispositivos():
    return {'Ventiladores':resultado}

if __name__=='__main__':
    app.run(debug=True)
   