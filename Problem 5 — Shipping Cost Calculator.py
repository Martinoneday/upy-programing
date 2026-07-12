total = 0
while True:
    w = input("Peso en kg o exit para salir: ")
    if w.lower() == "exit":
        break
    weight = float(w)
    distance = float(input("Distancia en km: "))

    if distance <= 100:
        costo = 50 if weight <= 5 else 80
    else:
        costo = 120 if weight <= 5 else 200

    total += costo
    print(f"Shipping cost: ${costo:.2f} MXN")

print(f"Total: ${total:.2f} MXN")