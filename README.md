<h1 align="center">Aprendizaje Automático</h1>

<h2 align="center">Proyecto Final</h2>

<h2 align="center">Clasificación del Riesgo de Inundación por Parroquia en Zonas Lluviosas del Ecuador</h2>

<p align="justify">
Este proyecto desarrolla un sistema de clasificación del riesgo de inundación por parroquia en zonas lluviosas del Ecuador, con enfoque en las provincias de Los Ríos y Guayas. El trabajo combina variables climáticas, geográficas y territoriales para construir un modelo de aprendizaje automático capaz de estimar el nivel de riesgo de inundación a escala parroquial.
</p>

<h2>Objetivo</h2>

<p align="justify">
Diseñar e implementar un modelo de clasificación supervisada que permita asignar a cada parroquia una categoría de riesgo de inundación, utilizando datos abiertos oficiales, procesos de limpieza y transformación de datos, análisis exploratorio, entrenamiento de modelos y evaluación comparativa.
</p>

<h2>Integrantes</h2>

<ul>
  <li>Caicho Shanney</li>
  <li>Cedeño Scarlett</li>
  <li>Moya Ivan</li>
  <li>Ordoñez Cosme</li>
  <li>Salavarria Alejandra</li>
</ul>

<h2>Contenido del proyecto</h2>

<p>El notebook desarrolla las siguientes etapas:</p>

<ul>
  <li>Importación de librerías</li>
  <li>Descarga y carga de datasets</li>
  <li>Lectura de información geoespacial de parroquias</li>
  <li>Carga de datos de precipitación</li>
  <li>Limpieza e imputación de valores faltantes</li>
  <li>Filtrado del área de estudio: Los Ríos y Guayas</li>
  <li>Asociación entre parroquias y estaciones meteorológicas cercanas</li>
  <li>Cálculo de variables derivadas</li>
  <li>Obtención de altitud y pendiente</li>
  <li>Cálculo de distancia a cuerpos de agua</li>
  <li>Análisis exploratorio de datos (EDA)</li>
  <li>Construcción del dataset final para modelado</li>
  <li>Entrenamiento y evaluación de modelos de clasificación</li>
  <li>Interpretación de resultados</li>
</ul>

<p><strong>Video demostrativo:</strong> <a href="https://www.youtube.com/watch?v=0CbeOIJNtWk">Ver video en YouTube</a></p>

<p><strong>Aplicación desplegada:</strong> <a href="https://scarleeett.pythonanywhere.com/">Abrir aplicación web</a></p>

<h2>Variables utilizadas</h2>

<p>Entre las variables del estudio se incluyen:</p>

<ul>
  <li>precipitación acumulada</li>
  <li>altitud</li>
  <li>pendiente aproximada</li>
  <li>distancia a cuerpos de agua</li>
  <li>variables geográficas por parroquia</li>
  <li>variables derivadas construidas a partir de información espacial y climática</li>
</ul>

<h2>Tecnologías utilizadas</h2>

<ul>
  <li>Python</li>
  <li>Google Colab</li>
  <li>pandas</li>
  <li>numpy</li>
  <li>geopandas</li>
  <li>matplotlib</li>
  <li>seaborn</li>
  <li>shapely</li>
  <li>scikit-learn</li>
  <li>gdown</li>
  <li>srtm.py</li>
</ul>

<h2>Estructura esperada de archivos</h2>

<ul>
  <li><code>AA_Proyecto_FinalPRUEBA3.ipynb</code> → notebook principal</li>
  <li><code>README.md</code> → descripción general del proyecto</li>
  <li><code>requirements.txt</code> → dependencias necesarias</li>
  <li><code>parroquias.geojson</code> → archivo geográfico generado para la aplicación</li>
  <li>carpeta de datos descargados desde Google Drive</li>
</ul>

<h2>Fuente de datos</h2>

<p align="justify">
Los datos utilizados provienen de fuentes abiertas y oficiales, integradas desde una carpeta de Google Drive que contiene información climática, geográfica y territorial relacionada con parroquias, estaciones meteorológicas y cuerpos de agua.
</p>

<h2>Cómo ejecutar el proyecto</h2>

<ol>
  <li>Abrir el notebook en Google Colab.</li>
  <li>Instalar las librerías requeridas si es necesario.</li>
  <li>Ejecutar las celdas en orden desde la primera hasta la última.</li>
  <li>Permitir la descarga de la carpeta de datos desde Google Drive.</li>
  <li>Verificar que los archivos geográficos y climáticos se carguen correctamente.</li>
  <li>Revisar el análisis exploratorio, las variables derivadas y el entrenamiento del modelo.</li>
</ol>

<h2>Requisitos</h2>

<p>Se recomienda instalar las siguientes librerías:</p>

<pre><code>pip install pandas numpy matplotlib seaborn scikit-learn geopandas shapely gdown srtm.py</code></pre>

<h2>Resultados esperados</h2>

<p>El proyecto permite:</p>

<ul>
  <li>identificar patrones espaciales y climáticos asociados al riesgo de inundación</li>
  <li>generar variables derivadas relevantes para el análisis territorial</li>
  <li>entrenar modelos de clasificación supervisada</li>
  <li>comparar el desempeño de distintos enfoques de modelado</li>
  <li>apoyar la interpretación local del riesgo por parroquia</li>
</ul>

<h2>Aplicación académica</h2>

<p align="justify">
Este proyecto fue desarrollado como parte de la asignatura de Aprendizaje Automático, con el propósito de aplicar técnicas de clasificación en un problema real del contexto ecuatoriano, integrando ciencia de datos, análisis espacial y modelado predictivo.
</p>

<h2>Observaciones</h2>

<ul>
  <li>El proyecto requiere conexión a internet para descargar la carpeta de datos desde Google Drive.</li>
  <li>Algunas variables geográficas y de elevación se calculan dentro del notebook.</li>
  <li>La ejecución completa puede tardar varios minutos por el procesamiento espacial y la obtención de altitudes.</li>
</ul>

<h2>Autoría</h2>

<p>Trabajo académico grupal.</p>
