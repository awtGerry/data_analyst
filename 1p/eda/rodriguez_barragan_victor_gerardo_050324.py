# Analisis exploratorio de datos (EDA)

# dispersion, moda y simetria.
# usar graficos de dispersion

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = [ 279, 244, 318, 262, 335, 321, 165, 180, 201, 252, 145, 192, 217, 179, 182, 210, 271, 302, 169, 192, 156, 181, 156, 125, 166, 248, 198, 220, 134, 189 ]

# Graficar
sns.displot(df, kde=True)
plt.show()

# Calcular la media
mean = np.mean(df)
median = np.median(df)
mode = pd.DataFrame(df).mode()
skew = pd.DataFrame(df).skew()
print('Media:', mean)
print('Mediana:', median)

# Ordenar datos de menor a mayor valor
df = np.sort(df)

# Calcular la q1 y q3
q1 = np.percentile(df, 25)
q3 = np.percentile(df, 75)

# Calcular el rango intercuartilico
iqr = q3 - q1

# Calcular los limites
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Grafico de dispersion
# visualizar la información en forma de dispersión para ver cómo se comportan los datos.
plt.scatter(range(len(df)), df)
plt.axhline(y=mean, color='r', linestyle='-')
plt.axhline(y=median, color='g', linestyle='-')
plt.axhline(y=mode[0][0], color='b', linestyle='-')
plt.axhline(y=lower_bound, color='r', linestyle='--')
plt.axhline(y=upper_bound, color='r', linestyle='--')
plt.show()

# Boxplot con l1, l2, q1, q3, media
plt.boxplot(df)
plt.axhline(y=lower_bound, color='r', linestyle='--')
plt.axhline(y=upper_bound, color='r', linestyle='--')
plt.show()

# Conclusiones
# Los datos se encuentran en un rango de 125 a 335 con una media de 213, mediana de 192 y moda de 156
# Los datos estan sesgados a la derecha con un valor de 0.7 y se encuentran dispersos
# Se observa un dato atipico en el limite superior del boxplot (335)
# El 50% de los datos se encuentran entre 169 y 271
# El 25% de los datos se encuentran por debajo de 169
# El rango intercuartilico es de 102
# Los limites inferior es 16 y el superior son 424
