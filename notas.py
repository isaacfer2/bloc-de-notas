#!/usr/bin/python3

class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def coinciden(self, busqueda):
        return busqueda in self.contenido

    def __str__(self):
        return self.contenido
