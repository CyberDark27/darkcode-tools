import base64
import hashlib
from cryptography.fernet import Fernet

def generar_clave(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encriptar(mensaje, password):
    clave = generar_clave(password)
    f = Fernet(clave)
    return f.encrypt(mensaje.encode()).decode()

def desencriptar(mensaje_enc, password):
    try:
        clave = generar_clave(password)
        f = Fernet(clave)
        return f.decrypt(mensaje_enc.encode()).decode()
    except:
        return "❌ Contraseña incorrecta"

print("╔══════════════════════════╗")
print("║  DARKCODE ENCRYPTOR 🔐   ║")
print("╚══════════════════════════╝")
print("\n1. Encriptar\n2. Desencriptar")
opcion = input("\nElige opción: ")
mensaje = input("Mensaje: ")
password = input("Contraseña: ")

if opcion == "1":
    resultado = encriptar(mensaje, password)
    print(f"\n✅ Encriptado:\n{resultado}")
else:
    resultado = desencriptar(mensaje, password)
    print(f"\n✅ Desencriptado:\n{resultado}")
