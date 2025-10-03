class İnsan:
    # Yapıcı metod: adı ve yaş bilgilerini alır
    def __init__(self, ad, yas):
        self.ad = ad  # Kişinin adı
        self.yas = yas  # Kişinin yaşı

    # Genel konuşma metodu
    def konus(self):
        print(f"Merhaba, benim adım {self.ad} ve {self.yas} yaşındayım.")

class Hoca(İnsan):  # Hoca sınıfı, İnsan sınıfından miras alır
    # Yapıcı metod, hoca için adı, yaşı ve sicil numarası alır
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)  # İnsan sınıfındaki yapıcıyı çağırır
        self.sicil_no = sicil_no  # Hoca için benzersiz sicil numarası

    # Konus metodunu ezerek farklı bir konuşma yapar
    def konus(self):
        print(f"Merhaba, ben {self.ad} hocanız. {self.yas} yaşımdayım ve sicil numaram: {self.sicil_no}.")
    
    # Ders verme metodu
    def ders_ver(self):
        print(f"{self.ad} hocanız derse başlıyor!")

class Sekreter(İnsan):  # Sekreter sınıfı, İnsan sınıfından miras alır
    # Yapıcı metod, sekreter için adı, yaşı ve telefon numarasını alır
    def __init__(self, ad, yas, telefon_numarasi):
        super().__init__(ad, yas)  # İnsan sınıfındaki yapıcıyı çağırır
        self.telefon_numarasi = telefon_numarasi  # Sekreterin telefon numarası

    # Sekreterin telefon açma metodu
    def telefon_ac(self):
        print(f"{self.ad} sekreteri, {self.telefon_numarasi} numaralı telefondan arama yapıyor.")

class Öğrenci(İnsan):  # Öğrenci sınıfı, İnsan sınıfından miras alır
    # Yapıcı metod, öğrenci için adı, yaşı ve okul numarasını alır
    def __init__(self, ad, yas, okul_numarasi):
        super().__init__(ad, yas)  # İnsan sınıfındaki yapıcıyı çağırır
        self.okul_numarasi = okul_numarasi  # Öğrencinin okul numarası

    # Öğrencinin ders çalışma metodu
    def ders_calismak(self):
        print(f"{self.ad} adlı öğrenci, okul numarası {self.okul_numarasi} ile derse çalışıyor.")

# İnsan sınıfından bir nesne oluşturuyoruz
insan1 = İnsan("Ali", 30)
insan1.konus()

# Hoca sınıfından bir nesne oluşturuyoruz
hoca1 = Hoca("Ahmet", 45, "12345")
hoca1.konus()  # Hoca kendi konuşma metodunu kullanacak
hoca1.ders_ver()

# Sekreter sınıfından bir nesne oluşturuyoruz
sekreter1 = Sekreter("Zeynep", 28, "0555 123 45 67")
sekreter1.konus()  # Sekreter de İnsan sınıfından miras alır
sekreter1.telefon_ac()

# Öğrenci sınıfından bir nesne oluşturuyoruz
ogrenci1 = Öğrenci("Ayşe", 22, "2012001")
ogrenci1.konus()  # Öğrenci de İnsan sınıfından miras alır
ogrenci1.ders_calismak()

