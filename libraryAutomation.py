class library:
    def __init__(self,kayıtlar="books.txt"):
        self.kayıtlar=open(kayıtlar,"a+")
    def __del__(self):
        self.kayıtlar.close()
        
    def listBooks(self):
        with open("books.txt","r") as kitap:
            booklist=[]
            for book in kitap.read().splitlines():
                booklist=book.split(",")
                kitapAdı=booklist[0]
                yazarAdı=booklist[1]
                yayınYılı=booklist[2]
                syfSayisi=booklist[3]
                print(f"Kitabın Adı: {kitapAdı} - Yazarı: {yazarAdı} - Yayın Yılı: {yayınYılı} - Sayfa Sayısı: {syfSayisi}")
        
    def addBook(self):
        with open("books.txt","a+") as kitap:
            kitapAdı=input("Kitabın Adı: ")
            yazarAdı=input("Yazar Adı: ")
            yayınYılı=input("Yayın Yılı: ")
            syfSayisi=input("Sayfa Sayısı: ")
            kitapBilgisi=(f"{kitapAdı},{yazarAdı},{yayınYılı},{syfSayisi}")
            kitap.write(str(kitapBilgisi)+"\n")

    def removeBook(self):
        books=library()
        books.listBooks()
        with open("books.txt","r+") as kitap:
            bookName=input("Silinecek Kitabın ismi: ")
            booklist=[]
            kitaplar=[]
            for book in kitap:
                booklist=book.strip().split(",")
                kitapAdı=booklist[0]
                yazarAdı=booklist[1]
                yayınYılı=booklist[2]
                syfSayisi=booklist[3]
                if kitapAdı==bookName:
                    bookName=(f"{kitapAdı},{yazarAdı},{yayınYılı},{syfSayisi}")
                else:
                    kitaplar.append(book)
        
            with open("books.txt","w") as kitap2:
                for kitap in kitaplar:
                    kitap2.write(kitap)


lib=library()

while True:
    secenek=input("***MENU***\n1 - Kitapları Listele\n2 - Kitap Ekle\n3 - Kitabı Kaldır\n4 - Çıkış\n")
    match secenek:
        case "1":
            lib.listBooks()
        case "2":
            lib.addBook()
        case "3":
            lib.removeBook()
        case "4":
            break
