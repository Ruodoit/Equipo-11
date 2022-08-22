import mysql.connector, json
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
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
    
@app.route('/dispositivos/ventiladores/cambiarestado',methods=['GET','POST'])
def estado():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET estado=estado WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    estado=request.args.get('estado')
    ida=request.args.get('id')
    
    print(estado)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/ventiladores/verificarconexion',methods=['GET','POST'])
def conexion():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET conexion=conexion WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    conexion=request.args.get('conexion')
    ida=request.args.get('id')
    
    print(conexion)
    return { "status": 200, "state": "OK" }
    
@app.route('/dispositivos/ventiladores/editarnombre',methods=['GET','POST'])
def nombre():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET nombre=nombre WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    nombre=request.args.get('nombre')
    ida=request.args.get('id')
    
    print(nombre)
    return { "status": 200, "state": "OK" }
        
@app.route('/dispositivos/ventiladores/cambiarvelocidad',methods=['GET','POST'])
def velocidad():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET velocidad=velocidad WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    velocidad=request.args.get('velocidad')
    ida=request.args.get('id')
    
    print(velocidad)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/ventiladores/activartimer',methods=['GET','POST'])
def timer():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET timer=timer WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    timer=request.args.get('timer')
    ida=request.args.get('id')
    
    print(timer)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/ventiladores/activarsleep',methods=['GET','POST'])
def sleep():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET sleep=sleep WHERE id=id;")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    sleep=request.args.get('sleep')
    ida=request.args.get('id')
    
    print(sleep)
    return { "status": 200, "state": "OK" }


cursor.close()
mydb.close()

if __name__=='__main__':
    app.run(debug=True)   

