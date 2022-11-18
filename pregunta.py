"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

import re

def ingest_data():
  with open('clusters_report.txt') as text:
    lines = text.readlines()
  lines = lines[4:]

  groups = []

  
  group = [0, 0, 0, '']

  for row in lines:

    if re.match('^ +[0-9]+ +', row):
      numero, valor, porcentaje, *txt = row.split()
      group[0] = int(numero)
      group[1] = int(valor)
      group[2] = float(porcentaje.replace(',','.'))
      txt.pop(0) 
      txt = ' '.join(txt)
      group[3] += txt

    elif re.match('^\n', row) or re.match('^ +$', row):
      group[3] = group[3].replace('.', '') 
      groups.append(group)
      group = [0, 0, 0, '']

    elif re.match('^ +[a-z]', row):
      txt = row.split()
      txt = ' '.join(txt)
      group[3] += ' ' + txt
  df = pd.DataFrame (groups, columns = ['clusters', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

  return df