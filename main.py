#!/usr/bin/python3

import os
from gestor_notas import GestorNotas
def main():

    while True:
        gestor = GestorNotas() 

        print(f"--------\n| MENU |\n--------\n ")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Bucar por una nota")
        print("4. Eliminar una nota")
        print("5. Salir\n")

        opcion= input("[+] Elige una opción: ")

        if opcion == "1":
            contenido = input("\n [+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas() 
            print("[+] Mostrando todas las notas almacenadas:\n ")
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "3":
            busqueda = input("[+] Ingresa la palabra  que quieres buscar: ")
            notas = gestor.buscar_nota(busqueda)

            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "4":
            num_nota = int(input("[+] Ingresa la nota que quieres eliminar: "))
            gestor.eliminar_nota(num_nota)

        elif opcion == "5":
            break
        else:
            print("La opción indicada es incorrecta")
        input(f"[+] Presion <Enter> para continuar")


if __name__ == '__main__':
    main()
