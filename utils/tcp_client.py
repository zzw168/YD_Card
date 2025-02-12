import socket
import time


class TCPClient:
    def __init__(self, host: str, port: int, reconnect_interval: int = 5):
        self.host = host
        self.port = port
        self.reconnect_interval = reconnect_interval
        self.sock = None

    def connect(self):
        """建立连接"""
        if self.sock:
            self.sock.close()  # 关闭旧连接

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(f"尝试连接到 {self.host}:{self.port} ...")
            self.sock.connect((self.host, self.port))
            print("✅ 连接成功")
        except (socket.error, ConnectionRefusedError) as e:
            print(f"❌ 连接失败: {e}, {self.reconnect_interval} 秒后重试...")
            self.sock = None
            time.sleep(self.reconnect_interval)
            self.connect()  # 递归重连

    def send_data(self, data: str):
        """发送数据"""
        if self.sock is None:
            print("⚠️ 连接未建立，尝试重连...")
            self.reconnect()

        try:
            self.sock.sendall(data.encode("gbk"))  # 发送数据
            print("✅ 数据发送成功")
        except (socket.error, BrokenPipeError) as e:
            print(f"❌ 发送失败: {e}, 尝试重连...")
            self.reconnect()

    def receive_data(self):
        """接收数据"""
        if self.sock is None:
            return None

        try:
            data = self.sock.recv(1024)
            return data.decode("gbk", errors="ignore")
        except (socket.error, ConnectionResetError) as e:
            print(f"❌ 接收失败: {e}, 重新连接...")
            self.reconnect()
            return None

    def reconnect(self):
        """断线重连"""
        print("🔄 重新连接中...")
        self.close()
        self.connect()

    def close(self):
        """关闭连接"""
        if self.sock:
            self.sock.close()
            self.sock = None
            print("🔴 连接已关闭")


if __name__ == "__main__":
    client = TCPClient("127.0.0.1", 12345)
    client.connect()

    try:
        while True:
            msg = input("输入要发送的消息: ")
            client.send_data(msg)
            response = client.receive_data()
            if response:
                print("服务器响应:", response)
    except KeyboardInterrupt:
        print("❌ 客户端退出")
        client.close()
