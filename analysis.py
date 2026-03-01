import pandas as pd

#Analizar de por que hay poca rentabilidad sabiendo que hay muchas ventas

df = pd.read_csv("retail_ventas_proyecto.csv")

#¿Que componentes esta afectando al margen de ganancia: descuento, costo?

df["Margen_%"] = df["Ventas"] / df["Ganancia"]

"""
df_mar_desc1 = df.groupby(pd.cut(df["Descuento"], bins=5))["Margen_%"].mean()
df_mar_desc2 = df[["Descuento", "Margen_%"]].corr()

df_mar_cost1 = df.groupby(pd.cut(df["CostoUnitario"],bins=5))["Margen_%"].mean()
df_mar_cost2 = df[["CostoUnitario", "Margen_%"]].corr()
"""


"""
print("Parte de Descuento:")
print("Primer Analisis")
print(df_mar_desc1)
print("_"*50)
print("Segundo Analisis")
print(df_mar_desc2)
print("")
print("")
print("Parte de Costo:")
print("Primer Analisis")
print(df_mar_cost1)
print("_"*50)
print("Segundo Analisis")
print(df_mar_cost2)
print("")
print("")
"""

#¿Que Region tiene menor Margen de Ganancia?
"""
df_mar_region = df.groupby("Region")["Margen_%"].mean()

print(df_mar_region)

Sur tiene el Peor Margen
"""
#¿Que Categoria de Producto tiene menor margen de Ganancia?
"""
df_mar_categoria = df.groupby("Categoria")["Margen_%"].mean()

print(df_mar_categoria)

Hogar tiene el Peor Margen de Ganancia
"""
#¿La Categoria 'Hogar' tiene peor margen por el descuento o costo?

"""
Entre el Descuento de Rango 12% y 18% genera un Margen de Ganancia -122% 
y Entre el CostoUnitario entre  354.38 y 528.52 genera un Margen de Ganancia -97%
"""

"""
df_hogar = df[df["Categoria"] == "Hogar"]

df_hogar_cat_ana1 = df_hogar[["Descuento", "CostoUnitario", "Margen_%"]].corr()

df_hogar_cat_ana2 = df_hogar.groupby(pd.cut(df["CostoUnitario"],bins=5))["Margen_%"].mean()

print(df_hogar_cat_ana2)
print("")
print(df_hogar_cat_ana1)
df_hogar_cat_ana2 = df_hogar.groupby(pd.cut(df["Descuento"],bins=5))["Margen_%"].count()
"""

#En La Region sur, ¿Que esta afectando al Margen, Costo, Categoria, Descuento?
"""
df_sur = df[df["Region"] == "Sur"]

df_ana_sur1 = df_sur.groupby(pd.cut(df["CostoUnitario"],bins=5))["Margen_%"].mean()
"""
"""
En el rango de Descuento entre 12% y 18% tienen un Margen de Ganancia -133%
y Entre el CostoUnitario entre  354.38 y 528.52 genera un Margen de Ganancia -120%
"""
#print(df_ana_sur1)

#Preparando la Tabla y Limpiando la Tabla

df.dropna()

df = df.drop(columns=["OrderID", "Fecha"])

df["Producto"] = df["Producto"].str.split()
df["Region"] = df["Region"].str.split()
df["Categoria"] = df["Categoria"].str.split()

print(df)

df.to_excel("rentabilidad_limpia.xlsx", index=False)
