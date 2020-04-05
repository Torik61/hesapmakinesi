z = 0

print("Üslü sayı hesap makinesine hoşgeldiniz.")

while z < 3 :

    x = input("Taban: ")
    y = input("Üs: ")
        
        #print(type(x))
        #print(type(y))


    try:
        sonuc = (float(x) ** float(y))
        print("Sonuc: " + str(sonuc))
        z = 5
    except:
        print("Lütfen sayı giriniz.")
        z = z + 1 

    if int(z) == 3:
        print("3 Kere hata yaptınız. Program kapatılıyor.")      
