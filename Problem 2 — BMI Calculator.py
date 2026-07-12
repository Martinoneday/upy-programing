while True:
    weight = input("Peso en kg o exit para salir: ")
    if weight.lower() == "exit":
        break
    height = float(input("Altura en metros: "))
    weight_num = float(weight)
    bmi = weight_num / (height ** 2)

    if bmi < 18.5:
        categoria = "Underweight"
    elif bmi < 25:
        categoria = "Normal"
    elif bmi < 30:
        categoria = "Overweight"
    else:
        categoria = "Obese"

    print(f"BMI: {bmi:} — {categoria}")