# /opt/project-alpha/api_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
# 设置响应头，告诉浏览器返回的是 JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
# 模拟后端数据
        response = {"status": "active", "service": "OrderService", "2.0 - Docker Edition"}
        self.wfile.write(json.dumps(response).encode())
# 服务监听所有 IP (空字符串) 的 8080 端口
server_address = ('', 8080)
print("Microservice starting on port 8080...")
httpd = HTTPServer(server_address, SimpleAPI)
httpd.serve_forever()
