# bilgisayarAraProjesi
Erkek Üreme Hücre Morfolojilerinin Derin Öğrenme ile Sınıflandırılması

->Veriseti ve arayüz 1yüksek boyutta olduğu için cloud a yüklenmiştir aşşağıdaki likten ulaşılabilir.
	https://drive.google.com/drive/folders/1JmtY57tSh_rTOv18YqfwpOsPvcAl87oN?usp=sharing

->Verisetleri ve Colab_15011091_16011110.ipynb Google Drive da (Proje) isimli dosyanın altına alınır.
->İstenen modeller Colab_15011091_16011110.ipynb ile Google Colab üzerinde  çalıştırılır.
->Model çalıştırılırken istenen parametreler ayarlanır. Google Drive'dan onay verilir. Modeli eğitmek uzun sürdüğü için Google Colabın kapanmaması için autoclicker ile Google Colab aktif tutulabilir.
->Modelin diskte bulunan .json ve .h5 uzantılı dosyaları indirilerek arayüzün ortamına atılır(Arayüz dosyasında her örnek için bu uzantılar mevcuttur.)
->İndirilen uzantılar VerisetiadıModeladı(.h5-.json) şeklinde kaydedilir.


Arayüzün çalışması için aşağıdaki program ve sınıfların ortamda bulunması gerekmektedir.

->Python version 3.7
Aşağıdaki sınıflar pip install ile powershell veya komut istemcisinden pythona import edilmeli
	import cv2
	import tensorflow as tf
	import os
	import numpy as np
	import matplotlib.pyplot as plt

	import skimage.io as io
	from skimage.transform import resize
	from skimage.io import imread
	import keras
	from keras.metrics import categorical_crossentropy
	from keras.models import model_from_json
	from keras.models import load_model
	from keras.optimizers import SGD, Adam, Adamax
	from keras.preprocessing import image

->PyQt5 Arayüz geliştirici (designer)
Aşağıdaki sınıflar arayüzde bulunmalı.
	from PyQt5 import QtCore, QtGui, QtWidgets
	from PyQt5.QtWidgets import QFileDialog

->Arayüz çalıştırılırken bulunan dizine gidilir powershell üzerinden (python Application.py) komutu ile çalıştırılır.

->Raporu çalıştırmak için https://www.overleaf.com/ üzerinde hesap oluşturulur. .rar uzantılı Latex dosyası sisteme yüklenerek rapor çalıştırılır.
