import pickle
from pathlib import Path

print('>> [API TEAM] Levantando servicio...')

# 1. ACCESO DIRECTO (High Coupling)
# Buscamos el archivo usando una ruta relativa ("sube una carpeta, entra a ml...")
ruta_modelo = Path(__file__).parent.parent / 'ml' / 'models' / 'churn_model.pkl'

if ruta_modelo.exists():
    with open(ruta_modelo, 'rb') as f:
        modelo = pickle.load(f)
    print(f"   ✅ ÉXITO: Modelo {modelo['version']} cargado desde disco local.")
    print(f"   - Datos internos: {modelo['pesos']}")
else:
    print(f"   ❌ ERROR: No encuentro el modelo. ¿El equipo de ML ya corrió el script?")