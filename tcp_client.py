import socket

# 目标服务器 IP 和端口
server_ip = "127.0.0.1"  # 替换为实际服务器地址
server_port = 19888

try:
    # 创建 TCP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    client_socket.connect((server_ip, server_port))
    print(f"成功连接到服务器 {server_ip}:{server_port}")

    # 持续与服务器交互
    while True:
        # 发送数据到服务器
        message = input("输入要发送的消息 (输入 'exit' 退出): ")
        if message.lower() == 'exit':
            print("已退出连接。")
            break

        client_socket.sendall(message.encode("utf-8"))
        print(f"已发送数据: {message}")

        # 接收服务器响应
        response = client_socket.recv(1024).decode("utf-8")
        print(f"服务器响应: {response}")

except ConnectionError as e:
    print(f"连接失败: {e}")
finally:
    client_socket.close()
    print("已关闭连接")

"""
服务器响应: {yd628565|729480|1|2010269|359860|300|0.3|0.2|2|#400#0.3#0.2#5#0,#400#0.3#0.2#5#0,#400#0.3#0.2#5#0,#400#0.3#0.2#5#0,#400#0.3#0.2#5#0,}
"""