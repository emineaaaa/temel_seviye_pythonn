#f=open("file.txt")#dosya açtık
#f=open("file.txt","rt") #okuma modunda açtık
"""
dosya=open("test.txt","r")
metin=dosya.read()
print(len(metin))

dosya=open("test.txt","r")
print(dosya.readline())

dosya=open("test.txt","r")
for satir in dosya.readlines():
    print(satir)

dosya.close()


dosya=open("test.txt","r")
satirlar=metin.split("\n")
print(satirlar)
for satir in satirlar:
    print(satir)



dosya=open("test.txt","a")
dosya.write("asdfg")
dosya.close()

dosya=open("istatistik.txt","r")
print(dosya.read())


import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("the file does not exist")
"""

import random
import os
while True:
 if os.path.exists("istatistikler.txt"):
    os.remove("istatistikler.txt")
 else:
  tercih=input("""
 1-oyun oyna 2-istatistik görüntüle 3-çıkış yap
tercihinizi yapın
  """)
 if tercih=="1":
   rnd=random.randrange(1,10)

   taban=0
   tavan=10

   sayi=int(input("sayı tahmini yapın:"))
   while True:
     if sayi==rnd:
        print("sayıyı buldun")
        dosya=open("istatistikler.txt","a")
        dosya.write(str(rnd)+"\t")
        dosya.close()
        break
     else:
        print("sayıyı bulamadın tekrar tahmin yapılacak")
        if sayi>rnd:
            print("azalt")
        else:
            print("arttır")
 elif tercih=="2":
   dosya=open("istatistikler.txt","r")
   print(dosya.read())
   dosya.close()
 elif tercih=="3":
    print("cıkıs yaptiniz.")
    break

   