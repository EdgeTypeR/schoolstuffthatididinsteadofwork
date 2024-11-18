def karakterSor(n, ca):
    # Ellenőrzi, hogy ca egyetlen karakter-e
    if not isinstance(ca, str) or len(ca) != 1:
        return "Hiba: A második paraméternek egyetlen karakternek kell lennie."
    
    # Létrehozza az n darab ca karakterből álló sztringet
    return ca * n
