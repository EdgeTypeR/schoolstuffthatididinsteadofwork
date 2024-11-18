def hanyszor_6():
    hatosok = 0
    for i in range(6000):
        if kocka() == 6:
            hatosok = hatosok+1
print(str(hatosok))
