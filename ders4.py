#TUPLE-->listeden tek farkı ekleme çıkarma yapamıyoruz.ve [] yerine() kullanılır.
#SET--> sırası yok (index) ve her veriden bir tane var.
#DİC-->
"""
sayi=int(input("bir sayi gir:"))
eb=sayi
ek=sayi
sayilar={sayi}
while len (sayilar)<10:
    sayilar.add(int(input("bir sayi gir:")))
for ksayi in sayilar:
    if eb<ksayi:
        eb=ksayi
    if ek > ksayi:
        ek=ksayi
    sayilar.remove(ksayi)
print ("en büyük",eb)
print("en küçük sayi",ek)



treng={"araba":"car","kırmızı":"red","mavi":"blue"}
print(treng)
print(type(treng))
print(treng.get("araba"))
print(treng["araba"])
print(treng.keys())
print(treng.values())
print(treng.items())
ikililer=treng.items()
print(type(ikililer))
for dd in treng:
    print(dd,treng.get(dd)
    print(treng[dd]))


yemekler ={"çorbalar":{"etli:":["işkembe","kelle paça","tavuk suyu"],
                       "etsiz":["mercimek","ezo gelin"],
                       "sebze":["domates","brokoli"]},
            "kebaplar":{"acılı":["adana","beyti"],
                        "acısız":["urfa","mardin"],
                        "dürümler":["ciğer","adana"]}
}
yemekler["çorbalar"]["etli"].append("kavurma")
#print(yemekler["kebaplar"].keys())
#print(yemekler)
for a in yemekler:
    print(a)
    for b in yemekler[a]:
        print("\t",b)
        for c in yemekler[a][b]:
            print("\t"*2,c)
yemekler.clear()
print(yemekler)



yapılacaklar=[]
while True:
  gorev=input("görevlerinizi yazın
  bittiğinde x e basarak kontrole başlayabilirsin ")
  if gorev.lower()=="x":
    break
  else:
    yapılacaklar.append(gorev)
print(yapılacaklar)

while yapılacaklar!=[]:
  for dd in range(len(yapılacaklar)):
    kontrol=input(f"{yapılacaklar[dd]} görevi bitirdiniz mi?")
    if kontrol.lower()=="evet":
      yapılacaklar.pop(dd)
      break
    print(yapılacaklar)
else:
    print("teşekkürler yapılacaklar listesini bitirdiniz")

    

"""

yapılacaklar ={"sabah":{"ödev":["matematik","fen","türkçe"],
                       "alışveriş":["yemek","giyecek"],},
            "akşam":{"spor":["koşu","karın"],
                    "dil çalışma":["ingilizce","almanca"],
                    "ziyaret":["anne","baba"]}
}
for a in yapılacaklar:
    print(a)
    for b in yapılacaklar[a]:
        print("\t",b)
        for c in yapılacaklar[a][b]:
            print("\t"*2,c)
  


while True:
  kontrol=input("sıradaki görevi bitirdiniz mi?")
  if kontrol=="evet":
    yapılacaklar.pop(0)
    print (yapılacaklar)
  if len(yapılacaklar)==0:
    break
print("teşekkürler yapılacaklar listesini bitirdiniz")


