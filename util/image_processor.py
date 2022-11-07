import cv2
import shutil

MAX_DIMENSION = 300

def copyAndCompressPicture(src_path : str, target_path : str):
  shutil.copyfile(src_path, target_path)
  img = cv2.imread(target_path)
  if img.shape[0] > img.shape[1]:
    img = cv2.resize(img, (round(img.shape[1]/img.shape[0]) * MAX_DIMENSION, MAX_DIMENSION))
  else:
    img = cv2.resize(img, (MAX_DIMENSION, round(img.shape[0]/img.shape[1] * MAX_DIMENSION)))
  cv2.imwrite(target_path, img)