# print("sinan")
# print("sinan", "başaran", "T", "B", "M", sep='.')

# a = "ali"
# b = 5
# print(type(a))  # <class 'str'>
# print(type(b))  # <class 'int'>

# a = 5  # integer veri tipi
# b = "sinan"  # string veri tipi
# c = 3.5  # float veri tipi
# d = 'k'  # karakter veri tipi

# liste1 = [1, 3, 3, 5, 4, 5, 4, "ali", "canan"]
# print(liste1[0])  # ilk elemanı alır
# print(len(liste1))  # eleman sayısını verir
# print(dir(liste1))  # listeye ait fonksiyonları listeler
# liste1[0] = 100000  # mutable, elemanı değiştirebilirsiniz
# print(liste1)
# liste1.append(25)  # yeni eleman ekler
# liste1.insert(7, "25")  # belirtilen index'e yeni eleman ekler

# demet = ("ali", "ayşe")
# print(demet[0])  # ilk elemanı alır
# print(len(demet))  # eleman sayısını verir
# print(demet.count("ali"))  # "ali" elemanının sayısını verir

# def topla(deger, deger2):
#     print("{}, {} degerlerini alır".format(deger, deger2))

# topla(5, 3)

# def selam(isim):
#     print(f"Selam, {isim}!")

# selam("sinan")


# def topla(a, b):
#     return a + b

# result = topla(3, 5)
# print(result)

# a = int(input("1. sayıyı giriniz: "))
# b = int(input("2. sayıyı giriniz: "))

# def cikar(x, y):
#     return x - y

# def kareal(x):
#     return x * x

# sonuc = cikar(a, b)
# print("Çıkarma işlemi sonucu:", sonuc)
# print("Kare:", kareal(a))


# kare = lambda x: x * x
# print(kare(5))

# toplama = lambda x, y: x + y
# print(toplama(3, 4))


# import math
# print(math.sqrt(16))  # karekök alır
# print(math.pow(2, 3))  # 2'nin 3. kuvveti
# print(math.sin(math.radians(60)))  # 60 dereceyi sinüs olarak verir

# import time
# print("Başlangıç")
# time.sleep(2)  # 2 saniye bekler
# print("Bitti")

# import random
# rastgele = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı üretir
# print(rastgele)

# import random
# import time

# rastgele = random.randint(1, 100)
# tahmin = 0

# while True:
#     tahmin = int(input("Tahmin gir (1-100 arası): "))
#     print("Kontrol ediliyor...")

#     if tahmin == rastgele:
#         print("Tebrikler, doğru tahmin ettiniz!")
#         break
#     elif tahmin < rastgele:
#         print("Sayıyı büyült!")
#     elif tahmin > rastgele:
#         print("Sayıyı küçült!")
#     else:
#         print("Lütfen 1-100 arasında bir değer giriniz.")
    
#     time.sleep(1)  # 1 saniye bekler

#     if tahmin == 0:
#         print("Hak bitti!")
#         break


#  class Araba:
#      # __init__ metodu, Araba sınıfından bir nesne oluşturulduğunda çalışır
#      # Bu metot marka ve model bilgilerini alır ve sınıfın özelliklerine (self.marka, self.model) atar
#      def __init__(self, marka, model):
#          self.marka = marka  # Nesnenin marka özelliğini tanımlar
#          self.model = model  # Nesnenin model özelliğini tanımlar

#      # bilgileri_yazdir metodu, Araba nesnesinin marka ve model bilgisini ekrana yazdırır
#      def bilgileri_yazdir(self):
#         print(f"Marka: {self.marka}, Model: {self.model}")  # Marka ve model bilgilerini yazdırır

#  # Araba sınıfından araba1 nesnesini oluşturuyoruz, marka: Toyota, model: Corolla
# araba1 = Araba("Toyota", "Corolla")
#  # araba1 nesnesinin bilgilerini yazdırıyoruz
#  araba1.bilgileri_yazdir()

class Dikdortgen:
    # __init__ metodu, dikdörtgenin genişlik ve yükseklik bilgilerini alır
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik  # Genişlik özelliğini tanımlar
        self.yukseklik = yukseklik  # Yükseklik özelliğini tanımlar

    # alan_hesapla metodu, dikdörtgenin alanını hesaplar ve döndürür
    def alan_hesapla(self):
        return self.genislik * self.yukseklik  # Alan, genişlik ve yükseklik çarpımıdır

# Dikdörtgen sınıfından dikdörtgen1 nesnesi oluşturuyoruz
dikdortgen1 = Dikdortgen(5, 10)
# Alanı hesaplayıp yazdırıyoruz
alan = dikdortgen1.alan_hesapla()
print(f"Dikdörtgenin alanı: {alan}")
