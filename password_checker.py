import re
import hashlib
import urllib.request

def check_password(password):
    print(f"\n🔐 DARKCODE PASSWORD ANALYZER")
    print(f"🎯 Analizando: {'*' * len(password)}\n")
    
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
        print("✅ Longitud suficiente (+2)")
    else:
        tips.append("❌ Usa mínimo 12 caracteres")

    if re.search(r'[A-Z]', password):
        score += 1
        print("✅ Tiene mayúsculas (+1)")
    else:
        tips.append("❌ Agrega letras mayúsculas")

    if re.search(r'[a-z]', password):
        score += 1
        print("✅ Tiene minúsculas (+1)")
    else:
        tips.append("❌ Agrega letras minúsculas")

    if re.search(r'[0-9]', password):
        score += 1
        print("✅ Tiene números (+1)")
    else:
        tips.append("❌ Agrega números")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        print("✅ Tiene símbolos especiales (+2)")
    else:
        tips.append("❌ Agrega símbolos como !@#$%")

    print(f"\n📊 PUNTAJE: {score}/7")
    
    if score >= 6:
        print("🟢 CONTRASEÑA FUERTE")
    elif score >= 4:
        print("🟡 CONTRASEÑA MEDIA")
    else:
        print("🔴 CONTRASEÑA DÉBIL")

    if tips:
        print("\n💡 SUGERENCIAS:")
        for tip in tips:
            print(tip)

password = input("\nEscribe una contraseña para analizar: ")
check_password(password)
