# DocumentClustering

Por: José Luis Álvarez Herrera y Luis Alfredo Gallego Montoya

# Descripción de la Aplicación

Este proyecto es una implementación en Python 2.7 de la técnica Clustering
de Machine Learning No Supervisado usando el algoritmo K-Means. Basado en
el paper "Similarity Measures for Text Document Clustering" de Anna Huang
para el Departamento de Ciencias de la Computación de la 
Universidad de Waikato, Hamilton, Nueva Zelanda. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.332.4480&rep=rep1&type=pdf

La aplicación fue realizada para la práctica #3 de la materia Tópicos Especiales
en Telemática de la Universidad EAFIT.

La aplicación esta divida en dos implementaciones, la serial y la paralela. 
Ambas leen el dataset de documentos de Gutenberg y cuentan palabras por documento,
generando un vector de téminos y frecuencias por documento. Luego se eliminan las
stopwords, palabras que no aportan nada a la semántica de los textos y que generarían
errores a la hora de calcular las funciones de similaridad entre documentos. Por último
para el procesado de documentos se utiliza una técnica de Stemming para unificar palabras
por prefijo que semánticamente nos dan un mismo contexto temático. 
(ej. Work, Works, Working, Worked; Todas significan lo mismo para nuestros fines prácticos).

Luego se procede a ejecutar el algoritmo K-Means con la función de similaridad del coseno,
basándonos en el ángulo entre dos vectores (Documentos) podemos saber que tan similares son
en dirección el uno del otro. Generando así K clusters con documentos similares semántica y 
sintácticamente comparando los elementos de los centroides entre si y los nuevos elementos con 
todos los centroides para determinar cúal es el cluster que más se adecua a cada documento.

# Implementación

El proyecto fue implementado usando Python 2.7 en Pycharm. Como librerías externas fueron usadas
mpi4py (http://mpi4py.scipy.org/docs/), stemming.porter2 (https://pypi.python.org/pypi/stemming/1.0)
y NumPy (http://www.numpy.org/), la estructura del proyecto tanto en serial como en paralelo cuenta
con los mismos archivos modulares que se encargan de completar cada uno de los pasos:
 
  `` \
     |- Cluster.py
     |- Comparator.py
     |- Document.py
     |- DocumentManager.py
     |- MainSerial.py o MainParallel.py
  ``
  
* Cluster.py contiene el algoritmo de Clustering con cada paso especificado como un método.
* Comparator.py contiene los algoritmos de similaridad (Jaccard Distance, Euclidean Distance y Cosine Distance)
* Document.py contiene una clase llamada Documento para la representación de los documentos como estructura de datos
* DocumentManager.py contiene la lógica de procesamiento de los documentos crudos y su representación en el programa
* Main.py valida los argumentos e inicializa el algoritmo

En el caso de la implementación paralela, tenemos un fichero extra para 
correrlo en modo de depuración, llamado: MainParallelDebugger.py que puede ser ejecutado e imprimirá
en pantalla todo un registro de los pasos.
