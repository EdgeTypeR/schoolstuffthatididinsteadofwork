import math

# Ismételt bekérés, ha a bemeneti érték negatív
while True:
    try:
        körsugár = float(input("Add meg a kör sugarát: "))
        
        if körsugár < 0:
            print("Hiba: A sugár nem lehet negatív. Kérlek, adj meg egy pozitív számot!")
        else:
            break  # Kilépünk a ciklusból, ha a sugár pozitív

    except ValueError:
        print("Hiba: Érvénytelen bemenet. Kérlek, számot adj meg!")

# Számítások
körterület = (körsugár ** 2) * math.pi
körkerület = (körsugár * 2) * math.pi

# Eredmények kiírása
print("A kör területe: ", körterület)
print("A kör kerülete: ", körkerület)
