#suma de positivos
#n = [5, 10, -50, 70, -6, -5, -8]
n=[]
while True:
    num= (input("Ingrese un número o exit para terminar: "))
    if num == "exit":
        break
    else:
        n.append(int(num))
t = 0
for i in n:
    if i < 0:
        continue
    t= t + i
print(f"La suma es {t}")