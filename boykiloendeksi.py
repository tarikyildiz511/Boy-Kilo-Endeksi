'''kişinin adı kilo boy unu alarak boy-kilo endeksini hesaplayınız
formül : kilo boy indeksinin karesi **
Aşağıdaki tabloya göre kişi hangi duruma girmektedir 
0 => 18.4 Zayıf
18.5 => 24.9 normal
25.0 => 29.9 fazla kilolu
30.0 => 34.9 obez
'''
isim = input("İsminizi giriniz")
boy = float(input("boyunuzu giriniz"))
kilo = float(input("kilonuzu giriniz"))

index = (kilo) / (boy **2)

if  (index >=0)and (index <=18.4):
    print(f"zayıfsınız çünkü boyunuz {boy} kilonuz{kilo} yani boy kilo endeksiniz {index}")
elif (index >=18.5)and (index <= 24.9):
    print(f"normalsiniz çünkü boyunuz {boy} kilonuz {kilo} yani boy kilo endeksiniz {index}")
elif (index >=25.0) and (index <=29.9):
    print(f"fazla kilolusunuz çünkü boyunuz {boy} kilonuz {kilo}yani kilo boy endeksiniz {index}")
elif (index >=29.9)and  (index <= 34.9):
    print(f"obezsiniz çünkü boyunuz {boy} kilonuz{kilo} yani kilo boy endeksiniz {index}")