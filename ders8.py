#oop nin temel amacı bir veri tipi modeli oluşturmaktır.
""""
class Ogrenci:
    ad="alpii"
    def selamlama(self):
        print("merhaba")

ogr1=Ogrenci()
print(type(ogr1))
ogr1.ad="alperen"
print(ogr1.ad)
ogr1.selamlama()

ogr2=Ogrenci()
print(type(ogr2))
ogr2.ad="emine"
print(ogr2.ad)

ogr3=Ogrenci()
print(ogr3.ad)


class Kullanıcı:
    isi="mühendis"
    def __init__(self):
        self.ad="alpi"
        self.soyad="akal"

k1=Kullanıcı()
print(k1.ad)
print(k1.isi)
print(Kullanıcı.isi)






class Kullanıcı:
    isi="mühendis"
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
    def tamAd(self):
        tamİsim=self.ad+self.soyad
        return tamİsim

k1=Kullanıcı("alperen","akal")
print(k1.ad)
print(k1.tamAd())





class Calisan:

    sirket="Elektrovizyon"
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.eposta=self.f_eposta()

    def f_eposta(self):
        return self.ad+self.soyad+"@sirket.com"
    @classmethod
    def pi(cls):
        return 3.14
    

print(Calisan.sirket)
calisan1=Calisan("Ege","Can",40000)
print(calisan1.ad)
calisan1.maas*=1.5
print(calisan1.maas)

print(calisan1.eposta)
print(calisan1.pi())
print(Calisan.pi())







class Calisan:
    zam_oranı = 1.05
    perSayisi=0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.perSayisi+=1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)
    def arttir(self):
        # self.maas = (self.maas*1.05)#classtaki şirketin zam oranı üzerinden belirlenir
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)#calisanın zam oranı üzerinden hesaplanır

print(Calisan.perSayisi)
calisan1=Calisan("alperen","akal",70000)
print(Calisan.perSayisi)
print(calisan1.tamad())
print(calisan1.maas)
calisan1.arttir()
print(calisan1.maas)
calisan2=Calisan("emine","aydınlı",70000)
print(Calisan.perSayisi)


#nesne üzerinde-->@objectmethod
#sınıf üzerinden--->@classmethod
#sınıf dışından da--->@staticmethod







class Calisan:

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

    @classmethod
    def zam_orani_degis(cls,yeni_oran):
        cls.zam_oranı = yeni_oran

    @classmethod
    def ypersonel(cls,pbilgisi):           #yeni personel üretmiş olduk.yapıcı metoda alternatiftir
        ad, soyad, maas = pbilgisi.split("-")
        return cls(ad,soyad,maas)

    @staticmethod
    def tel_no(telefon):
        return telefon.split(" ")
    

print(Calisan.tel_no("537 486 50 25"))
per1=Calisan("alperen","akal",2000)
per2=Calisan("emine","aydınlı",2000)
per1.arttir()
print(per1.maas)
print(per1.zam_oranı)
Calisan.zam_orani_degis(1.2)
print(per1.zam_oranı)
print(per2.zam_oranı)
print(Calisan.zam_oranı)

mpersonel1="hacer-aydınlı-5000"
yeniPer=Calisan.ypersonel(mpersonel1)







class Calisan():

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

class Gelistirici(Calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        Calisan.__init__(self,ad,soyad,maas)
        #super().__init__(ad,soyad,maas)
        self.p_dili = p_dili
        self.zam_oranı = 1.2

class yonetici(Calisan):
    def __init__(self,ad,soyad,maas,calisanlar = None):
        super().__init__(ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def eleman_ekle(self,eleman):
        self.calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.calisanlar.remove(eleman)

    def calisan_listele(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())

personel1=Calisan("e","a",2)
personel2=Calisan("a","e",3)
gel1=Gelistirici("alperen","akal",3000,"python")
print(gel1.tamad(),gel1.p_dili,gel1.maas)
gel1.arttir()
print(gel1.maas)
yonet1=yonetici("ali","veli",7000,[gel1,personel1])
print(yonet1.calisan_listele)
yonet1.eleman_ekle(personel2)
print(yonet1.calisan_listele)
yonet1.eleman_cikar
print(yonet1.calisan_listele)



print(issubclass(personel2,yonetici))
print(issubclass(Calisan,yonetici))
print(issubclass(Gelistirici,Calisan))







# program to illustrate access modifiers of a class

# super class
class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
print(obj.__var3)



"""





class Ogrenci():
    def __init__(self, ad, soyad):
        self.adi = ad
        self.soyad = soyad


class Fogrencisi(Ogrenci):
    def __init__(self, ad, soyad, fakulte):
        Ogrenci.__init__(self, ad, soyad)
        self.fakulte = fakulte


class BOgrencisi(Fogrencisi):
    def __init__(self, ad, soyad, fakulte, bolum):
        # Fogrencisi.__init__(self, ad, soyad, fakulte)
        super().__init__(ad, soyad, fakulte)
        self.bolum = bolum


genel_ogrenci = Ogrenci("ali", "veli")
print(genel_ogrenci.adi, genel_ogrenci.soyad)

fakulte_ogrencisi = Fogrencisi("Uğur", "YERSEL", "Mühendislik")
print(fakulte_ogrencisi.fakulte)

bolum_ogrencisi = BOgrencisi("Uğur","YERSEL","Mühendislik","Bilgisayar")
print(bolum_ogrencisi.bolum)







class sporcu():
    def __init__(self,ad,brans,altin,gumus,bronz):
        self.ad = ad
        self.brans = brans
        self.mbronz = bronz #public veri halka açık değişken
        self._mgumus = gumus #protected yarı gizli
        self.__maltin = altin #private tam gizli
    def atlet_bilgisi(self):
        return "Sporcu adı : {}, Branşı :{}".format(atlet1.ad,atlet1.brans)
    @property
    def a_yazdir(self):
        amadalya = self.__maltin
        return "altın madalya sayısı {}".format(self.__maltin)

atlet1 = sporcu("ali","100 Metre",2,3,9)
print(atlet1.atlet_bilgisi())
print("bronz madalya sayısı",atlet1.mbronz)
print("gümüş madalya sayısı",atlet1._mgumus)
print(atlet1.a_yazdir)