# # import json
# # import http.server
# # import socketserver
# # from typing import Tuple
# # from http import HTTPStatus
# # import requests

# # class Handler(http.server.SimpleHTTPRequestHandler):

# #     def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
# #         print(request)
# #         super().__init__(request, client_address, server)

# #     @property
# #     def api_response(self):
# #         print(requests)
# #         import use_cifar
# #         #return json.dumps({"message": "Hello world"}).encode()

# #     def do_GET(self):
# #         if self.path == '/':
# #             self.send_response(HTTPStatus.OK)
# #             self.send_header("Content-Type", "application/json")
# #             self.end_headers()
# #             self.wfile.write(bytes(self.api_response))


# # if __name__ == "__main__":
# #     PORT = 8000
# #     # Create an object of the above class
# #     my_server = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
# #     # Star the server
# #     print(f"Server started at {PORT}")
# #     my_server.serve_forever()

# #####################

# # import json

# # from typing import List

# # from http.server import HTTPServer
# # from http.server import BaseHTTPRequestHandler

# # from attrs import asdict
# # from attrs import define

# # HOST = "127.0.0.1"
# # PORT = 8027 # <----- nailed it in the 27th try :)

# # @define
# # class Entry:

# #     name: str
# #     some_list: List[int]

# # class Handler(BaseHTTPRequestHandler):
# #     def do_POST(self):
        
# #         # read incoming sent data
# #         data = self.rfile.read(self._sent_data_size)
        
# #         # do something with it ...
# #         response = self._process(data)#.decode("utf-8"))

# #         # perpare the (json) response
# #         jsonbytes = self._prepare_json_response(response)
                    
# #         # send the (json) response back ...
# #         self.wfile.write(jsonbytes)

# #     def _process(self, data: str) -> List[Entry]:
# #         return [
# #             Entry("employee"+str(i), [d["id"], d["salary"]])
# #             for i, d in enumerate(json.loads(data))
# #         ]

# #     def _prepare_json_response(self, response: List[Entry]) -> bytes:
# #         self.send_response(200)
# #         self.send_header("Content-type", "application/json")
# #         self.end_headers()
# #         jsonstr = json.dumps(
# #             response,
# #             indent=4,
# #             default=asdict
# #         )
# #         return jsonstr.encode()

# #     @property
# #     def _sent_data_size(self) -> int:
# #         return int(self.headers.get("Content-Length"))

# # server = HTTPServer((HOST, PORT), Handler)
# # server.serve_forever()
# # server.serve_close()

# ########

# # Using flask to make an api
# # import necessary libraries and functions
# from flask import Flask, jsonify, request
  
# # creating a Flask app
# app = Flask(__name__)
  
# # on the terminal type: curl http://127.0.0.1:5000/
# # returns hello world when we use GET.
# # returns the data that we send when we use POST.
# @app.route('/', methods = ['GET', 'POST'])
# def home():
#     if(request.method == 'POST'):
#         data = "hello world"
#         return jsonify({'data': data})
        
  
  
# # A simple function to calculate the square of a number
# # the number to be squared is sent in the URL when we use GET
# # on the terminal type: curl http://127.0.0.1:5000 / home / 10
# # this returns 100 (square of 10)
# @app.route('/home/<int:num>', methods = ['GET'])
# def disp(num):
  
#     return jsonify({'data': num**2})
  
  
# # driver function
# if __name__ == '__main__':
  
#     app.run(debug = True)

#############################

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
#arr.reshape(3, -1)
print(arr)