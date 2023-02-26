from flask import Flask
from flask_restful import Api
from customerresources import Employess
import ipaddress

app = Flask(__name__)

app.run(host='192.168.184.101',debug=True,port=8000)

app.config.from_pyfile('customerdbconfigure.py')

api = Api(app)

api.add_resource(Employess,'/customer/all')


# def socketFind():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(('10.0.0.0', 0)) 
#     print("Socket",s.getsockname()[0])

# def get_Host_name_IP():
#     try:
#         host_name = socket.gethostname()
#         host_ip = socket.gethostbyname(host_name)
#         print("Hostname :  ", host_name)
#         print("IP : ", host_ip)
#     except:
#         print("Unable to get Hostname and IP")

# get_Host_name_IP()

if __name__ == '__main__':
    app.run(debug=True)
    
