from data_stark import lista_personajes
from funciones import *


lista_superheroes = []
flag_lista = False


while True:
    match menu_stark00():
        case "0":
            cargar_lista(lista_superheroes, lista_personajes)
            flag_lista = True
        case "1": 
            if se_cargo(flag_lista):
                mostar_nombres(lista_superheroes)
        case "2":
            if se_cargo(flag_lista):
                mostar_nombre_altura(lista_superheroes)
        case "3":
            if se_cargo(flag_lista):
                mayor_altura(lista_superheroes)
        case "4":
            if se_cargo(flag_lista):
                menor_altura(lista_superheroes)
        case "5":
            if se_cargo(flag_lista):
                promedio_altura(lista_superheroes)
        case "6":
            if se_cargo(flag_lista):
                mas_pesado(lista_superheroes)
                menos_pesado(lista_superheroes)
        case "7":
            if confirmar("Esta seguro que quiere entrar a STARK 01? s/n: "):
                while True:
                    match menu_stark01():
                        case "1":
                            cargar_lista(lista_superheroes, lista_personajes)
                            flag_lista = True
                        case "2":
                            if se_cargo(flag_lista):
                                mostrar_nombres_por_genero(lista_superheroes, "genero", "M", "nombre")
                        case "3":
                            if se_cargo(flag_lista):
                                mostrar_nombres_por_genero(lista_superheroes, "genero", "F", "nombre")
                        case "4":
                            if se_cargo(flag_lista):
                                mayor_altura_por_genero(lista_superheroes, "genero", "M")
                        case "5":
                            if se_cargo(flag_lista):
                                mayor_altura_por_genero(lista_superheroes, "genero", "F")
                        case "6":
                            if se_cargo(flag_lista):
                                promedio_altura_por_genero(lista_superheroes, "genero", "M")
                        case "7":
                            if se_cargo(flag_lista):
                                promedio_altura_por_genero(lista_superheroes, "genero", "F")
                        case "8":
                            if se_cargo(flag_lista):
                                determinar_cantidad_tipos(lista_superheroes, "color_ojos")
                        case "9":
                            if se_cargo(flag_lista):
                                determinar_cantidad_tipos(lista_superheroes, "color_pelo")
                        case "10":
                            if se_cargo(flag_lista):
                                determinar_cantidad_tipos(lista_superheroes, "inteligencia")
                        case "11":
                            if se_cargo(flag_lista):
                                listar_superheores_tipo(lista_superheroes, "color_ojos", "nombre")
                        case "12":
                            if se_cargo(flag_lista):
                                listar_superheores_tipo(lista_superheroes, "color_pelo", "nombre")
                        case "13":
                            if se_cargo(flag_lista):
                                listar_superheores_tipo(lista_superheroes, "inteligencia", "nombre")
                        case "s":
                            if confirmar("Esta seguro que desea salir? s/n: "):
                                break
        case "s":
            if confirmar("Esta seguro que desea salir? s/n: "):
                break
    pausar()