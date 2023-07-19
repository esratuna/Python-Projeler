#Sezar şifreleme
def sezar_sifreleme(sifrelenecek_metin,k,alfabe=['a','b','c', 'ç','d', 'e', 'f',
                'g','ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm',
                'n', 'o','ö', 'p', 'r', 's','ş', 't',
                'u','ü', 'v','y', 'z']):
  k=k%len(alfabe)
  sif_met_index=[]
  for harf in sifrelenecek_metin:
    if harf in alfabe:  
      sif_met_index.append(alfabe.index(harf))
  #print(sif_met_index)
  sifreli_metin_index=[]
  for i in range(len(sif_met_index)):
    sifreli_metin_index.append(sif_met_index[i]+k)
  #print(sifreli_metin_index)
  sifreli_metin=""
  for i in range(len(sifreli_metin_index)):
    sifreli_metin+=alfabe[sifreli_metin_index[i]]
  return(sifreli_metin)


kul_sifr_metin=input("Şifrelenecek metni giriniz: ")
kul_sifr_metin=kul_sifr_metin.lower()
k_sayisi=int(input("Bir sayı giriniz: "))
print(sezar_sifreleme(sifrelenecek_metin=kul_sifr_metin,k=k_sayisi))