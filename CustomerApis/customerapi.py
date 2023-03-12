from flask import Flask
from flask_restful import Api
from customerresources import Employess

# from gevent.pywsgi import WSGIServer

app = Flask(__name__)
app.debug = True
app.run(host='0.0.0.0',port=5000)

app.config.from_pyfile('customerdbconfigure.py')

api = Api(app)

api.add_resource(Employess,'/customer/all')

# def get_ip():
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.settimeout(0)
#         try:
#             # doesn't even have to be reachable
#             hostname = socket.gethostname()
#             ipAddress = socket.gethostbyname(hostname)
#             print("Hostname ",ipAddress)
#             s.connect((ipAddress, 1))
#             print("SocketName ",s.getsockname()[0])
#             IP = s.getsockname()[0]
#         except Exception:
#             IP = '127.0.0.1'
#         finally:
#             s.close()
#         return IP

if __name__ == '__main__':
    app.run(debug=True)
    
