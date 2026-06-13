#!/bin/bash
echo "╔══════════════════════════╗"
echo "║    DARKCODE NET SCANNER  ║"
echo "╚══════════════════════════╝"
echo ""
echo "🌐 Tu IP: $(hostname -I | awk '{print $1}')"
echo "📡 Escaneando red local..."
echo ""
for i in $(seq 1 254); do
    ip="192.168.1.$i"
    ping -c 1 -W 1 $ip &>/dev/null && echo "✅ Dispositivo encontrado: $ip"
done
echo ""
echo "✔ Escaneo completado"
