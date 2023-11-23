import os

#FONKSİYONLAR
#yazdir=print
#yazdir("merhaba")

#giris=input
#tamsayi=int

"""
#fonksiyon tanımlarken def ifadesini kullanırız
def selamla():
    print("merhabaa")

mesaj=selamla()
print(mesaj)
print(type(mesaj))
print(selamla())




def selamla(isim):
    print("merhaba",isim)

#selamla() ----->hata verir
selamla("alpi")
mesaj=selamla(8)
print(type(mesaj))



def pi():
    print("pi fonksiyonu çalıştı")
    return 3.14

donus=pi()
print(donus)
print(type(donus))
cevre=pi()*5**2
print(cevre)
print(type(pi()))



def kare(a):
    return a**2
sayi=int(input("hangi sayinin degerini hesaplayalım?"))
deger=kare(sayi)
print(deger)



def daire (r,pi=3.14):  #----->değer girilmemesi halinde deafult değer atamış olduk.
    alan=pi*r**2
    return alan
print(daire(5,3))



def sayiYazdir(*sayilar):
    print(sayilar)

sayiYazdir(1,2,3,4,5)



#**kwargs keywordlü argümanlar almamızı sağlar 
#kwargs ise dict tipinde veri oluşturur

def oKarti(**kwargs):
    print(kwargs)
    oBilgiler={**kwargs}
    print(oBilgiler)
oKarti(oAdi="alpi",oNo=6,sehir="ankara")



def fakt(n):
    if n!=0:
        return n*fakt(n-1)
    else:
        return 1
print(fakt(3))


def azaltan(n):
    if n!=0:
        print(n)
        return azaltan(n-1)
    else:
        return 0
print(azaltan(5))



def ogrList(liste):
    if len(liste)>0:
        print(liste[0])
        return ogrList(liste[1:])
    
        
print(ogrList(["alpi","emoş"]))




def main():
    print("program başlatma fonksiyonu")
    ikinci()
def ikinci():
    print("sonradan çalıştırılan fonsiyon")
main()


#if __name__=='__main__':     ---->main tanımlamadıysam main olamsını isteğim fonksiyon adını yazarak bu if yapısını kullanırız.
#    fonksiyon_adi()




from math import sqrt

def asal(n):
    kok=round(sqrt(n))+1
    kontrol=0
    for deneme in range(2,kok):
        if n %deneme==0:
            kontrol+=1
    return True if kontrol==0 else False

def main():
    enBuyuk=int(input("asal sayıları hangi değere kadar gösterelim? "))
    for deger in range(2,enBuyuk+1):
        if asal(deger):
            print(deger,end='')
print()
main()








import random
import os


def cikis():
    print("Çıkış Yapıldı - Oyun Bitti")
    exit()


def dosya_kontrol(dosya):
    if not (os.path.exists(dosya_adi)):
        dosya = open(dosya_adi, "x")
        dosya.close()


def oyun(dosya_adi):
    dosya = open(dosya_adi, "a")
    rastgele = random.randrange(1, 100)
    dosya.write(str(rastgele) + " tahminleriniz:")
    tahminSayisi = 10
    taban = 0
    tavan = 100
    while tahminSayisi >= 1:
        tahmin = int(input("Bir sayı giriniz"))
        dosya.write(str(tahmin) + ",")
        if tahmin == rastgele:
            dosya.write("+kazandiniz" + "\n")
            print("Tebrikler")
            break
        elif tahmin > rastgele:
            print("daha küçük giriniz")
            tavan = tahmin
        elif tahmin < rastgele:
            print("daha büyük giriniz")
            taban = tahmin
        tahminSayisi -= 1
        print("kalan hakkınız", tahminSayisi)
        if tahmin == 0:
            dosya.write("kaybettiniz" + "\n")
            dosya.close()


def istatistik(dosya_adi):
    dosya = open(dosya_adi, "r")
    print(dosya.readlines())
    dosya.close()


while True:
    while True:
     dosya_adi = "oyun.txt"
     dosya_kontrol(dosya_adi)
     cevap = int(input("Oyun için :1 \n İstatistik için : 2\t Çıkış için: 3\t"))
     if cevap == 3:
        cikis()
     elif cevap == 1:
        oyun(dosya_adi)
     elif cevap == 2:
        istatistik(dosya_adi)





x=50
def myfunc():
    global x
    x=300
    print(x)
def fonk2 ():
    print(x)

fonk2()
myfunc()
fonk2()






x=2
print("1. x=",x)
def fun1(a=15):
    x=10
    print("2. x =",x)
    return a
print("3. x=",x)
def fun2():
    x=20
    print("4. x=",x)
print("5. x=",x)
fun1()
fun2()
print("6. x=",x)





#hata ayıklama

try :
    a=int("a")
except:
    print("hatalı veri girişi")




try:
    print(x)
except NameError:
    print("x tanımlanmamış")
except :
    print("başka bir hata meydana geldi")



try:
    print("merhaba")
except:
    print("bir şeyler ters gitti")
else:
    print("herhangi bir hata yok")




try:
    print(x)
except:
    print("bir hata bulundu")
finally:
    print("'try except' sona erdi")




try:
    f=open("demofile.txt","a")
    f.write("lorum ıpsum")
except:
    print("dosyaya yazarken hata ile karşılaşıldı")
finally:
    f.close()



x=-1
if x<0:
 raise Exception("üzgünüm,sıfırdan kuçuk olamaz")


x="hello"
if not type(x) is int:
 raise TypeError("sadece sayılara izin verilir")

"""







