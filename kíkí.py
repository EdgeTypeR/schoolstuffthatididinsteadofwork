a = int(input("Kérem az első számot: "))
b = int(input("Kérem a második számot: "))

# Számítások
hanyados = a // b
maradek = a % b

# "-szor"/"-szer" rag kiválasztása
if hanyados % 10 == 1:
    rag_szor = "-szer"
else:
    rag_szor = "-szor"

# "-ban"/"-ben" rag kiválasztása, speciális kivétellel
utolso_szamjegy = a % 10
if utolso_szamjegy == 6 and a != 6:  # Ha a szám 6-tal végződik, de nem maga a 6 szám
    rag_ban = "-ban"
elif utolso_szamjegy in [2, 4, 5, 6, 9]:  # "magas hangrendű" számok esetén "-ben"
    rag_ban = "-ben"
else:  # "mély hangrendű" számok esetén "-ban"
    rag_ban = "-ban"

# Eredmény kiírása
print(f"A(z) {b} megvan a(z) {a}{rag_ban} {hanyados}{rag_szor}, megmaradt a(z) {maradek}.")
