# Riesgo de Inundación por Parroquia - Los Ríos y Guayas

Aplicación web que visualiza en un mapa interactivo el nivel de riesgo de inundación (bajo / medio / alto) de las parroquias de las provincias de Los Ríos y Guayas, Ecuador, a partir de un modelo de clasificación supervisada entrenado con variables climáticas, topográficas y socio-territoriales.

## Estructura del proyecto

```
Proyecto-Aprendizaje-Automatico/
├── data/
│   ├── parroquias.geojson     # Polígonos geográficos de las parroquias
│   └── predicciones.csv        # Predicciones del modelo final (ensamble)
├── templates/
│   └── index.html              # Frontend con mapa interactivo (ECharts)
├── app.py                      # Backend Flask
├── requirements.txt            # Dependencias de Python
└── README.md
```

## Tecnologías utilizadas

- **Backend:** Python 3 + Flask
- **Visualización geográfica:** Apache ECharts (mapa interactivo)
- **Modelo de Machine Learning:** Regresión Logística, Árbol de Decisión, SVM y Random Forest combinados en un ensamble de votación suave (entrenado en `notebook.ipynb`, no incluido en este repositorio de despliegue)

## Cómo ejecutar el proyecto en local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/scarleeett6/Proyecto-Aprendizaje-Automatico.git
   cd Proyecto-Aprendizaje-Automatico
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

4. Abrir el navegador en:
   ```
   http://127.0.0.1:5000
   ```

## Funcionalidades del mapa

- **Hover** sobre una parroquia: muestra nombre, cantón y provincia.
- **Clic** sobre una parroquia: muestra la categoría de riesgo y el score/probabilidad del modelo.
- **Colores por nivel de riesgo:** verde (bajo), naranja (medio), rojo (alto).
- **Leyenda** con la simbología de colores.

## Despliegue en producción

La aplicación está desplegada en PythonAnywhere y accesible públicamente en:

```
[URL pública aquí una vez desplegada]
```

### Pasos generales de despliegue (PythonAnywhere)

1. Crear una cuenta gratuita en [pythonanywhere.com](https://www.pythonanywhere.com).
2. Abrir una consola Bash y clonar este repositorio:
   ```bash
   git clone https://github.com/scarleeett6/Proyecto-Aprendizaje-Automatico.git
   ```
3. Instalar las dependencias dentro del entorno virtual de PythonAnywhere:
   ```bash
   pip install --user -r requirements.txt
   ```
4. Crear una nueva Web App (Flask) desde el panel de PythonAnywhere, apuntando el archivo WSGI al `app.py` de este repositorio.
5. Recargar (Reload) la aplicación y acceder a la URL pública generada.

## Origen de los datos

- **INAMHI:** registros históricos de precipitación mensual por estación (1960-2019).
- **División político-administrativa (DPA):** shapefile de parroquias del Ecuador.
- **Shapefile de cuencas hidrográficas:** distancia a cuerpos de agua.
- **SRTM:** altitud y pendiente aproximada del terreno (variables derivadas).

## Autora

Scarlett - Proyecto del Segundo Parcial, Aprendizaje Automático.
