def kontrol(info):
    sepal_length = float(info[0])
    sepal_width = float(info[1])
    petal_length = float(info[2])
    petal_width = float(info[3])
    sonuc=""
    if(sepal_length>=4.3 and sepal_length<=5.8 and sepal_width>=2.3 and sepal_width<=4.4 and petal_length>=1.0 and petal_length<=1.9 and petal_width>=0.1 and petal_width<=0.6):
        sonuc = "Iris-setosa"
    elif(sepal_length>=4.9 and sepal_length<=7.0 and sepal_width>=2.0 and sepal_width<=3.3 and petal_length>=3.0 and petal_length<=5.1 and petal_width>=1.0 and petal_width<=1.8):
        sonuc = "Iris-versicolor"
    elif(sepal_length>= 4.9 and sepal_length<=7.9 and sepal_width>=2.2 and sepal_width<=3.8 and petal_length>=4.5 and petal_length<=6.9 and petal_width>=1.4 and petal_width<=2.5):
        sonuc = "Iris-virginica"
    else:
        sonuc="cicek-bulunamadi"
    return sonuc

with open("iris.txt","r") as dosya:
    dogru=0
    yanlis=0
    toplam=0
    for satir in dosya:
        cicek = satir.strip()
        info = cicek.split(",")
        sonuc = kontrol(info)
        toplam+=1
        if (sonuc == info[4]):
            dogru +=1
        else:
            yanlis +=1
    print("Toplam Veri: " + str(toplam))
    print("Toplam Tahmin: "+ str(dogru+yanlis))
    print("Doğru Tahminler: " +str(dogru))
    print("Yanlış Tahminler: " + str(yanlis))
    print("Doğru Tahmin Oranı: %" + str(dogru/(toplam)*100))