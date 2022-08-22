import mysql.connector, json
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'

app=Flask(__name__)
cursor=mydb.cursor()
cursor.execute("select * from ventiladores;")
resultados=cursor.fetchall()

@app.route('/dispositivos/ventiladores',methods=['GET'])
def Ventiladores():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"estado":resultados[i ][1],"conexion":resultados[i][2],"nombre":resultados[i][3],"velocidad":resultados[i][4],"timer":resultados[i][5],"sleep":resultados[i][6]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado    
    
@app.route('/dispositivos/ventiladores/cambiarestado',methods=['GET','PUT'])
def estado():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"estado":resultados[i ][1]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado    
    # if estado == 0:
    #     return "APAGADO"
    # else:
    #     return "PRENDIDO"    

@app.route('/dispositivos/ventiladores/verificarconexion',methods=['GET','PUT'])
def conexion():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"conexion":resultados[i ][2]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado 
#     if conexion ==0:
#         return "DESCONECTADO"
#     else:
#         return "CONECTADO"           

@app.route('/dispositivos/ventiladores/editarnombre',methods=['GET','PUT'])
def nombre():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"nombre":resultados[i ][3]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado 
        
@app.route('/dispositivos/ventiladores/cambiarvelocidad',methods=['GET','PUT'])
def velocidad():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"velocidad":resultados[i ][4]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado 

@app.route('/dispositivos/ventiladores/activartimer',methods=['GET','PUT'])
def timer():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"timer":resultados[i ][5]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado 

@app.route('/dispositivos/ventiladores/activarsleep',methods=['GET','PUT'])
def sleep():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"sleep":resultados[i ][6]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado 

cursor.close()
mydb.close()

if __name__=='__main__':
    app.run(debug=True)   

