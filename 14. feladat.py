# Kezdeti betét
P = 10000  # Ft
# Névleges kamatláb
r = 0.08  # 8%
# Évközi kamatozások száma
m = 12  # havonta

# A futamidő éveinek számának bekérése a felhasználótól
t = float(input("Kérlek add meg a futamidő hosszát (években): "))

# Jövőbeli érték (FV) kiszámítása
FV = P * (1 + r/m) ** (m * t)

# Eredmény kiírása
print(f"A betét jövőbeli értéke {t} év múlva: {FV:.2f} Ft")
