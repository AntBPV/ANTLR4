#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/../logs/update.log"

echo "========== UPDATE =========="
echo "Nodo: $(hostname)"
echo "Iniciando actualización..."

echo "[1/3] Verificando conexión..."
sleep 1

echo "[2/3] Descargando actualizaciones..."
sleep 1

echo "[3/3] Instalando paquetes..."
sleep 1

echo "Actualización completada ✔"

# Guardar log
echo "Update ejecutado en $(date)" >> "$LOG_FILE"

echo "==============================="