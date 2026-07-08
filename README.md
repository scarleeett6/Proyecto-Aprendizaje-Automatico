**Aprendizaje Automático**

Proyecto Final

Clasificación del Riesgo de Inundación por Parroquia en Zonas Lluviosas del Ecuador
Este proyecto desarrolla un sistema de clasificación del riesgo de inundación por parroquia en zonas lluviosas del Ecuador, con enfoque en las provincias de Los Ríos y Guayas. El trabajo combina variables climáticas, geográficas y territoriales para construir un modelo de aprendizaje automático capaz de estimar el nivel de riesgo de inundación a escala parroquial.

**Objetivo**

Diseñar e implementar un modelo de clasificación supervisada que permita asignar a cada parroquia una categoría de riesgo de inundación, utilizando datos abiertos oficiales, procesos de limpieza y transformación de datos, análisis exploratorio, entrenamiento de modelos y evaluación comparativa.

**Integrantes**
	•	Caicho Shanney
	•	Cedeño Scarlett
	•	Moya Ivan
	•	Ordoñez Cosme
	•	Salavarria Alejandra
   
**Contenido del proyecto**
El notebook desarrolla las siguientes etapas:
	•	Importación de librerías
	•	Descarga y carga de datasets
	•	Lectura de información geoespacial de parroquias
	•	Carga de datos de precipitación
	•	Limpieza e imputación de valores faltantes
	•	Filtrado del área de estudio: Los Ríos y Guayas
	•	Asociación entre parroquias y estaciones meteorológicas cercanas
	•	Cálculo de variables derivadas
	•	Obtención de altitud y pendiente
	•	Cálculo de distancia a cuerpos de agua
	•	Análisis exploratorio de datos (EDA)
	•	Construcción del dataset final para modelado
	•	Entrenamiento y evaluación de modelos de clasificación
	•	Interpretación de resultados
	•	Enlace de video: https://www.youtube.com/watch?v=0CbeOIJNtWk
   
**Variables utilizadas**
Entre las variables del estudio se incluyen:
	•	precipitación acumulada
	•	altitud
	•	pendiente aproximada
	•	distancia a cuerpos de agua
	•	variables geográficas por parroquia
	•	variables derivadas construidas a partir de información espacial y climática
   
**Tecnologías utilizadas**
	•	Python
	•	Google Colab
	•	pandas
	•	numpy
	•	geopandas
	•	matplotlib
	•	seaborn
	•	shapely
	•	scikit-learn
	•	gdown
	•	srtm.py
   
**Estructura esperada de archivos**
	•	AA_Proyecto_FinalPRUEBA3.ipynb → notebook principal
	•	README.md → descripción general del proyecto
	•	requirements.txt → dependencias necesarias
	•	parroquias.geojson → archivo geográfico generado para la aplicación
	•	carpeta de datos descargados desde Google Drive
   
**Fuente de datos**
Los datos utilizados provienen de fuentes abiertas y oficiales, integradas desde una carpeta de Google Drive que contiene información climática, geográfica y territorial relacionada con parroquias, estaciones meteorológicas y cuerpos de agua.

**Cómo ejecutar el proyecto**
	1	Abrir el notebook en Google Colab.
	2	Instalar las librerías requeridas si es necesario.
	3	Ejecutar las celdas en orden desde la primera hasta la última.
	4	Permitir la descarga de la carpeta de datos desde Google Drive.
	5	Verificar que los archivos geográficos y climáticos se carguen correctamente.
	6	Revisar el análisis exploratorio, las variables derivadas y el entrenamiento del modelo.
   
**Requisitos**
Se recomienda instalar las siguientes librerías:
pip install pandas numpy matplotlib seaborn scikit-learn geopandas shapely gdown srtm.py

**Resultados esperados**
El proyecto permite:
	•	identificar patrones espaciales y climáticos asociados al riesgo de inundación
	•	generar variables derivadas relevantes para el análisis territorial
	•	entrenar modelos de clasificación supervisada
	•	comparar el desempeño de distintos enfoques de modelado
	•	apoyar la interpretación local del riesgo por parroquia

**Aplicación académica**
Este proyecto fue desarrollado como parte de la asignatura de Aprendizaje Automático, con el propósito de aplicar técnicas de clasificación en un problema real del contexto ecuatoriano, integrando ciencia de datos, análisis espacial y modelado predictivo.

**Observaciones**
	•	El proyecto requiere conexión a internet para descargar la carpeta de datos desde Google Drive.
	•	Algunas variables geográficas y de elevación se calculan dentro del notebook.
	•	La ejecución completa puede tardar varios minutos por el procesamiento espacial y la obtención de altitudes.

**Autoría**
Trabajo académico grupal
