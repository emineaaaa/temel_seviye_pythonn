
print(type(5))

print(type("alpi"))

a=True
print(a)
print(type(a))

b=5
b+=4
print (b)

isim="alpi"
isim*=3
print(isim)

s1=12
s2=str(s1)
print(type(s1))
print(type(s2))

deger="123"
dDeger=int(deger)
print(dDeger)

print("adınızı girin:")
isim= input()
print("soyadınızı girin: ")
soyiism=input()
print("Hoşgeldin",isim,soyiism)


boy=float(input("Boy bilgisi girin:"))




#alıştırma soruları 1(bölüm2)
not1=64.86
not2=70
not3=86
ort=(not1+not2+not3)/3
print("öğrencinin ortalaması:",ort)

not1=int(input("ilk notu gir:"))
not2=int(input("ikinci notu gir:"))
not3=int(input("son notu gir"))
ort=(not1+not2+not3)/3
print("öğrencinin ortalaması:",ort)




#alıştırma 2
isim=input("adınızı girin:")
yas=int(input("yaşınızı giriniz:"))
isim*=yas
print("isim")



#alıştırma3
print("yarı çapı girin:")
r=float(input())
print("pi değerini giriniz:")
pi=float(input())
alan=pi*r**2
cevre=2*pi*r

print("alanınız:",alan)
print("çevresi:",cevre)



#alıştırma 4
print("doğum tarihinizi giriniz:")
dTarihi=int(input())
yas=2023-dTarihi
print(yas>=18)

#alıştırma5
faiz=float(input("faiz oranını(yüzde) giriniz"))
para=float(input("para miktarını giriniz"))
yıllıkFaiz=para*faiz
print("yıllık faiziniz:",yıllıkFaiz)


#alıştırma6
kilo=int(input("kilonuzu giriniz:"))
print ("yaşınızı giriniz:")
boy=float(input())
endeks=kilo/boy**2
print("boy-kilo endeksiniz:",endeks)


#alıştırma7
isim=input("İsminizi giriniz:")
print(isim=="emine")


#alıştırma8
ort=input("not ortalamanızı giriniz:")
print(ort>=70)


#alıştırma9
uzunluk=input("otoban uzunluğunuzu girin:")
sure=input("geçiş sürenizi giriniz:")
hiz=uzunluk/sure
print(hiz>=130)


#alıştırma10
gun=input("çalışılan gün sayısını girin: ")
tutar=350*gun
print(tutar)


print("adım emine")
print("soyadım aydınlı")
print("yaşım 20")
print("süleyman demirel üniversitesinde okuyorum")
print("bilgisayar mühendisliği bölümü öğrencisiyim")


sayi=1
isim="alpi"
dger=2.5
dogruluk=True
print(sayi,isim,dger,dogruluk)


#çoklu değişkne ataması
a,b,c=1,2,3
print(a)

#değerleri değiştirdik
a,b=b,a
print (a,b)

isim=input("isminiz nedir?")
soyisim=input("soyisminiz nedir?")
print("memnun oldum",isim,soyisim,"!")
yas=int(input("yasınız nedir?"))
print("benim de yasım",yas)


boy=float(input("boyunuzu girin:"))
ogrenim=input("üniversite öğrencisi misiniz:")

if boy>=180 and ogrenim == "evet":
    print("turnuvaya katılmaya hak kazandınız")
else:
    print("katılmaya hak kazanamadınız")



ort=int(input("ortalamanızı girin:"))
if ort>=70:
    if ort>85:
        print("takdir aldınız")
    else:
        print("teşekkür aldınız")
else:
    print("belge alamadınız")

#tek satırlık koşul yapısı
a=5
b="büyüktür "if a>2 else "küçüktür"
print (b)

#else + if ---->elif
gun=input("haftanın hangi günü")
if gun=="pazartesi":
    print("1")
elif gun=="sali":
    print("2")
elif gun =="çarşamba":
    print("3")

 
ort=int(input("ortalamanızı yazın"))
if ort>=70 and ort<85:
    print("teşekkür alamya hak kazandınız")
elif ort>=85:
    print("takdir almaya hak kazandınız")    
else :
    print("belge alamaya hak kazanamadınız")    

#1
memlekt=input("nerelisiniz? ")
if memlekt=="karaman":
    print("hemşeryiz!")
else :
    print("hemşeri değiliz.")


#2
sayi1=int(input("ilk sayıyı girin:"))
sayi2=int(input("ikinci sayııyı girin:"))
if sayi1>sayi2:
    print(sayi1,sayi2)
else :
    print(sayi2,sayi1)



#3
s1=int(input("sayı gir"))
s2=int(input("sayı gir"))
s3=int(input("sayı gir"))


if s1>s2 and s1>s3:
    
    if s2>s3:
        print(s1,s2,s3)
    else:
        print(s1,s3,s2)
elif s2>s3 and s2>s1:
    if s3>s2:
        print(s2,s3,s1)
    else:
        print(s2,s1,s3)
else:
    if s1>s2:
        print(s3,s1,s2)
    else:
        print(s3,s2,s1)
#ya da if koşul kısmına s1>s2>s3 şeklinde dıra sıra değerlendirebiliriz.

#4
yas=int(input("yaşınızı girin:"))
ogrenim=input("öğrenim durumunuzu girin:")

if yas>=18 and ogrenim=="ilköğretim":
    print("ehliyet almaya hak kazandınız")
else:
    print("ehliyet almaya hak kazanamadınız")

#6
print("MENU")
print("1- hamburger   2-pizza    3-gözleme")
print("1- kola   2-ayran")

sip1=input("yiyecek seçin")
sip2=input("içecek seçin")

if sip1=="hamburger" or sip1=="pizza":
    print("doğru sipariş")
elif sip1=="gözleme:":
    print("doğru sipariş")
else:
    print("yanllış sipariş")

if sip2=="kola" or sip2=="ayran":
    print("doğru sipariş")
else:
    print("yanlış sipariş")



#7
gun=input("hanfi gündeyiz? ")
if gun =="pazartesi":
    print("pazarlama elemanı bugün karşıyakada")
elif gun=="sali":
    print("pazarlama elemanı bugün bostanlıda")
else:
  print("pazarlama uzmanı bugün yenigirnede")


#8
ort1=int(input("ilk ort gir"))
ort2=int(input("ikinci ort gir"))
ort3=int(input("üçüncü ort gir"))

gecmeNot=(ort1+ort2+ort3)/3

if gecmeNot>=60:
    print("geçtin")
else :
    print("kaldın")


    #9

    #10
isim=input("kullanıcı ismi girin:")
sisim=input("kullanıcı soyadı girin:")

if isim=="Alperen" and sisim=="Akal":
    print("HOŞGELDİNİZ!")
else:
    print("KULLANICI DOĞRULANAMADI")


#12
print("programlama dili katoloğu:\n1-python 2-java 3-swift")
pdili=input("yukarıdakilerden programlama dili seçiniz:")

if pdili=="1":
    print("geliştiriciler:ali\nahmet\nmehmet")
elif pdili=="2":
    print( "geliştiriciler:ayşe\nfatma\hayriye")
else :
    print("geliştriciler:ali\nveli")


#13
tercih=input("menü seçimi yapın")

if tercih=="menü 1":
    print("ödemeniz 50 tl")
elif tercih=="menü 2":
    print("ödemeniz 35 tl")
elif tercih=="menü 3":
    print("ödemeniz 40 tl")
else :
    print("geçersiz menü tercifhi yaptınız lütfen tekrarar deneyin")






