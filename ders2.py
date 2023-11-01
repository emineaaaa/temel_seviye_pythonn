"""
ad="alpi"
print(len(ad))    #kaç karakterli olduğunu verdi bize


a = "Hello, World!"
print(a.upper())

ad1="alpi"
ad2="emoş"
metin="merhaba {} hoşgeldin"
print (metin.format(ad1))
print (metin.format(ad2))



for dd in range(10):
    print(dd)
    print("alpi")



for dd in range(2,6):
    print (dd)



for dd in range(5,15,3):
    print(dd)



baslangic=1
bitis=20
artis=2
for dd in range(baslangic,bitis,artis):
    print(dd)



baslangic=int(input("baslangıç değerini girin:"))
bitis=int(input("bitiş değerini girin:"))
artis=int(input("artis değerini girin:"))

for dd in range(baslangic,bitis,artis):
    print(dd)

3


isim=input("adınızı girin:")
yas=int(input("yaşınızı girin:"))

for dd in range(yas):
    print(isim)




dilim=int(input("kaç dilim pizza istersiniz?"))

for dd in range(1,dilim+1):
    print("{}. dilim pizzanız afiyet bal şeker!".format(dd))

#birden dokuza kadar olan sayıların toplamı
toplam=0
for dd in range (10):           
    toplam+=dd
print(toplam)

ilk=int(input("hangi değerden itibaren toplama işleminin yapılmasını istersiniz?"))
son=int(input("kaça kadar sayıların toplamını istersin?"))
artis=int(input("kaç artarak işlemin yapılmasını istyediğinizi yazın:"))
toplam=0
for dd in range(ilk,son,artis):
    toplam+=dd

print(toplam)



fakt=1
sayi=int(input("faktöriyelini hesaplamak istediğiniz sayıyı girin:"))
for dd in range(1,sayi+1):
    fakt*=dd

print("sonucunuz:",fakt)


isim=input("ad soyad girin:")
for harf in isim:
    print (harf)



a=0
while a<10:
    print(a)
    a+=1


bas=int(input("başlangıç değeri gir:"))
bit=int(input("biitiş değeri gir:"))
art=int(input("artış değeri gir:"))
toplam=0
while bas>bit:
    print(bas)
    bas+=art
    toplam+=art
else:
    print("hesaplama tamamlanmıştır")
print("girilen değerlerin toplamı",toplam)

#while ın else i çok kullanılmaz

#pass-->döngü çalışır sonra bi şeyler yazabilmemiz için kullanırız amaç sadece döngüyü çalıştırabilmek
#break-->döngüden çıkıp programın döngü dışında çalışmasını sağlar
#continue-->döngünün geri kalan işlemlerini yapmasını pas geçerek devam ettiriyo geri kalanlarını


for dd in range(10):
    if dd==5:
        break#döngüyü kırdı ve bitirerek döngünün dışına çıkar
    print(dd)

for dd in range(10):
    if dd==5:
        continue #döngünün kendisinden sonra kaldığı yerden devam etmesinş sağlar
    print(dd)




carpim=1
while True:
    sayi=int(input("sayı gir:"))
    if sayi==0:
        print("girdiğiniz sayıların çarpımı",carpim)
        break
    carpim*=sayi


    

carpim=1
for dd in range(10):
    sayi=int(input("sayı gir:"))
    if sayi==0:
        print("girilenlerin çarpımı:",carpim)
        break
    carpim*=sayi
    if sayi==111:
       continue 
    
print("sonucunuz:",carpim)



dersSayisi=int(input("toplam ders sayınızı girin:"))
genelOrtTop=0
for ders in range(1,dersSayisi+1):
    print(ders,"dersinizde kaç sınavın var?")
    sinavSayisi=int(input())
    toplam=0
    for sinav in range(1,sinavSayisi+1)
        print(ders,"dersinin",sinav,"sınav notu")
        sinavPuani=int(input())
        toplam+=sinavPuani
    ortalama=toplam/sinavSayisi
    genelOrtTop=genelOrtTop/dersSayisi
sonucOrt=genelOrtTop/dersSayisi
print("derslein genel ortalaması:",sonucOrt)


#1
for dd in range(1,30):
    if dd%2==1:
        print(dd)

#2
toplam=0
carpim=0
for dd in range(10):
    sayi=int(input("sayı girin:"))
    toplam+=sayi
    carpim+=sayi
print("toplam sonucu:",toplam,"çarpım sonucu:",carpim)


#3


#4
tekTop=0
ciftTop=0
for dd in range(20):
    sayi=int(input("sayi girin:"))
    if sayi%2==1:
        tekTop+=sayi
    else:
        ciftTop+=sayi
print("teklerin toplamı:",tekTop,"çiftlerin toplamı:",ciftTop)

#5

sonuc=1
for birinciCarpan in range(10):
    for ikincicarpan in range(10):
        sonuc=birinciCarpan*ikincicarpan
        print(birinciCarpan,"x",ikincicarpan"=",sonuc)

        
#6
sonuc=1
sayi1=0
while sayi1<10:
     sayi2=0
     while sayi2<10:
        sonuc=sayi1*sayi2
        print(sayi1,"x",sayi2,"=",sonuc)    
        sayi2+=1
     sayi1+=1

 
#8
for sayi in range(100):
    if sayi%3==0 and sayi%3==0:
        print(sayi)
    """



"""
#14
sayimiz=73
while True:
    kullanıcıSayisi=int(input("aklınızdan bir sayı tutun:"))
    if kullanıcıSayisi==sayimiz:
        print("kazandınız!")
        break
    elif kullanıcıSayisi>73:
        print("daha küçük sayı girin")
    elif kullanıcıSayisi<73:
        print("daha büyük sayı girin")

"""


