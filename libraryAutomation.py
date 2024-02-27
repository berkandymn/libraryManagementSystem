class library:
    def __init__(self,kayitlar="books.txt"):
        self.kayitlar=open(kayitlar,"a+",encoding="utf-8")
    def __del__(self):
        self.kayitlar.close()
        
    def listBooks(self):
        with open("books.txt","r",encoding="utf-8") as kitap:
            booklist=[]
            for book in kitap.read().splitlines():
                booklist=book.split(",")
                kitapAdi=booklist[0]
                yazarAdi=booklist[1]
                yayinYili=booklist[2]
                syfSayisi=booklist[3]
                print(f"Kitap: {kitapAdi} - {yazarAdi} - {yayinYili} - {syfSayisi}")
        
    def addBook(self):
        with open("books.txt","a+",encoding="utf-8") as kitap:
            kitapAdi=input("Kitabın Adını Giriniz: ")
            yazarAdi=input("Yazar Adını Giriniz: ")
            yayinYili=input("Yayın Yılını Giriniz: ")
            syfSayisi=input("Sayfa Sayısını Giriniz: ")
            kitapBilgisi=(f"{kitapAdi},{yazarAdi},{yayinYili},{syfSayisi}")
            kitap.write(str(kitapBilgisi)+"\n")

    def removeBook(self):
        silinecek=False
        books=library()
        books.listBooks()
        with open("books.txt","r+",encoding="utf-8") as kitap:
            bookName=input("Silinecek Kitabın ismi: ")
            booklist=[]
            kitaplar=[]
            for book in kitap:
                booklist=book.strip().split(",")
                kitapAdi=booklist[0]
                yazarAdi=booklist[1]
                yayinYili=booklist[2]
                syfSayisi=booklist[3]
                if kitapAdi==bookName:
                    bookName=(f"{kitapAdi},{yazarAdi},{yayinYili},{syfSayisi}")
                    silinecek=True
                else:
                    kitaplar.append(book)
            if silinecek==True:
                print("\n"+bookName+" Silindi")
            elif silinecek==False:
                print("\n"+"Silinecek Kitap Bulunamadı.")
                        
            with open("books.txt","w",encoding="utf-8") as kitap2:
                for kitap in kitaplar:
                    kitap2.write(kitap)

lib=library()

while True:
    secenek=input("\n***MENU***\n1 - Kitapları Listele\n2 - Kitap Ekle\n3 - Kitabı Kaldır\n4 - Çıkış\n")
    if secenek=="1":
        lib.listBooks()
    elif secenek=="2":
        lib.addBook()
    elif secenek=="3":
        lib.removeBook()
    elif secenek=="4":
        break