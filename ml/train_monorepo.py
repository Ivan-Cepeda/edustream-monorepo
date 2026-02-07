import sys
import os
import pickle
from pathlib import Path

# 1. TRUCO MONOREPO: Agregamos la carpeta raíz al sistema para ver 'core'
sys.path.append(str(Path(__file__).parent.parent))
from core.transform import normalize_data

print('>> [ML TEAM] Iniciando entrenamiento...')

# 2. Usamos la lógica compartida
datos_crudos = [150, 500, 900]
datos_limpios = [normalize_data(x) for x in datos_crudos]
print(f'   - Datos limpiados con Core: {datos_limpios}')

# 3. Guardamos el modelo (El Artefacto)
# Lo guardamos en una carpeta local, visible para todos
os.makedirs('ml/models', exist_ok=True)
modelo = {'version': 'v1.0', 'pesos': datos_limpios}

with open('ml/models/churn_model.pkl', 'wb') as f:
    pickle.dump(modelo, f)

print('   - Modelo guardado en: ml/models/churn_model.pkl')
