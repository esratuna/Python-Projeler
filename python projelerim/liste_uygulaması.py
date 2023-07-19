isim_listesi = ["Ali","Ayşe","Mehmet","Esra","Salih"]
while True:
  print("""
          Y = Yeni Kayıt
          S = Kayıt Silmek için
          Q = Çıkmak için

  """)
  aranan_ad = input("İsminizi Giriniz = ")
  aranan_ad.lower()
  aranan_ad.capitalize()
  if aranan_ad in isim_listesi :
    print("İsminiz listede mevcuttur")
  if aranan_ad == "Q" :
    print("Döngü bitti")
    break

  elif aranan_ad == "S" :
    kayıt = input("Lİsteden silmek istediğiniz kayıtı giriniz")
    if kayıt in isim_listesi :
      isim_listesi.remove(kayıt)
      print(isim_listesi)
    else :
      continue
  else :
    isim_listesi.append(aranan_ad)
    print(isim_listesi)