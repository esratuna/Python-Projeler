def vücut_kitle_endeksi_hesapla():
    boy = float(input("Boyunuzu giriniz = "))
    kilo = float(input("Kilonuzu giriniz = "))
    kitle_endeks = kilo/(boy**2)

    if kitle_endeks < 18.5 :
        print(kitle_endeks)
        print("Normale göre zayıfsınız")

    elif 18.5 < kitle_endeks <= 25 :
        print(kitle_endeks)
        print("Kilonuz Normal")

    elif 25 < kitle_endeks < 30:
        print(kitle_endeks)
        print("Kilonuz Normalden Fazla")

    else :
        print(kitle_endeks)
        print("En kısa sürede doktora başvurunuz")

vücut_kitle_endeksi_hesapla()