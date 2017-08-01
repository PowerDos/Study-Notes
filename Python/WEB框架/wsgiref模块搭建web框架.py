# wsgiref模块
from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    # environ 客户端发送来的所以数据
    # start_response 封装要返回给用户的数据，响应头
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 返回内容
    return ['<h1>Hello, Web Frame!</h1>'.encode('utf-8'),]

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()


















