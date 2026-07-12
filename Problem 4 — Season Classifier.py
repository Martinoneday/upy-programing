while True:
    m = input("Ingrese el número de mes o exit para salir: ")
    if m.lower() == "exit":
        break
    m = int(m)

    if m < 1 or m > 12:
        print("Mes invalido, ingrese uno entre 1 y 12")
        continue

    if m in (12, 1, 2):
        estacion = "Winter"
    elif m in (3, 4, 5):
        estacion = "Spring"
    elif m in (6, 7, 8):
        estacion = "Summer"
    else:
        estacion = "Fall"

    print(estacion)