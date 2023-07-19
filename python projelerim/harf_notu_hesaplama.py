sınav1 = int(input("1. sınav notunuzu giriniz"))
sınav2 = int(input("2. sınav notunuzu giriniz"))
ortalama = (sınav1 + sınav2)/2
if (100>=ortalama>=90):
  print(ortalama,"Harf notu = A")
if (90>ortalama>=75):
  print(ortalama,"Harf notu = B")
if (75>ortalama>=50):
  print(ortalama,"Harf notu = C")
if (50>ortalama>=0):
  print(ortalama,"Harf notu = D")