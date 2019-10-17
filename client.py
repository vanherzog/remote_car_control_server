from socketIO_client import SocketIO, LoggingNamespace
import time
socket = SocketIO('http://192.168.1.16',5000,LoggingNamespace)
socket.emit('Ping')