import mysql.connector
from flask import Flask, request, Response, jsonify, render_template

mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'

app=Flask(__name__)
cursor=mydb.cursor()
cursor.execute("select * from aireacondicionado;")
resultados=cursor.fetchall()

@app.route('/dispositivos/aireacondicionado',methods=['GET'])
def aires():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"estado":resultados[i ][1],"conexion":resultados[i][2],"nombre":resultados[i][3],"temperatura":resultados[i][4],"fan":resultados[i][5],"swin":resultados[i][6],"timer":resultados[i][7],"sleep":resultados[i][8],"modo":resultados[i][9],"direccion":resultados[i][10]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/cambiarestado',methods=['GET','PUT'])
def estado():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"estado":resultados[i ][1]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/verificarconexion',methods=['GET','PUT'])
def conexion():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"conexion":resultados[i ][2]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/editarnombre',methods=['GET','PUT'])
def nombre():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"nombre":resultados[i ][3]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/cambiartemperatura',methods=['GET','PUT'])
def temperatura():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"temperatura":resultados[i ][4]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/activarfan',methods=['GET','PUT'])
def fan():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"fan":resultados[i ][5]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/activarswin',methods=['GET','PUT'])
def swin():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"swin":resultados[i ][6]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/activartimer',methods=['GET','PUT'])
def timer():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"timer":resultados[i ][7]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/activarsleep',methods=['GET','PUT'])
def sleep():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"sleep":resultados[i ][8]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/cambiarmodo',methods=['GET','PUT'])
def modo():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"modo":resultados[i ][8]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/cambiardireccion',methods=['GET','PUT'])
def direccion():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"direccion":resultados[i ][8]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado


cursor.close()
mydb.close()
    
if __name__=='__main__':
    app.run(debug=True)
