#!/usr/bin/python3

import pickle
from notas import Nota

class GestorNotas:
    ## metodos especiales

           
       
    def __init__(self, archivo_notas = "notas.pkl"):
        self.archivo_notas = archivo_notas
        
        try:
            with open(self.archivo_notas, "rb") as f:
                self.notas = pickle.load(f)
        except FileNotFoundError:
                self.notas = []

    def guardar_notas(self):
        with open(self.archivo_notas, "wb") as f:
            pickle.dump(self.notas, f) # que información y dónde lo voy a insertar

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def leer_notas(self):
        return self.notas

    def buscar_nota(self, busqueda):
        return [nota for nota in self.notas if nota.coinciden(busqueda)]

    def eliminar_nota(self, num_nota):
        if num_nota < len(self.notas):
            del self.notas[num_nota]
            self.guardar_notas()
        else:
                print("[!] No se ha encontrado el número de la nota")


    def __str__(self):
        return f"La notas son las siguientes: {self.notas}"
 
