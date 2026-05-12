# Script de prueba para verificar la carga desde Google Drive
# Ejecutar con: python test_google_drive.py

import pandas as pd
import sys

print("=" * 60)
print("🧪 TEST: Carga de datos desde Google Drive")
print("=" * 60)
print()

# IDs de los archivos en Google Drive
files = {
    "Facturito": "1fforhn03rynmhUva0SaN1SawnxmEm5dV",
    "Perseo WEB": "1wt2unhyUsXhKjQnjEXoB36tlP2eA5Jst",
    "Perseo PC": "168V0BCy0-LZDzeKQp-9sdJuXIbRQvOpd"
}

all_passed = True

for name, file_id in files.items():
    print(f"📊 Probando: {name}")
    print(f"   File ID: {file_id}")
    
    try:
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        df = pd.read_excel(url)
        
        print(f"   ✅ ÉXITO - Cargado correctamente")
        print(f"   📈 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
        print(f"   📋 Columnas: {list(df.columns[:5])}...")
        print()
        
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        print()
        all_passed = False

print("=" * 60)
if all_passed:
    print("✅ TODAS LAS PRUEBAS PASARON")
    print("Los dashboards están listos para desplegarse en Streamlit Cloud")
    sys.exit(0)
else:
    print("❌ ALGUNAS PRUEBAS FALLARON")
    print()
    print("Posibles causas:")
    print("1. Los archivos no tienen permisos públicos en Google Drive")
    print("2. Los enlaces no son correctos")
    print("3. Problemas de conexión a internet")
    print()
    print("Solución:")
    print("1. Verifica que cada archivo tenga permisos de 'Cualquier persona con el enlace'")
    print("2. El rol debe ser 'Lector' (no Editor)")
    sys.exit(1)

print("=" * 60)
