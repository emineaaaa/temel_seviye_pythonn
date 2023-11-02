"""
#LİSTELER

ogrAd="alperen"
ogrSoyad="akal"
ogrYas=22
ogrBoy=1.82
ogrCinsiyet=True

ogrenci=["irem","sönmez",19,1.72,False]
print(ogrenci)
print(ogrenci[0])
print(type(ogrenci))
print(type(ogrenci[-1]))
print(len(ogrenci))


for eleman in ogrenci:
    print(eleman)

ogrenci=[ogrAd,ogrSoyad,ogrYas,ogrBoy,ogrCinsiyet]
print(ogrenci)
print(ogrenci[0])
print(type(ogrenci))
print(type(ogrenci[-1]))
print(len(ogrenci))


for eleman in ogrenci:
    print(eleman)



ad=input("adınızı girin:")
soyad=input("soyadınızı girin:")
yas=int(input("yaşınızı girin:"))
boy=float(input("boyunuzu girin:"))
cinsiyet=bool(input("cinsiyetinizi girin:"))

kullanıcı=[ad,soyad,yas,boy,cinsiyet]

for eleman in kullanıcı:
    print(eleman)



pazar=["elma","armut","incir","karpuz","üzüm","kavun"]

pazar.append("çilek")
print(pazar)
pazar.append("armut")
print(pazar)
print(pazar.count("armut"))
print(len(pazar))
print(pazar.index("armut"))
pazar.insert(1,"ayva")
print(pazar)
pazar.pop(0) #parametre vermezsek son elemanı siler
print(pazar)
pazar.remove("kavun")
print(pazar)
pazar.sort()
print(pazar)
pazar.reverse()
print(pazar)

ikinciPazar=["domates","biber"]
pazar.extend(ikinciPazar)

pazar.clear()
print(pazar)
del pazar
print(pazar)

liste=[]
adet=int(input("kaç adımlı alışveriş yapacaksınız?"))
for pazar in range(adet):
    alıs=input("almak istediğiniz sebze meyveyi girin")
    liste.append(alıs)
print("pazar listeniz:",liste)

#ya da

mesaj=""" """"
hoşgeldiniz
ürün girişinde çıkmak için x e basın
""""""

print(mesaj)
zerzevat=[]
while True:
    urun=input("ürün girişi yapın veya x e basın")
    if urun.lower()!="x":
        zerzevat.append(urun)
    else:
        print("pazar listeniz",zerzevat)
        break


sebze =['domates',"biber"]
meyve=["üzüm","çilek","kivi","karpuz","incir"]
sark=["peynir","helva","bal"]
yesillik=["roka","maydanoz","tere"]
pazarLİstesi=[sebze,meyve,sark,yesillik]
print(pazarLİstesi)
print(pazarLİstesi[0][0])

for dd in pazarLİstesi :
    print(dd)
    if type(dd) is list:
        for urun in dd:
          print(urun ,end="\t")
        print()
    else:
       print(dd)

#ya da


for dd in pazarLİstesi:
   index=pazarLİstesi.index(dd)
   for urun in dd:
      index2=dd.index[urun]
      pazarLİstesi[index][index2]

#ya da

for dd in range(len(pazarLİstesi)):
   for urun in range(len(pazarListesi[dd])):
      pazarLİstesi[dd][urun]


"""

kizlar=["emine","esra","ilayda"]
erkekler=["ali","emre","mert"]
liste=[kizlar,erkekler]
for dd in range(len(liste)):
    for kisi in range(len(liste[dd])):
        print(liste[dd][kisi])


#on sayı al en büyük ve en küçük listeye koy kaçıncı elemanı en büyük kaçıncı en küçük
liste=[]
buyuk=0
kucuk=0
for dd in range(10):
    sayi=int(input("sayi gir:"))
    liste.append(sayi)
    if dd==0:
        buyuk=sayi
        kucuk=sayi
      
    if buyuk<sayi:
        buyuk=sayi
    if kucuk>sayi:
        kucuk=sayi

print((liste.index(buyuk))+1)
print((liste.index(kucuk))+1)


    

