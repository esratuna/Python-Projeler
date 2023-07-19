#Sezar şifre çözme
def sezar_sifre_coz(sif_coz_metin,k,alfabe=['a','b','c', 'ç','d', 'e', 'f',
                'g','ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm',
                'n', 'o','ö', 'p', 'r', 's','ş', 't',
                'u','ü', 'v','y', 'z']):
  k=k%len(alfabe)
  sif_coz_index=[]
  for harf in sif_coz_metin:
    if harf in alfabe:  
      sif_coz_index.append(alfabe.index(harf))
  sifresiz_metin_index=[]
  for i in range(len(sif_coz_index)):
    sifresiz_metin_index.append(sif_coz_index[i]-k)
  sifresiz_metin=""
  for i in range(len(sifresiz_metin_index)):
    sifresiz_metin+=alfabe[sifresiz_metin_index[i]]
  return(sifresiz_metin)

sezar_sifre_coz(sif_coz_metin="ğuolhöğv",k=3)