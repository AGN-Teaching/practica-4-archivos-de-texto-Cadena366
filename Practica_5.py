# PASO 1: Cargar palabras correctas (solo hazlo una vez)
# Crea conjunto vacío para almacenar palabras correctas
palabras_buenas = set()  
# Abre archivo diccionario
with open('palabras.txt') as f:  
  # Lee línea por línea
    for linea in f:  
      # Añade palabra normalizada (minúsculas, sin espacios)
        palabras_buenas.add(linea.strip().lower())  

# PASO 2: Pedir archivo a revisar
archivo = input("Dime qué archivo quieres revisar: ")  

# PASO 3: Buscar errores
try:
    # Leer y limpiar el texto
  # Lee archivo y convierte a minúsculas
    texto = open(archivo).read().lower()  
  # Para cada signo de puntuación
    for signo in '.,;:¿?¡!()"\'':  
       # Reemplaza por espacio
        texto = texto.replace(signo, ' ')  
    
    # Encontrar palabras mal escritas
    errores = set()  # Conjunto para errores (evita duplicados)
   # Divide texto en palabras
    for palabra in texto.split():  
      # Si palabra no está en diccionario
        if palabra and palabra not in palabras_buenas:  
            errores.add(palabra)  
    
    # Mostrar resultados
    if errores:
        print("\n Posibles errores:")
      # Ordena errores alfabéticamente
        for error in sorted(errores):  
            print(f"- {error}")
    else:
        print("\n No hay errores")

except:
    print("\n No pude leer el archivo") 
