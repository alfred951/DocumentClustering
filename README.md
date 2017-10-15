# DocumentClustering

Por: José Luis Álvarez Herrera y Luis Alfredo Gallego Montoya

# 1. Descripción de la Aplicación

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
en dirección el uno del otro.
