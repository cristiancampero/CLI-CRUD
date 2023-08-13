import sys

# Crea un diccionario para almacenar los registros
records = {}

# Imprime el menú principal
def print_menu():
    print("1. Guardar registro")
    print("2. Listar registros")
    print("3. Editar registro")
    print("4. Eliminar registro")
    print("5. Salir")

# Solicita al usuario una opción del menú
def get_user_input():
    user_input = input("Ingresa una opción: ")
    while user_input not in ["1", "2", "3", "4", "5"]:
        user_input = input("Ingresa una opción válida: ")
    return user_input

# Guarda un registro
def save_record():
    name = input("Nombre: ")
    while not name.isalpha():
        print("El nombre debe contener solo letras.")
        name = input("Nombre: ")
    age = input("Edad: ")
    while not age.isdigit() or int(age) <= 1 or int(age) > 120:
        print("La edad debe ser un número entre 1 y 120.")
        age = input("Edad: ")
    # Genera un id automáticamente
    id = len(records) + 1
    records[id] = {"name": name, "age": age}
    print("El registro se guardó correctamente\n")

# Lista los registros
def list_records():
    print()
    for id, record in records.items():
        print(id, record["name"], record["age"])
    print()

def edit_record():
    while True:
        try:
            record_id = int(input("Ingresa el ID del registro que quieres editar: "))
            break
        except ValueError:
            print("ID Invalido. El ID debe ser un número.")
    while record_id not in records:
        print("ID Invalido. El ID debe ser un número.")
        record_id = int(input("Ingresa el ID del registro que quieres editar: "))
    name = input("Nombre: ")
    while not name.isalpha():
        print("El nombre debe contener solo letras.")
        name = input("Nombre: ")
    age = input("Edad: ")
    while not age.isdigit() or int(age) < 0 or int(age) > 120:
        print("La edad debe ser un número entre 0 y 120.")
        age = input("Edad: ")
    records[record_id]["name"] = name
    records[record_id]["age"] = age
    print("El registro se editó correctamente\n")

def delete_record():
    while True:
        try:
            record_id = int(input("Ingresa el ID del registro que quieres eliminar: "))
            break
        except ValueError:
            print("ID Invalido. El ID debe ser un número.")
    while record_id not in records:
        print("ID Invalido. El ID debe ser un número.")
        record_id = int(input("Ingresa el ID del registro que quieres eliminar: "))
    del records[record_id]
    print("El registro se eliminó correctamente\n")



# Ejecuta el programa
while True:
    print_menu()
    user_input = get_user_input()
    if user_input == "1":
        save_record()
    elif user_input == "2":
        list_records()
    elif user_input == "3":
        edit_record()
    elif user_input == "4":
        delete_record()
    else:
        sys.exit()
