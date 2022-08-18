import mysql.connector
from flask import Flask, request, Response, jsonify, render_template

mydb=mysql.connector.connect(host="localhost",database="dispositivos",
user="root",password="")

app=Flask(__name__)

@app.route('/', methods=['GET','UPDATE'])
def verificarConexion():
    cursor=mydb.cursor()
    cursor.execute("select temperatura, conexion from aireacondicionado;")
    resultado=cursor.fetchall()
    print(resultado)
    cursor.close()
    mydb.close()
    return {'Aires':resultado}

# @app.route('/', methods=['GET'])
# def temperatura():
#     cursor=mydb.cursor()
#     cursor.execute("select temperatura from aireacondicionado;")
#     resultado=cursor.fetchall()
#     print(resultado)
#     cursor.close()
#     mydb.close()
#     return {'Aires':resultado}

if __name__=='__main__':
    app.run(debug=True)
   

'''
r=request.get('RUTA')
print(r)
print(r.content)

r=request.post('RUTA',data={'key':'value'})
print(r)
print(r.json())

class Aacc:
    def __init__(self,estado,conexion,nombre='',temperatura='',swin,fan,modo,direccion,eco,timer='',sleep=''):
        self.estado=estado
        self.conexion=conexion
        self.nombre=nombre
        self.temperatura=temperatura
        self.swin=swin
        self.fan=fan
        self.modo=modo
        self.direccion=direccion
        self.eco=eco
        self.timer=timer
        self.sleep=sleep
'''