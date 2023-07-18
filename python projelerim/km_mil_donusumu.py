def km_mil_donusumu():
    print("km_mil dönüşüm programına hoşgeldiniz.")
    birim = input("Dönüştürmek istediğiniz birimi giriniz : km veya m = ")
    sayı = float(input("Uzaklık birimini giriniz = "))
    km = sayı / 1.609344
    m = sayı*(1.609344)
    if birim == "km" :
        print(sayı , birim , " = " , m)
    if birim == "m":
        print(sayı , birim , " = " , km)

km_mil_donusumu()