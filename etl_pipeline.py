import os
import requests
import pandas as pd
from datetime import datetime

# 1. Extracción de datos
def extract_data():
    url = "https://mindicador.cl/api"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"Error al consultar la API: {response.status_code}")

# 2. Transformación con Pandas
def transform_data(raw_data):
    indicators = ['uf', 'dolar', 'euro', 'utm']
    transformed_list = []
    
    for key in indicators:
        if key in raw_data:
            item = raw_data[key]
            transformed_list.append({
                'codigo': item['codigo'],
                'nombre': item['nombre'],
                'unidad_medida': item['unidad_medida'],
                'valor': item['valor'],
                'fecha_consulta': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
    df = pd.DataFrame(transformed_list)
    return df

# 3. Carga de Datos
def load_data(df):
    os.makedirs('data_lake', exist_ok=True)
    filename = f"data_lake/economic_indicators_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ ETL ejecutado con éxito. Archivo guardado en: {filename}")

if __name__ == "__main__":
    raw = extract_data()
    data = transform_data(raw)
    load_data(data)
