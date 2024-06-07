def menu_stark00()-> str:
    """un menu diseñado para industrias stark
    
    Returns:
        str: la opcion elegida
    """
    limpiar_pantalla()
    print("--------------------------------------------------------------------------------------------------")
    print(f"{'Desafio STARK':^50s}")
    print("0- Cargar lista")
    print("1- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("2- Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("3- Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("4- Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("5- Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("6- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("7- Calcular e informar cual es el superhéroe más y menos pesado.")
    print("8- Ordenar el código implementando una función para cada uno de los valores informados.")
    print("9- Construir un menú que permita elegir qué dato obtener")
    print("s- salir")
    return input("ingrese opcion: ").lower().strip()

def confirmar(mensaje:str)-> bool:
    """confirma con un booleano

    Args:
        mensaje (str): pregunta que sera respondida por el usuario

    Returns:
        bool: True si la respuesta es si, False si es no
    """
    rta = input(mensaje).lower().strip()
    return rta == 's'


def pausar():
    """pausa el programa
    """
    import os
    os.system("pause")

def limpiar_pantalla():
    """limpia la pantalla
    """
    import os
    os.system("cls")

def cargar_lista(lista_destino:list, lista_origen:list):
    for item in lista_origen:
        lista_destino.append(item)
    print("Se cargo la lista con exito...")
    print("------------------------------------------------------------")

def se_cargo(flag: bool)->bool:
    """pregunta si se cargo la lista

    Args:
        flag (bool): bandera de la lista

    Returns:
        bool: retorna True, y si es False muestra por consola un mensaje
    """
    return True if flag else print("Primero cargue la lista...")


def mostar_nombres(lista: list)->None:
    """muesta por consola los nombres

    Args:
        lista (list): lista diccionario donde estan los nombres
    """
    for heroe in lista:
        print(heroe["nombre"])
        print("------------------------")

def mostar_nombre_altura(lista: list)->None:
    """muestra por consola los nombres con sus alturas

    Args:
        lista (list): lista diccionario donde estan los nombres y sus alturas
    """
    for heroe in lista:
        print(heroe["nombre"])
        print(f"{heroe['altura']:.6}")
        print("------------------------")

def mayor_altura(lista:list)->None:
    """muestra por consola el superheroe con mayor altura

    Args:
        lista (list): lista diccionario donde esta el superheroe mas alto
    """
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["altura"]) > max_altura:
            bandera = False
            max_altura = float(heroe["altura"])
            nombre_max_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == max_altura:
            print(heroe)
    
    print(f"El heroe mas alto es: {nombre_max_altura} {max_altura:5.2f}")
    print("------------------------------------------------------------")

def menor_altura(lista:list)->None:
    """muestra por consola el superheroe con menor altura

    Args:
        lista (list): lista diccionario donde esta el superheroe de menor altura
    """
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["altura"]) < men_altura:
            bandera = False
            men_altura = float(heroe["altura"])
            nombre_men_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == men_altura:
            print(heroe)
    
    print(f"El heroe mas bajo es: {nombre_men_altura} {men_altura:5.2f}")
    print("------------------------------------------------------------")

def promedio_altura(lista:list):
    """promedia la altura de todos los superheroes

    Args:
        lista (list): lista diccionario donde estan los superheroes
    """
    total_altura = 0
    cant_heroes = len(lista)

    for superheroe in lista:
        total_altura += float(superheroe["altura"])

    prom_altura = total_altura / cant_heroes

    print(f"La altura promedio de los superheroes es: {prom_altura:5.2f}")
    print("------------------------------------------------------------")

def menos_pesado(lista:list):
    """muestra por consola al menos pesado de una lista

    Args:
        lista (list): lista diccionario donde se encuentra el menos pesado
    """
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["peso"]) < menos_pesado:
            bandera = False
            menos_pesado = float(heroe["peso"])
            nombre_menos_pesado = heroe["nombre"]

    for heroe in lista:
        if heroe["peso"] == menos_pesado:
            print(heroe)
    
    print(f"El heroe menos pesado es: {nombre_menos_pesado} {menos_pesado:5.2f}")
    print("------------------------------------------------------------")

def mas_pesado(lista:list):
    """muestra por consola al mas pesado de una lista

    Args:
        lista (list): lista diccionario donde se encuentra el mas pesado
    """
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["peso"]) > mas_pesado:
            bandera = False
            mas_pesado = float(heroe["peso"])
            nombre_mas_pesado = heroe["nombre"]

    for heroe in lista:
        if heroe["peso"] == mas_pesado:
            print(heroe)
    
    print(f"El heroe mas pesado es: {nombre_mas_pesado} {mas_pesado:5.2f}")
    print("------------------------------------------------------------")

