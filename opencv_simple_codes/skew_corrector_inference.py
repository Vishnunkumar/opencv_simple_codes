import tensorflow as tf
import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt
import joblib

class SkewCorrector:
  
  def __init__(self, model, scaler):
