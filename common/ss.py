import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1088)
socket.socket = socks.socksocket