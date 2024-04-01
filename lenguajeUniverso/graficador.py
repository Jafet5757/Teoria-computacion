import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def show():
  # Leemos el archivo combinations.csv
  df = pd.read_csv('combinations.csv')

  # Calculamos la cantidad de . que hay en cada combinación
  df['dots'] = df['combination'].apply(lambda x: x.count('.'))

  # aplicamos logaritmo base 10 a la cantidad de . que hay en cada combinación
  df['log_dots'] = df['dots'].apply(lambda x: 0 if x == 0 else math.log10(x))


  # Obtenemos el total de los datos
  total = np.linspace(1, len(df), len(df))

  # Graficamos los resultados
  plt.subplot(1, 2, 1)
  plt.scatter(total, df['dots'])
  plt.title('Cantidad de .')
  plt.xlabel('Combinación')
  plt.ylabel('Cantidad de .')

  # Graficamos los resultados en log10
  plt.subplot(1, 2, 2)
  plt.scatter(total, df['log_dots'], color='purple')
  plt.title('Log10 de la cantidad de .')
  plt.xlabel('Combinación')
  plt.ylabel('Log10 de la cantidad de .')
  plt.show()

if __name__ == '__main__':
  show()