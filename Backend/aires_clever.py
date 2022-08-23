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

@app.route('/dispositivos/aireacondicionado/cambiarestado',methods=['GET','POST'])
def estado():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET estado='"+estado+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    id=request.args.get('id')
    estado=request.args.get('estado')   
    
    print(estado)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/verificarconexion',methods=['GET','POST'])
def conexion():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET conexion='"+conexion+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    id=request.args.get('id')
    conexion=request.args.get('conexion')   
    
    print(conexion)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/editarnombre',methods=['GET','POST'])
def nombre():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET nombre='"+nombre+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    id=request.args.get('id')
    conexion=request.args.get('nombre')   
    
    print(nombre)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/cambiartemperatura',methods=['GET','POST'])
def temperatura():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET temperatura='"+temperatura+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    temperatura=request.args.get('temperatura')
    ida=request.args.get('id')
    
    print(temperatura)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/activarfan',methods=['GET','POST'])
def fan():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET fan='"+fan+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    temperatura=request.args.get('fan')
    ida=request.args.get('id')
    
    print(fan)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/activarswin',methods=['GET','POST'])
def swin():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET swin='"+swin+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    swin=request.args.get('swin')
    ida=request.args.get('id')
    
    print(swin)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/activartimer',methods=['GET','POST'])
def timer():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET timer='"+timer+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    timer=request.args.get('timer')
    ida=request.args.get('id')
    
    print(timer)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/activarsleep',methods=['GET','POST'])
def sleep():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET sleep='"+sleep+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    sleep=request.args.get('sleep')
    ida=request.args.get('id')
    
    print(sleep)
    return { "status": 200, "state": "OK" }


@app.route('/dispositivos/aireacondicionado/cambiarmodo',methods=['GET','POST'])
def modo():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET modo='"+modo+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    modo=request.args.get('modo')
    id=request.args.get('id')
    
    print(modo)
    return { "status": 200, "state": "OK" }


@app.route('/dispositivos/aireacondicionado/cambiardireccion',methods=['GET','POST'])
def direccion():
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET direccion='"+direccion+"' WHERE id='"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    direccion=request.args.get('direccion')
    ida=request.args.get('id')
    
    print(direccion)
    return { "status": 200, "state": "OK" }

cursor.close()
mydb.close()
    
if __name__=='__main__':
    app.run(debug=True)
