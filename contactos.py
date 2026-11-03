import csv


ARCHIVO_TEXTO = "contactos.csv"
ARCHIVO_BINARIO = "contactos.bin"
COLUMNAS = ["id", "nombre", "telefono"]


def cargar_contactos():
    with open(ARCHIVO_TEXTO, "a+", newline="", encoding="utf-8") as archivo:
        archivo.seek(0)
        if not archivo.read(1):
            archivo.seek(0)
            csv.writer(archivo).writerow(COLUMNAS)

        archivo.seek(0)
        lector = csv.reader(archivo)
        next(lector)
        contactos = []
        for fila in lector:
            contactos.append([int(fila[0]), fila[1], fila[2]])
        return contactos


def agregar_contacto():
    contactos = cargar_contactos()
    id_texto = input("ID: ").strip()
    if not id_texto.isdigit() or int(id_texto) < 1:
        print("El ID debe ser un número positivo.")
        return

    identificador = int(id_texto)
    for contacto in contactos:
        if contacto[0] == identificador:
            print("Ya existe un contacto con ese ID.")
            return

    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    if not nombre or not telefono:
        print("El nombre y el teléfono son obligatorios.")
        return

    with open(ARCHIVO_TEXTO, "a", newline="", encoding="utf-8") as archivo:
        csv.writer(archivo).writerow([identificador, nombre, telefono])
    print("Contacto guardado.")


def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
        return

    print("\nID | NOMBRE | TELÉFONO")
    for contacto in contactos:
        print(f"{contacto[0]} | {contacto[1]} | {contacto[2]}")


def buscar_contactos():
    consulta = input("Busca por ID, nombre o teléfono: ").strip().lower()
    encontrados = []
    for contacto in cargar_contactos():
        if (
            consulta in str(contacto[0])
            or consulta in contacto[1].lower()
            or consulta in contacto[2].lower()
        ):
            encontrados.append(contacto)
    mostrar_contactos(encontrados)


def guardar_binario():
    contactos = cargar_contactos()
    with open(ARCHIVO_BINARIO, "wb") as archivo:
        archivo.write(len(contactos).to_bytes(4, "big"))
        for contacto in contactos:
            nombre = contacto[1].encode("utf-8")
            telefono = contacto[2].encode("utf-8")
            archivo.write(contacto[0].to_bytes(4, "big"))
            archivo.write(len(nombre).to_bytes(2, "big"))
            archivo.write(len(telefono).to_bytes(2, "big"))
            archivo.write(nombre + telefono)
    print("Contactos guardados en el archivo binario.")


def leer_binario():
    with open(ARCHIVO_BINARIO, "rb") as archivo:
        datos = archivo.read()

    cantidad = int.from_bytes(datos[:4], "big")
    posicion = 4
    contactos = []
    for _ in range(cantidad):
        identificador = int.from_bytes(datos[posicion:posicion + 4], "big")
        largo_nombre = int.from_bytes(datos[posicion + 4:posicion + 6], "big")
        largo_telefono = int.from_bytes(datos[posicion + 6:posicion + 8], "big")
        posicion += 8
        nombre = datos[posicion:posicion + largo_nombre].decode("utf-8")
        posicion += largo_nombre
        telefono = datos[posicion:posicion + largo_telefono].decode("utf-8")
        posicion += largo_telefono
        contactos.append([identificador, nombre, telefono])
    mostrar_contactos(contactos)


while True:
    print(
        "\n--- GESTIÓN DE CONTACTOS ---\n"
        "1. Agregar contacto\n"
        "2. Mostrar contactos\n"
        "3. Buscar contactos\n"
        "4. Contar contactos\n"
        "5. Guardar archivo binario\n"
        "6. Leer archivo binario\n"
        "0. Salir"
    )
    opcion = input("Selecciona una opción: ").strip()

    match opcion:
        case "1":
            agregar_contacto()
        case "2":
            mostrar_contactos(cargar_contactos())
        case "3":
            buscar_contactos()
        case "4":
            print(f"Total de contactos: {len(cargar_contactos())}")
        case "5":
            guardar_binario()
        case "6":
            leer_binario()
        case "0":
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida.")
