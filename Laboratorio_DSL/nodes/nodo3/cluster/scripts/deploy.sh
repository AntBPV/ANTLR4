#!/bin/bash

# Ruta real del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

APP_DIR="$SCRIPT_DIR/../app"

echo "========== DEPLOY =========="
echo "Nodo: $(hostname)"
echo "Iniciando despliegue..."

# Validación / creación
if [ ! -d "$APP_DIR" ]; then
    echo "[INFO] Creando directorio de aplicación..."
    mkdir -p "$APP_DIR"
fi

echo "[1/2] Descargando artefactos..."
sleep 1

# Simulación descarga
touch "$APP_DIR/app_v1.0.jar"

if [ $? -ne 0 ]; then
    echo "[ERROR] Falló la descarga"
    exit 1
fi

echo "[2/2] Desplegando aplicación..."
sleep 1

echo "Aplicación desplegada en $APP_DIR"
echo "Deploy finalizado exitosamente ✔"
echo "==============================="