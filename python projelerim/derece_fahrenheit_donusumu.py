def derece_fahrenheit_donusum ():
    birim = input("Dönüştürmek istediğiniz birimi giriniz: derece (C) veya Fahreheit (F)")
    sayi =float(input("Sıcaklık birimini giriniz: Örneğin 20C  veya 18F"))
    derece = (sayi-32) / 1.8
    fahrenheit = 1.8 * sayi + 32
    if birim == "C" :
        print("C = " , fahrenheit )
    if birim == "F":
        print("F = " , derece )

derece_fahrenheit_donusum()