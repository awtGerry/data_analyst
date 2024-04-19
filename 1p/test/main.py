# Victor Gerardo Rodriguez Barragan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cargar datos
df = pd.read_csv('calif_ingreso.csv')

# agregar titulo genero
df.rename(columns={'Unnamed: 1': 'Genero'}, inplace=True)
print(df.head())

# analisis
print(df.info())

# --[ 1 ]--
print(df.describe())
# Grafica de dispersión
plt.scatter(df["geodif"], df["ancompl"])
plt.scatter(df["alg"], df["anreal"])
plt.show()
# Boxplot
sns.boxplot(data=df)
plt.show()

# en las variables geodif, ancompl y alg. En estas variables se observa que hay
# valores atípicos que se alejan del resto de los datos.

# En el análisis descriptivo se observa que la media de las calificaciones es
# similar en todas las variables, sin embargo, la desviación estándar es
# considerablemente alta, lo que indica que hay una gran variabilidad en las
# calificaciones. Esto se puede observar en los boxplots, donde se observa que
# hay valores atípicos que se alejan del resto de los datos.

# --[ 2 ]--
# Estadística
print(df.corr())
print(df[["geodif", "ancompl"]].corr())
print(df[["alg", "anreal"]].corr())

# matriz de correlación
sns.heatmap(df.corr(), annot=True)
plt.show()

# Se observa que todas las variables tienen una correlación relativamente alta entre ellas,
# lo que indica que las calificaciones en estas
# variables están relacionadas entre sí. Los dos pares de variables con mayor
# correlación son: geodif y ancompl, y alg y anreal.

sns.regplot(x="geodif", y="ancompl", data=df)
sns.regplot(x="alg", y="anreal", data=df)
plt.show()

# En ambas se observa una relación lineal entre las variables.

# --[ 3 ]--
# Agrupar los datos
# Estandarizar los datos
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[["geodif", "ancompl", "alg", "anreal", "estad"]])
# Agrupar por similitud
kmeans = KMeans(n_clusters=3, random_state=1234)
kmeans.fit(df_scaled)
# Asignar cluster a cada registro
df["cluster"] = kmeans.labels_
print(df)
# graficar
sns.pairplot(df, hue="cluster")
plt.show()
# Calcular correlación
print(df.corr())

# Hay similitud entre los candidatos, por lo que se pueden formar grupos de
# preparación. Tres ejemplos de agrupaciones son:
# Grupo 1
print(df[df["cluster"] == 0])
# Grupo 2
print(df[df["cluster"] == 1])
# Grupo 3
print(df[df["cluster"] == 2])

# los candidatos se agrupan en tres grupos, donde cada grupo
# tiene similitud en las calificaciones de las cinco variables.
