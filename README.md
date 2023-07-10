# ObjectDetection-NesneTanima

Merhaba,

Bu projede amaç makinenin Yolov5 algoritması kullanılarak görsellerle eğitilmesi ve eğitim sonucunda makinenin test görüntülerindeki nesneyi tanıması hedeflenmiştir.

Alınan sonuçlar, algoritmanın etiketlediği test görselleri ile birlikte tüm algoritma çıktısı repo içerisinde bulunmaktadır.

## Projenin çalışabilmesi için:
- Görsel ve bu görsellerin etiketlerinin konumlarını barındıran .txt uzantılı verilerinizi tutan dosyanızı yolov5 formatına çevirmelisiniz.
  
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/40a86e96-b375-428c-a8d6-23f4e5247dec)
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/4341a297-2852-48a3-b474-e06f9bd582fc)
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/cf1465b2-6ae6-4608-9d26-205f37b3823e)
- Çevirme işleminin ardından aşağıdaki formatı elde edeceksiniz.
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/a8b4a1e3-693b-4575-96f4-e59adc07c313)
- Her model içerisinde dosya yollarını oluşturduğunuz veri setinin yoluna göre düzenlemelisiniz.
- Github üzerinden yolov5 algoritmasını edinmelisiniz.
- Bu gereklilikleri sağlayıp istenilen modelden sonuç alabilirsiniz.

--------------------------------------------------------------------------------
Hello,

The aim of this project is to train the machine with visuals using the Yolov5 algorithm, and as a result of the training, the machine will recognize the object in the test images.

The results, along with the test images tagged by the algorithm, are included in the repository as the output of the entire algorithm.

## To make the project work:
- You need to convert your files that contain the images and the positions of their labels in .txt format to the yolov5 format.

 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/40a86e96-b375-428c-a8d6-23f4e5247dec)
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/4341a297-2852-48a3-b474-e06f9bd582fc)
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/cf1465b2-6ae6-4608-9d26-205f37b3823e)

- After the conversion process, you will obtain the following format.
 ![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/a8b4a1e3-693b-4575-96f4-e59adc07c313)
- You should adjust the file paths within each model according to the path of your created dataset.
- You need to obtain the yolov5 algorithm from Github.
- Once you fulfill these requirements, you can obtain results from the desired model.


## Kullanılan Kaynaklar - Utilized resources
- [Yolov5 algoritması](https://github.com/ultralytics/yolov5)
- [Veriseti dönüştürme - Dataset conversion](https://github.com/RapidAI/YOLO2COCO)
- [Etiketli Google görsel verisi - Tagged google image data](https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=segmentation&r=false&c=%2Fm%2F0h8my_4)


## Sonuçlar
Bu projede 60 eğitim 20 test görseli kullanılarak işlem yapılmıştır.
Elde bulunan verilerin sayısıyla doğru orantılı şekilde modelleri eğitme ve sonuç alma süresi artmaktadır. Modelin eğitim süreci arttıkça nesneleri tanıma oranı da artıyor.
Etiketlerin bilgisini vermeden sadece fotoğraflar ile eğittikten sonra, test görselini algoritmaya uygulayarak 3 farklı modelde başarı oranının arttığını gözlemleyebiliyoruz. 

Sırasıla
**Model L, Model M, Model S**

![image](https://github.com/OzcanFatihCan/ObjectDetection-NesneTanima/assets/93872480/7377e7c5-44ed-4678-a294-ed85b1b319a5)
Etiketleme işleminin ne kadar başarılı olduğunu kontrol etmek için varsayılan etiketlerle karşılaştırabilirsiniz.
