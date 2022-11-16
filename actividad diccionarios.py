#consulta frutas / look for a fruit
def consulta():
    consulta = input("\nIngrese la fruta que desea consultar: ").capitalize()
    if consulta.title() in dictFrutas:
       print(f"El precio de la fruta {consulta} es de: ${dictFrutas[consulta.title()]}")
    else:
        print("Esa fruta no existe en la tienda.")

#Ingresa frutas / input a fruit
def ingresaFrutas():
    fruta = input("Ingrese la fruta que desea agregar: ").capitalize()
    if fruta.title() in dictFrutas:
         print("\nEsta fruta ya está en la tienda.")
    else:
        precio = int(input("Ingrese el precio de la nueva fruta: "))
        dictFrutas[fruta] = precio
        print("\nFruta agregada con exito.")

#Reemplazar fruta / replace a fruit
def reemplazaFruta():
    fruta = input("\n¿Qué fruta desea modificar?: ").capitalize()
    if fruta.title() in dictFrutas:
        nuevoPrecio = int(input("Ingrese el nuevo precio de la fruta: "))
        dictFrutas[fruta] = nuevoPrecio
        print("El precio de la fruta se ha actualizado exitosamente.")
    else:
        print("Esta fruta no está en la tienda.")

#Eliminar fruta / delete a fruit
def eliminarFruta():
    fruta = input("\nIngrese la fruta que desea borrar: ").capitalize()
    if fruta.title() in dictFrutas:
        del dictFrutas[fruta]
        print("La fruta ha sido eliminada exitosamente.")
    else:
        print("La fruta no existe en la tienda.")

#Lista de objetos / list of the fruits
def listaObjetos():
    lista = dictFrutas.items()
    lista = list(lista)
    print(f"\n----------------------")
    for i in range(len(lista)):
        print(f"|{i} | {lista[i]}")

#Mostrar inventario / show inventory
def inventario():
    print(f"\nLa cantidad de frutas en la tienda es de: {len(dictFrutas)}\
        \nEl valor del inventario es de: ${sum(dictFrutas.values())}\
        \nEl precio promedio de las frutas es de: ${sum(dictFrutas.values())/len(dictFrutas)}")

#Ventas / sales
def ventas():
    neto = 0
    frutas = list(dictFrutas.keys())
    precios = list(dictFrutas.values())
    print("\nLas frutas disponibles son: ")
    for i in range(len(frutas)):
        print(f"{i+1}| {frutas[i]}, precio:   ${precios[i]}")
    while True:
        fruta = input("\n¿Qué fruta desea comrar?: ").capitalize()
        while True:
            if fruta.title() in dictFrutas:
                break 
            else:
                fruta = input("\n¿Ingrese una fruta válida?: ").capitalize() 
        cantidad = int(input("¿Qué cantidad desea comprar?: "))
        print(f"El total para esta fruta es de: {dictFrutas[fruta]*cantidad}")
        neto += dictFrutas[fruta] * cantidad
        print(f"El total sera de: ${neto}")
        otra = input("¿Desea comprar otra fruta? SI/NO: ").upper()
        if otra == "NO":
            break
    global ventasDia
    ventasDia += neto
    return neto





#Crear diccionario / create the dictionary
dictFrutas = {
    "Lulo":500,
    "Pera":300,
    "Manzana":600,
    "Sandia":250,
    "Uva": 100
}

ventasDia = 0

while True:
    print("\n********MENÚ********\n____________________\n|1) Consultar      |\n|2) Agregar        |\n|3) Modificar      |\
    \n|4) Borrar         |\n|5) Lista de frutas|\n|6) Inventario     |\n|7) Vender fruta   |\n|8) Ventas del día |\
    \n|9) Terminar       |\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    #Opcion de respuesta / answer
    opcion = int(input("\nIngrese una opción del menú: ").capitalize())

    if opcion == 1:
        consulta()
        print(dictFrutas)
    elif opcion == 2:
        ingresaFrutas()
    elif opcion == 3:
        reemplazaFruta()
    elif opcion == 4:
        eliminarFruta()
    elif opcion == 5:
        listaObjetos()
    elif opcion == 6:
        inventario()
    elif opcion == 7:
        neto = ventas()
        print(f"\nEl total a comprar sera de: ${neto}")
    elif opcion == 8:
        print(f"El total de ventas del dia fue de: ${ventasDia}")
    elif opcion < 1 or opcion > 9:
        print("Ingrese una opción valida.") 
    else:
        print("Adios.")
        break