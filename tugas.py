while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        a = int(input("Masukkan Angka Anda: "))
        if a > 0:
            print("Bilangan Positif")
        elif a == 0:
            print("Bilangan Nol")
        else:
            print("Bilangan Negatif")
            break
    except ValueError:
        print("Maaf Silahkan masukkan angka")
        # better try again... Return to the start of the loop

