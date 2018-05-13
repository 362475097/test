#!/usr/bin/env python
# _*_coding:utf-8 _*_
__author__ = "Gao"

import socketserver

class MyTcpHandler(socketserver.BaseRequestHandler):
    '''自定义一个请求处理类'''

    def setup(self):    #可以定义处理请求前需要做的事情
        pass

    def handle(self):
        while True:
            try:
                # self.data = self.request.recv(1024).decode('utf-8')
                # print('接收到的数据:', self.data)
                res = '135348'

                self.request.sendall(res.encode('utf-8'))
            except ConnectionResetError as e:
                print('客户端%s已断开连接'%self.client_address[0])
                break

    def finish(self):    #可以定义处理请求后需要做的事情
        pass




if __name__ == '__main__':
    #server = socketserver.TCPServer(('localhost', 2221), MyTcpHandler)    #只能同时处理一个请求
    server = socketserver.ThreadingTCPServer(('localhost', 2221), MyTcpHandler)    #使用多线程的方式处理多个请求
    #server = socketserver.ForkingTCPServer(('localhost', 2221), MyTcpHandler)    #使用多进程的方式处理多个请求
    server.serve_forever()
    #server.handle_request()


