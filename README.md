# Bilgisayar Ara Projesi
Erkek Üreme Hücre Morfolojilerinin Derin Öğrenme ile Sınıflandırılması

>Veriseti ve arayüz büyük boyutta olduğu için drive a yüklenmiştir <a href="https://drive.google.com/drive/folders/1JmtY57tSh_rTOv18YqfwpOsPvcAl87oN?usp=sharing" target="_blank">Link</a> 'ten ulaşılabilir.


>Verisetleri ve Colab_15011091_16011110.ipynb Google Drive da (Proje) isimli dosyanın altına alınır.

>İstenen modeller Colab_15011091_16011110.ipynb ile Google Colab üzerinde  çalıştırılır.

>Model çalıştırılırken istenen parametreler ayarlanır. Google Drive'dan onay verilir. Modeli eğitmek uzun sürdüğü için Google Colabın kapanmaması için autoclicker ile Google Colab aktif tutulabilir.

>Modelin diskte bulunan .json ve .h5 uzantılı dosyaları indirilerek arayüzün ortamına atılır(Arayüz dosyasında her örnek için bu uzantılar mevcuttur.)

>İndirilen uzantılar VerisetiadıModeladı(.h5-.json) şeklinde kaydedilir.


Arayüzün çalışması için aşağıdaki program ve sınıfların ortamda bulunması gerekmektedir.

->Python version 3.7
Aşağıdaki sınıflar pip install ile powershell veya komut istemcisinden pythona import edilmeli
	
	import cv2
	import tensorflow as tf
	import os
	import numpy as np
	import matplotlib.pyplot as plt
	import skimage.io as io
	import keras


PyQt5 Arayüz geliştirici (designer)
Aşağıdaki sınıflar arayüzde bulunmalı.

>from PyQt5 import QtCore, QtGui, QtWidgets

>from PyQt5.QtWidgets import QFileDialog
<p align="center">

  <img src="https://github.com/omertortumlu/Midterm-Project/blob/master/firstpage.png" title="Uygulama Arayüzü" alt="accessibility text">
</p>

### 1.Adım
Bu adımda, veriseti ve bu verisetinde çalışılmış olan ağın en başarılısı seçilmiştir. Arayüzde seçilen ağın veriseti ile en başarılı olduğu parametrelerde colab’da test yapılmış ve confusion matrisi ve model ağırlıkları çıkartılmıştır. Yapılan seçim ile model ağırlıkları yüklenip, confusion matrisi kullanıcıya gösterilmektedir.

### 2.Adım
Bu adımda test edilmek istenen fotograf kullanıcı tarafından dosya yolu 
girilerek veya browse butonuna basarak seçilir load test image butonuyla seçilen
fotoğraf yüklenir. Model de test edilebilmesi için görüntünün yüklenen model boyutlarına 
dönüştürülmesi gerekmektedir. HuSHeM veri seti için 131x131, 
SMIDS veri seti içinde 170x170 boyutlarına dönüştürülmelidir.

### 3.Adım
Bu adımda yüklenen fotoğraf test edilir. Veriseti için bulunan sınıf benzerlik sonuçları 
text kutusuna yazılır. En yüksek sonuç görüntünün en yakın olduğu sınıftır soru işaretli
bölüme prediction sonucu yazılır.

