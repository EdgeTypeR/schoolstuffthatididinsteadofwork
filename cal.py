def osszeadas(a, b):
    return a + b

def kivonas(a, b):
    return a - b

def szorzas(a, b):
    return a * b

def osztas(a, b):
    if b == 0:
        return "Nem lehet nullával osztani!"
    return a / b

print("Válassz egy műveletet:")
print("1. Összeadás")
print("2. Kivonás")
print("3. Szorzás")
print("4. Osztás")

valasztas = input("Add meg a művelet számát (1/2/3/4): ")

szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))

if valasztas == '1':
    print(f"Eredmény: {szam1} + {szam2} = {osszeadas(szam1, szam2)}")

elif valasztas == '2':
    print(f"Eredmény: {szam1} - {szam2} = {kivonas(szam1, szam2)}")

elif valasztas == '3':
    print(f"Eredmény: {szam1} * {szam2} = {szorzas(szam1, szam2)}")

elif valasztas == '4':
    print(f"Eredmény: {szam1} / {szam2} = {osztas(szam1, szam2)}")

else:
    print("Érvénytelen választás!")
