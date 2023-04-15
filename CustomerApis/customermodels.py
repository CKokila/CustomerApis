from customerdb import mysql
from flask import jsonify




def home(id):
    con=mysql.connection.cursor()
    print("id",id)
    try:
        con.execute("SELECT * FROM users where  id = %d",(id))
        res=con.fetchall()
        print("sdfkjhdf")
        return jsonify({
        "status":200,
        "data":res,
         "message":"Data read successfully"
        })
    except NameError:
        return "There is no method called value"
    except TypeError:
        return "There is something typeerror have found in the project"
    except:
        return "Id not found"


def allEmployees():
    try:
        con= mysql.connection.cursor()
        con.execute("SELECT * FROM users")
        # con.callproc('crud.getUsers')
        res = con.fetchall()
    # d = list(res)
        con.close()
        return jsonify({
        "status":200,
        "data":res,
         "message":"Data read successfully"
        })
    except NameError:
        return "There is no method called value"
    except TypeError:
        return "There is something typeerror have found in the project"
    except:
        return "Id not found" 

def getAllProducts():
    con= mysql.connection.cursor()
    con.execute("SELECT * FROM products")
    res = con.fetchall()
    con.close()
    return jsonify({
        "status":200,
        "data":res,
         "message":"Data read successfully"
        }) 

def getProductById(id):
    con= mysql.connection.cursor()
    sql=("SELECT * FROM users where  id = %s")
    con.execute(sql,id)
    res = con.fetchall()
    con.close()
    return jsonify({
        "status":200,
        "data":res,
         "message":"Data read successfully"
        }) 



