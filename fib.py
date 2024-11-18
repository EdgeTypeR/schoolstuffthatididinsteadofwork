# Fibonacci sorozat első 10 elemének kiírása

# Kezdő értékek
a, b = 1, 1

# Számláló a 10 elemhez
for _ in range(10):
    print(a)  # Kiírjuk az aktuális Fibonacci számot
    a, b = b, a + b  # Frissítjük az a és b értékeket
