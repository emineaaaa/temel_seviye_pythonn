#MODÜL      import ile dahil ediyoruz.     (import math diyebilirz ya da from math import*  ya da from math import cos,sin,sin,pi diyebiliriz.)
# dir(math) dersek kütüphanenin içerisinde kullanabileceğimiz özellikleri görebiliriz.
#pip install flask -->paket yöneticisi ile bir şeyler ekleme.

#import math

#a=math.cos(30)
#print(a)
#print(dir(math))
#print(math.factorial(5))
##derece=math.degrees(90)
#print(math.cos(derece))
#print(help(math))
#print(math.pow(5,6))
#print(help(math.cos))
#print(math.sqrt(16))
 

#from math import *
#print(cos(90))
#print(pi)



"""
rnd=random.randrange(1,10)
for dd in range(10):
 sayi=int(input("bir ile on arasında bir sayi girin:"))
 if sayi==rnd:
     print("tebrikler kazandınız")
 else:
     if sayi>rnd:
        print("azalt")
     else:
        print("arttır")


import random
rnd=random.randrange(1,10)
print("bulunmaya çalışılan sayı:",rnd)
taban=0
tavan=10
while True:
    biltahmin=random.randrange(taban,tavan)
    print("bilgisayarın tahmini:",biltahmin)
    if biltahmin==rnd:
        print("bilgisayar sayıyı buldu")
        break
    else:
        print("bilgisayar sayıyı bulamadı tekrar tahmin yapılacak")
        if biltahmin>rnd:
            tavan-=1
        else:
            taban+=1

    

import datetime
import time
time.sleep(5)
a=input("ilk bilgiyi gir")
giris=datetime.datetime.now()
b=input("ikinci bilgiyi gir")
cikis=datetime.datetime.now()
fark=giris-cikis
print(fark.microseconds) 


#1000 e kadar olan asal sayıların adedini ve geçen zamanı bulan program
from datetime import datetime 
import math
sonDeger=1000
sayac=0
zaman=datetime.now()#süre başladı
for deger in range(2,sonDeger):
    kontrol=True#degerlerin kontrolü için ilk deger true veriliyor
    for bolenSayi in range(2,int(math.sqrt(deger))+1):
        if deger % bolenSayi==0:
            kontrol=False #tam bölme işlemi oluşturuyorsa kontrol false oldu
            break
    if kontrol:
        print(deger)
        sayac+1
print()
gecenZaman=datetime.now() - zaman 
print("Adet:",sayac,"Gecen zaman:",gecenZaman,"saniye")

"""





