grades = []
while True:
    entry = input("Ingresa una calificación o escribe done, para terminar: ")
    if entry.lower() == "done":
        break
    grades.append(float(entry))

if len(grades) == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    average = sum(grades) / len(grades)
    status = "Passed" if average >= 7.0 else "Failed"
    print(f"Average: {average} — {status}")