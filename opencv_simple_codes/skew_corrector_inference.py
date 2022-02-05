import tensorflow as tf
import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt
import joblib

class SkewCorrector:
  
  def __init__(self, model, scaler):

    self.model = model
    self.scaler = scaler
    self.img_path = img_path

  def skew_correction(self):

    self.scaler = joblib.load('sscaler.gz')
    self.model = tf.keras.models.load_model("scaled_model_b_50eps.h5")

    imge = cv2.imread(self.img_path)
    imge = cv2.resize(imge, (img_width, img_height))
    imge = imge.reshape(1, img_height, img_width, 3)
    imge = imge/255
    angle = self.model.predict(imge)
    rt_angle = self.scaler.inverse_transform(angle)[0][0]
    rt_angle = round(rt_angle,0)

    img = PIL.Image.open(fp)
    img2 = img.rotate(rt_angle, expand=True, fillcolor="white")

    return img2