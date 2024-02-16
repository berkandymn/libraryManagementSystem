class library:
    def __init__(self,kayıtlar="books.txt"):
        self.kayıtlar=open(kayıtlar,"a+")
    def __del__(self):
        self.kayıtlar.close()
        
    def listBooks(self):
        with open("books.txt","r",encoding="utf-8") as kitap:
            booklist=[]
            for book in kitap.read().splitlines():
                booklist=book.split(",")
                kitapAdı=booklist[0]
                yazarAdı=booklist[1]
                yayınYılı=booklist[2]
                syfSayisi=booklist[3]
                print(f"Kitap: {kitapAdı} - {yazarAdı} - {yayınYılı} - {syfSayisi}")
        
    def addBook(self):
        with open("books.txt","a+") as kitap:
            kitapAdı=input("Kitabın Adını Giriniz: ")
            yazarAdı=input("Yazar Adını Giriniz: ")
            yayınYılı=input("Yayın Yılını Giriniz: ")
            syfSayisi=input("Sayfa Sayısını Giriniz: ")
            kitapBilgisi=(f"{kitapAdı},{yazarAdı},{yayınYılı},{syfSayisi}")
            kitap.write("\n"+str(kitapBilgisi)+"\n")

    def removeBook(self):
        books=library()
        books.listBooks()
        with open("books.txt","r+",encoding="utf-8") as kitap:
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
        
            with open("books.txt","w",encoding="utf-8") as kitap2:
                for kitap in kitaplar:
                    kitap2.write(kitap)

"""def menu(islem):
    if islem==1:
        lib.listBooks()
    elif islem==2:
        lib.addBook()
    elif islem==3
        lib.removeBook()
    elif islem==4:
        break"""
lib=library()

while True:
    secenek=input("\n***MENU***\n1 - Kitapları Listele\n2 - Kitap Ekle\n3 - Kitabı Kaldır\n4 - Çıkış\n")
    match secenek:
        case "1":
            lib.listBooks()
        case "2":
            lib.addBook()
        case "3":
            lib.removeBook()
        case "4":
            break
