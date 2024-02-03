"""
import os
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)
#dosya varlık durumuna göre True ve ya False değeri dönderir
if dosya_mevcut:
    vt = sql.connect(veritabani)
    imlec = vt.cursor()
else:
    print("veri tabanı yoktur")

imlec.execute("SELECT * FROM kitap_bilgisi")
#imlec.execute("SELECT kitap_adi ,kitap_yazari,begeni,FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
# print(kitaplar[0])
# print(kitaplar[9])
a=1
for i in kitaplar:
    #print(i)
    print(a," ",end="")
    for k in i:
        print(k,end=" ")
    print("")
    a=a+1
vt.close()




import os
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("DELETE FROM kitap_bilgisi WHERE okunma_durumu='hayır'")
vt.commit()
imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")
vt.commit()
vt.close()





import os
import sqlite3 as sql
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()


imlec.execute("UPDATE kitap_bilgisi SET begeni = '****' WHERE begeni='***'")
imlec.execute("UPDATE kitap_bilgisi SET okunma_durumu = 'evet' WHERE okunma_durumu = 'hayır'")
vt.commit()

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")

vt.close() 





# veritabanı oluşturmak
#sqlite3 modülünü dahil ediyoruz
import sqlite3 as sql
vt = sql.connect('kitaplik.sqlite') # bağlanacak olduğumuz veri tabanının adını
# yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda
# bir veri tabanı oluşturuluyor
imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz
imlec.execute("CREATE TABLE IF NOT EXISTS ozel (kitap_id INTEGER PRIMARY KEY  "
              "AUTOINCREMENT, kitap_adi ,kitap_yazari,okunma_durumu,begeni)")
#kitap bilgisi adında içerisine bir tablşo oluşturuyoruz ilgili alanlar ile birlikte
# hata almamak için IF NOT EXISTS varlık kontrolü
kitap_girisi = ("INSERT INTO ozel (kitap_adi,kitap_yazari,okunma_durumu,begeni) "
                "VALUES ('Suç ve Ceza', 'Dostoyevski', 'evet','*****')")
kitap_girisi_2=("INSERT INTO ozel (kitap_adi,kitap_yazari,okunma_durumu,begeni) "
                "VALUES ('Beyaz Diş', 'Jack LONDON', 'evet','***')")
imlec.execute(kitap_girisi)
imlec.execute(kitap_girisi_2)
vt.commit() # veri tabanına hafızadaki bilgiyi kaydetmek için
vt.close() # veri tabanını kapatmak için








import sqlite3 as sql
vt = sql.connect('kitaplik_db.sqlite')
imlec = vt.cursor()

def ekle(kitap_adi="",kitap_yazari="",okunma_durumu="",begeni=""):
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplik_tb (kitap_id INTEGER PRIMARY KEY  AUTOINCREMENT, kitap_adi,kitap_yazari,okunma_durumu,begeni)")
#    print(kitap_adi,kitap_yazari,okunma_durumu,begeni)
    kitap_girisi = "INSERT INTO kitaplik_tb (kitap_adi,kitap_yazari,okunma_durumu,begeni) VALUES ('"+kitap_adi+"','"+kitap_yazari+"','"+okunma_durumu+"','"+begeni+"')"
#    print(kitap_girisi)
    imlec.execute(kitap_girisi)
    vt.commit()
def listele():
    imlec.execute("SELECT * FROM kitaplik_tb")
    kitaplar = imlec.fetchall()
#    print(kitaplar)
    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")

def guncelle(guncellenecek):
    gkitap = input("Güncel kitap adını giriniz")
    gyazar = input("Güncel kitap yazarını")
    gokunma = input("Güncel kitap okunma durumunu giriniz")
    gbegeni = input("Güncel kitap beğeni değerini giriniz")
    guncelleme_kodu = "UPDATE kitaplik_tb SET kitap_adi='"+gkitap+"',kitap_yazari='"+gyazar+"',okunma_durumu='"+gokunma+"',begeni='"+gbegeni+"' WHERE kitap_id = '"+guncellenecek+"'"
    imlec.execute(guncelleme_kodu)
    vt.commit()
def sil(silinecek):
    silme_kodu="DELETE FROM kitaplik_tb WHERE kitap_id='"+silinecek+"'"
    imlec.execute(silme_kodu)
    vt.commit()
def cikis():
    vt.close()
    print("Çıkış Yapıldı İyi Günler")









import sys
import veritabani_06 as baglanti

print("-"*56)
print("-"*10, "Kitaplık Programımıza Hoş Geldiniz", "-"*10)
print("-"*56)
while 1 == 1:
    print("-"*10, "Yapmak istediğiniz işlemi Seçiniz", "-"*10)
    print("-" * 10, "(E)klemek,(L)istelemek,(G)üncellemek,(S)ilmek,(Ç)ıkmak", "-" * 10)
    islem = input()
    if islem == "Ç" or islem == "ç":
        baglanti.cikis()
        sys.exit()
    elif islem == "E" or islem == "e":
        kitap = input("kitap adını giriniz")
        yazar = input("kitap yazarını")
        okunma = input("kitap okunma durumunu giriniz")
        begeni = input("kitap beğeni değerini giriniz")
        baglanti.ekle(kitap, yazar, okunma, begeni)
    elif islem == "L" or islem == "l":
        baglanti.listele()
    elif islem == "G" or islem == "g":
        baglanti.listele()
        guncellenecek = input("güncellemek istediğiniz kitabın id'sini giriniz")
        baglanti.guncelle(guncellenecek)
    elif islem == "S" or islem == "s":
        baglanti.listele()
        silinecek = input("silmek istediğiniz kitabın id'sini giriniz")
        baglanti.sil(silinecek)

      """