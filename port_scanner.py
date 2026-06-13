import socket
import sys

def scan(host, inicio, fin):
    print(f"\n🔍 DARKCODE PORT SCANNER")
    print(f"🎯 Target: {host}")
    print(f"📡 Puertos: {inicio}-{fin}\n")
    
    for port in range(inicio, fin + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"✅ Puerto {port} ABIERTO")
        sock.close()
    print("\n✔ Escaneo completado")

scan("192.168.1.1", 1, 100)
