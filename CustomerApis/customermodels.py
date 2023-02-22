from customerdb import mysql
from flask import jsonify




# def home(id):
#     con=mysql.connection.cursor()
#     print("id",id)

#     sql=("SELECT * FROM users where  id = %s")
#     # try:
#     con.execute(sql,id)
#     res=con.fetchall()
#     print("sdfkjhdf")
#     return json.dumps(res)
#     except NameError:
    #     return "There is no method called value"
    # except TypeError:
    #     return "There is something typeerror have found in the project"
    # except:
    #     return "Id not found"

def allEmployees():
    con= mysql.connection.cursor()
    # con.execute("SELECT * FROM users")
    con.callproc('crud.getUsers')
    res = con.fetchall()
    d = list(res)
    con.close()
    return jsonify(d) 








