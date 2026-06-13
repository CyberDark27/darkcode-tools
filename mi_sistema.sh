#!/bin/bash
echo "╔══════════════════════════╗"
echo "║   DARKCODE SYSTEM INFO   ║"
echo "╚══════════════════════════╝"
echo ""
echo "👤 Usuario:  $USER"
echo "📅 Fecha:    $(date '+%d/%m/%Y %H:%M')"
echo "⏰ Uptime:   $(uptime -p)"
echo ""
echo "💾 RAM:"
free -h | grep Mem
echo ""
echo "💿 Disco:"
df -h / | tail -1
echo ""
echo "🌐 IP Local: $(hostname -I)"
echo ""
echo "🔥 Top 3 procesos:"
ps aux --sort=-%cpu | awk 'NR>1 && NR<=4 {print $1, $3"%", $11}'
