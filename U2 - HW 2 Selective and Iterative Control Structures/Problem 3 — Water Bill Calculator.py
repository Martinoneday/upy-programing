total = 0
while True:
    m3 = input("m^3 consumidos o 'exit' para salir: ")
    if m3.lower() == "exit":
        break
    m3 = float(m3)

    if m3 <= 10:
        cargo = m3 * 8
    elif m3 <= 20:
        cargo = m3 * 12
    else:
        cargo = m3 * 18

    total += cargo
    print(f"Month charge: ${cargo:.2f} MXN")

print(f"Total: ${total:.2f} MXN")