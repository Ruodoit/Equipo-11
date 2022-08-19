#!/usr/bin/env python
# coding: utf-8
import mysql.connector, json
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="localhost",database="dispositivos",
user="root",password="")

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
    
@app.route('/dispositivos/ventiladores/estado',methods=['GET','UPDATE'])
def estado():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"estado":resultados[i ][1]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
        return resultado    
    if estado == 0:
        return "OFF"
    else:
        return "ON"    

@app.route('/dispositivos/ventiladores/conexion',methods=['GET','UPDATE'])
def conexion():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"conexion":resultados[i ][2]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
        return resultado    

    cursor.close()
    mydb.close()

if __name__=='__main__':
    app.run(debug=True)   

