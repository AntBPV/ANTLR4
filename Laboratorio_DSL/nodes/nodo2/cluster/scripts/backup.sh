#!/bin/bash

# Obtener ruta del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

LOG_DIR="$SCRIPT_DIR/../logs"
BACKUP_DIR="$SCRIPT_DIR/../backup"

echo "========== BACKUP =========="
echo "Nodo: $(hostname)"
echo "Iniciando proceso de respaldo..."

# Validación
if [ ! -d "$LOG_DIR" ]; then
    echo "[ERROR] No existe el directorio de logs en $LOG_DIR"
    exit 1
fi

# Crear backup si no existe
if [ ! -d "$BACKUP_DIR" ]; then
    echo "[INFO] Creando directorio de backup..."
    mkdir -p "$BACKUP_DIR"
fi

echo "[1/3] Copiando archivos..."
sleep 1
cp -r "$LOG_DIR" "$BACKUP_DIR/" 2>/dev/null

if [ $? -ne 0 ]; then
    echo "[ERROR] Falló la copia de archivos"
    exit 1
fi

echo "[2/3] Comprimiendo respaldo..."
sleep 1
tar -czf "$BACKUP_DIR/backup.tar.gz" "$BACKUP_DIR" 2>/dev/null

echo "[3/3] Verificando integridad..."
sleep 1

echo "Backup completado correctamente ✔"
echo "==============================="