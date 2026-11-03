# Gestión de Contactos

Este proyecto es una pequeña aplicación en Python para administrar contactos.

## ¿Qué hace?

Permite:
- agregar contactos
- mostrar todos los contactos
- buscar contactos por ID, nombre o teléfono
- contar registros
- guardar la información en un archivo binario
- leer contactos desde un archivo binario

## Archivos principales

- `contactos.py`: lógica principal de la aplicación
- `contactos.csv`: almacena los contactos en formato CSV
- `contactos.bin`: almacena la información en formato binario

## Requisitos

- Python 3.x

## Cómo ejecutarlo

```bash
python contactos.py
```

## Menú

1. Agregar contacto
2. Mostrar contactos
3. Buscar contactos
4. Contar contactos
5. Guardar archivo binario
6. Leer archivo binario
0. Salir

## Nota

La aplicación guarda los datos en `contactos.csv` y también puede exportarlos a `contactos.bin`.