def menu_stark01()->str:
    """un menu diseñado para industrias stark

    Returns:
        _type_: la opcion elegida
    """
    print("      *** Menu de Opciones ***   ")
    print("------------------------------------------------------------")
    print("  1- cargar lista")
    print("  2- mostrar heroes masculinos")
    print("  3- mostrar heroes femeninos")
    print("  4- mostrar heroe masculino mas alto")
    print("  5- mostrar heroe femenino mas alto")
    print("  6- mostrar el promedio de altura del genero masculino")
    print("  7- mostrar el promedio de altura del genero femenino")
    print("  8- Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("  9- Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("  10- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("  11- Listar todos los superhéroes agrupados por color de ojos.")
    print("  12- Listar todos los superhéroes agrupados por color de pelo.")
    print("  13- Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("  s- salir")
    return input("Ingrese opcion: ").lower().strip()


def mostrar_nombres_por_genero(lista:list, key:str, key2:str, key3:str)-> None:
    """muestra por consola los nombres del genero elegido

    Args:
        lista (list): lista con los nombres
        key (str): campo donde esta el genero en la lista diccionario
        key2 (str): el genero elegido
        key3 (str): campo donde esten los nombres
    """
    for item in lista:
        if item[key] == key2:
            print("Nombre: {}".format(item[key3]))
            print("------------------------------------------------------------")

def mayor_altura_por_genero(lista:list, key:str, key2:str)->None:
    """muesta la mayor altura por genero

    Args:
        lista (list): lista con las alturas
        key (str): campo de los generos
        key2 (str): genero elegido
    """
    bandera = True
    for heroe in lista:
        if heroe[key] == key2:
            if bandera or float(heroe["altura"]) > mas_altura:
                bandera = False
                mas_altura = float(heroe["altura"])
                nombre_mas_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == mas_altura:
            print(heroe)
    
    print(f"El heroe mas alto es: {nombre_mas_altura} {mas_altura:5.2f}")
    print("------------------------------------------------------------")

def promedio_altura_por_genero(lista:list, key:str, key2:str)->None:
    """muestra el promedio de altura por genero

    Args:
        lista (list): lista con las alturas
        key (str): campo de los generos
        key2 (str): genero elegido
    """
    total_altura = 0
    cant_heroes = len(lista)
    for superheroe in lista:
        if superheroe[key] == key2:
            total_altura += float(superheroe["altura"])

    prom_altura = total_altura / cant_heroes

    print("La altura promedio de los superheroes es: {}".format(prom_altura))
    print("------------------------------------------------------------")

def determinar_cantidad_tipos(lista:list, key:str)-> None:
    """determina y muestra por pantalla la cantidad de elementos de un tipo

    Args:
        lista (list): la lista con los elementos
        key (str): el tipo de elemento que queremos determinar y mostrar
    """
    lista_aux = []
    for i in lista:
        if i[key] == "":
            lista_aux.append("No tiene")
        else:
            lista_aux.append(i[key])

    cuenta_tipos = {}
    for elemento in lista_aux:
        if elemento in cuenta_tipos:
            cuenta_tipos[elemento] += 1
        else:
            cuenta_tipos[elemento] = 1
    for tipo, cantidad in cuenta_tipos.items():
        print(f"Tipo {tipo}, Cantidad: {cantidad}")

def listar_superheores_tipo(list: list, key: str, key_nombre: str)->None:
    """lista los superheores por su tipo

    Args:
        list (list): lista donde esten los superheroes
        key (str): el tipo por el que vamos a listar a los superheroes
        key_nombre (str): el campo con los nombres de los superheores
    """
    lista_aux = []
    for i in list:
        if i[key] == "":
            lista_aux.append("No tiene")
        else:
            lista_aux.append(i[key])

    dict_aux = {}
    for i in range(len(lista_aux)):
        tipo = lista_aux[i]
        nombre = list[i][key_nombre]
        if tipo in dict_aux:
            dict_aux[tipo].append(nombre)
        else:
            dict_aux[tipo] = [nombre]
    
    for tipo, nombres in dict_aux.items():
        print(f"Tipo {tipo}: {', '.join(nombres)}")


