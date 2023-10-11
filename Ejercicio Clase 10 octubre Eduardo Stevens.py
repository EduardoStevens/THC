print("Ejercicio Clase 5")
"""
thisdict={
    "name": 'Hamal', 
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thisdict)

thisdict2={
    "name": 'Hamal', 
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

diccionario = {'python': 2.7, 'zope': 2.13, 'plone': 5.7}

l=[]
for i in diccionario.keys():
    l.append(diccionario[i])

print(l)

import pandas as pd

# Crear un diccionario con datos
datos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Luisa'],
    'Edad': [25, 28, 22, 30],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

# Crear un DataFrame a partir del diccionario
dataframe = pd.DataFrame(datos)

# Mostrar el DataFrame
print(dataframe)

frutas=("naranja","uva","manzana","limon")

for fruta in frutas:
    print(fruta)

if 'limon' in frutas:
    print("El limón está en la tupla")

def mi_funcion_1(fname,lname):
    print("Saludos " + fname + ", " + lname + " te saludo desde la función")

mi_funcion_1("Eduardo Stevens","CC")

def mi_funcion_2(*kids):
    print("El niño menor es " + kids[2])

mi_funcion_2("Emil", "Tobias", "Linus", "Alan")

def mi_funcion(**chamaco):
    print("El apellido es " +chamaco["Ape"])

mi_funcion(nombre="Aquiles", Ape="Vapython")
"""
def sum_vec(a,b):
    n=len(a)
    c=n*[0.0]
    if len(a)==len(b):
        for i in range(n):
            c[i]=a[i]+b[i]    
    print(c)

def prod_punto(a,b):
    n=len(a)
    if len(a)==len(b):
        for i in range(n):
            c=+a[i]*b[i]
    print(c)

""""
def sum_matrix(a,b):
    r=len(a)
    c=len(a[0])
    if len(a[0])==len(b[0]) and len(a)==len(b):
        for i in range(n):
            for j in range():  
                d[i][j]=a[i][j]+b[i][j]
    print(d)
"""

a=[10,20,30,40,50]
b=[20,30,40,50,60]    

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[20,30,40]

sum_vec(a,b)
prod_punto(a,b)