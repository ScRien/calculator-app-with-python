import time
islem = int(input("Dört işlemden birini seçiniz: 1- Toplama, 2- Cıkarma, 3- Çarpma, 4- Bolme \n"))
if islem == 1:
    number1 = int(input("1.Sayıyı giriniz: "))
    number2 = int(input("2.Sayıyı giriniz: "))
    number3 = int(input("3.Sayıyı giriniz: "))
    number4 = int(input("4.Sayıyı giriniz: "))
    number5 = int(input("5.Sayıyı giriniz: "))
    if number1 != "" or number2 != "" or number3 != "" or number4 != "" or number5 != "":
        print("Sonuç: {}".format(number1 + number2 + number3 + number4 + number5
        time.sleep(5)
    else:
        print("Tüm alanları Doldurun!")
        time.sleep(5)
#--------------------------------------------------------------------------------------------------------------
if islem == 2:
    number1 = int(input("1.Sayıyı giriniz: "))
    number2 = int(input("2.Sayıyı giriniz: "))
    number3 = int(input("3.Sayıyı giriniz: "))
    number4 = int(input("4.Sayıyı giriniz: "))
    number5 = int(input("5.Sayıyı giriniz: "))
    if number2 != "" or number2 != "" or number3 != "" or number4 != "" or number5 != "":
        print("Sonuç: {}".format(number1 - number2 - number3 - number4 - number5))
        time.sleep(5)
    else:
        print("Tüm alanları Doldurun!")
        time.sleep(5)
#--------------------------------------------------------------------------------------------------------------
if islem == 3:
    number1 = int(input("1.Sayıyı giriniz: "))
    number2 = int(input("2.Sayıyı giriniz: "))
    number3 = int(input("3.Sayıyı giriniz: "))
    number4 = int(input("4.Sayıyı giriniz: "))
    number5 = int(input("5.Sayıyı giriniz: "))
    if number1 != "" or number2 != "" or number3 != "" or number4 != "" or number5 !=   "":
        print("Sonuç: {}".format(number1 + number2 * number3 * number4 * number5))
        time.sleep(5)
    else:
      print("Tüm alanları Doldurun!")
      time.sleep(5)
#--------------------------------------------------------------------------------------------------------------
if islem == 4:
    number1 = int(input("1.Sayıyı giriniz: "))
    number2 = int(input("2.Sayıyı giriniz: "))
    number3 = int(input("3.Sayıyı giriniz: "))
    number4 = int(input("4.Sayıyı giriniz: "))
    number5 = int(input("5.Sayıyı giriniz: "))
    if number1 != "" or number2 != "" or number3 != "" or number4 != "" or number5 != "":
        print("Sonuç: {}".format(number1 / number2 / number3 / number4 / number5))
        time.sleep(5)
    else:
        print("Tüm alanları Doldurun!")
        time.sleep(5)
