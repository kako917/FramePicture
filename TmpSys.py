import os
import cv2
import numpy as np

class TmpSys:

    def tmpSys (self, input, template):
    #args = sys.argv   
    #inputName = args[1]
    #templateName = args[2]

    # 画像の読み込み + グレースケール化
    # convert the received filenames into their file paths, respectrively
    #current = os.getcwd() #get the current directory
    #input_image_path =current+"/"+inputName #input file path
      input_image = cv2.imread(input)
      input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    #output_video_path =current+"/"+outputName #output file path
   # template_path = current+"/"+templateName #template file path
      template = cv2.imread(template)
      template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    # 処理対象画像に対して、テンプレート画像との類似度を算出する
      res = cv2.matchTemplate(input_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # 類似度の高い部分を検出する
      threshold = 0.8
      loc = np.where(res >= threshold)

    # テンプレートマッチング画像の高さ、幅を取得する
      h, w = template_gray.shape

    # 検出した部分に赤枠をつける
      for pt in zip(*loc[::-1]):
          cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

   # 画像の保存
      cv2.imwrite('tempImage.jpg', input_image)

      return pt, (pt[0] + w, pt[1] + h)

