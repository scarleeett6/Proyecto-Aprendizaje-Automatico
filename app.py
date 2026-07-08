from flask import Flask, render_template, jsonify
import json
import pandas as pd

app = Flask(__name__)

with open('data/parroquias.geojson', encoding='utf-8') as f:
    geojson_parroquias = json.load(f)

predicciones = pd.read_csv('data/predicciones.csv', dtype={'DPA_PARROQ': str})
predicciones['DPA_PARROQ'] = predicciones['DPA_PARROQ'].str.strip()

pred_dict = predicciones.set_index('DPA_PARROQ').to_dict(orient='index')

for feature in geojson_parroquias['features']:
    codigo = str(feature['properties'].get('DPA_PARROQ', '')).strip()
    feature['properties']['name'] = feature['properties'].get('DPA_DESPAR', codigo)

    if codigo in pred_dict:
        fila = pred_dict[codigo]
        feature['properties']['categoria_riesgo'] = fila.get('riesgo_predicho', 'sin_dato')
        feature['properties']['score_riesgo'] = fila.get('probabilidad')
        feature['properties']['canton'] = fila.get('canton', '')
        feature['properties']['provincia'] = fila.get('provincia', '')
    else:
        feature['properties']['categoria_riesgo'] = 'sin_dato'
        feature['properties']['score_riesgo'] = None
        feature['properties']['canton'] = feature['properties'].get('DPA_DESCAN', '')
        feature['properties']['provincia'] = feature['properties'].get('DPA_DESPRO', '')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/mapa')
def api_mapa():
    return jsonify(geojson_parroquias)


if __name__ == '__main__':
    app.run(debug=False)