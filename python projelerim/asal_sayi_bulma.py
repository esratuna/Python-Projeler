def asal_mi(sayi):
  bolen_sayisi = 0
  i = 2
  while i<=((sayi/2)+1):
    if sayi>2 :
      
      if sayi%i == 0 :
        bolen_sayisi+=1 
        return False
        break
    i+=1  
  if bolen_sayisi==0 or sayi==2 :
    return True



asal_mi(20)