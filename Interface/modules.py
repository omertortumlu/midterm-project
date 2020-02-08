
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

# gelen modelin hangi optimizer da iyi olduğunu öğren modeli compile etmek için


def test_model(dataset, model, directory):

    if(len(directory) > 0):
        img_size = 0
        classes = []
        opt = ''
        # Datasete göre resmin boyutu hesaplandı
        if(dataset == 'HuSHeM'):
            img_size = 131
            classes = ['Normal', 'Tapered', 'Pyriform', 'Amorphous']
            if(model == 'GoogleNet'):  # 1.durum için
                opt = 'sgd'
            elif(model == 'MobileNet'):  # 2.durum için
                opt = 'adamax'
            else:  # 3.durum için
                opt = 'adam'
        else:
            img_size = 170
            classes = ['Abnormal', 'Boya', 'Sperm']
            if(model == 'GoogleNet'):  # 4.durum için
                opt = 'adamax'
            elif(model == 'MobileNet'):  # 5.durum için
                opt = 'sgd'
            else:  # 6.durum için
                opt = 'adamax'

        # Json yükleniyor
        json_file = open(dataset+model+'.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()

        # Model oluşturuluyor
        loaded_model = model_from_json(loaded_model_json)

        # Modelin ağırlıkları yükleniyor
        loaded_model.load_weights(dataset+model+'.h5')

        # Yeni model compile ediliyor
        loaded_model.compile(loss="categorical_crossentropy",
                             optimizer=opt, metrics=['accuracy'])

        # Resim okunuyor...
        img = io.imread(directory)
        img = resize(img, (img_size, img_size, 3), anti_aliasing=True)
        image = np.asarray(img)
        image = np.expand_dims(image, axis=0)

        # Resim test ediliyor
        pred = loaded_model.predict(image)

        # En yüksek değere sahip sınıf
        y_pred = np.argmax(pred)

        # pred[count] şekline sokuluyor
        pred.shape = (len(classes), 1)

        # Sınıflarıyla birlikte text e çevriliyor
        text = ""
        x = 0.0
        for n in range(len(pred)):
            x += pred[n]
        for n in range(len(pred)):
            text += (classes[n]+str((pred[n]/x)*100)+'%\n')

        return text, classes[y_pred]
    else:
        return "Lütfen image yolunu belirtiniz", "Null"
