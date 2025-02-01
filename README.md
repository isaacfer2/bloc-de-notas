# Bloc de Notas

Este es un sencillo gestor de notas escrito en Python que permite agregar, leer, buscar y eliminar notas.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio:

    ```
    git clone https://github.com/isaacfer2/bloc-de-notas.git
    ```

2. Navega al directorio del proyecto:

    ```
    cd bloc-de-notas
    ```

## Uso

Para ejecutar el programa, simplemente ejecuta el archivo `main.py`:

```
python3 main.py
```

### Menú Principal

1. **Agregar una nota**: Permite agregar una nueva nota.
2. **Leer todas las notas**: Muestra todas las notas almacenadas.
3. **Buscar una nota**: Permite buscar notas que contengan un texto específico.
4. **Eliminar una nota**: Permite eliminar una nota específica.
5. **Salir**: Sale del programa.

## Archivos

- `main.py`: Contiene el menú principal del programa.
- `gestor_notas.py`: Contiene la clase `GestorNotas` que maneja las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de las notas.
- `notas.py`: Contiene la clase `Nota` que representa una nota individual.

## Clases y Métodos

### Clase Nota

- **`__init__(self, contenido)`**: Inicializa una nueva nota con el contenido proporcionado.
- **`coinciden(self, busqueda)`**: Verifica si el contenido de la nota coincide con el texto de búsqueda.
- **`__str__(self)`**: Devuelve el contenido de la nota como una cadena de texto.

### Clase GestorNotas

- **`__init__(self, archivo_notas='notas.pkl')`**: Inicializa el gestor de notas y carga las notas desde un archivo.
- **`guardar_notas(self)`**: Guarda las notas en un archivo.
- **`agregar_nota(self, contenido)`**: Agrega una nueva nota.
- **`leer_notas(self)`**: Devuelve una lista de todas las notas.
- **`buscar_nota(self, busqueda)`**: Devuelve una lista de notas que coinciden con el texto de búsqueda.
- **`eliminar_nota(self, num_nota)`**: Elimina la nota en la posición especificada.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Envía tus cambios a tu repositorio fork (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
```

Puedes ajustar y expandir esta plantilla según sea necesario para tu proyecto.
