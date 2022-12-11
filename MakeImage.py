import sys
import os
from MyModules.ImageIO import ImageIO
from MyModules.BasicImageProcessing import BasicImageProcessing
from PIL import Image, ImageDraw, ImageFilter


class MakeImage: #絵の画像のサイズ調整と画像のはりつけ

    def imposeSys (self, input_file_path, outputName, result): #額縁に写真を貼り付ける

        #引数resultはテンプレートマッチングで取得した額縁の中身の座標が格納された配列
        #result[0]が左上の座標 result[1]が右上の座標
        #result[0]とresult[1]の中には(x,y) = (x座標,y座標)みたいな情報が入っていて、result[0][0]はresult[0]に格納された座標のx座標、
        #result[0][1]はresult[0]に格納された座標のy座標

        current = os.getcwd() #get the current directory 
        impose_file_path = current + "/" + "resizeImage.jpg" #貼り付ける画像の相対パスの取得
        bip = BasicImageProcessing() #インスタンス化
        iio = ImageIO() #インスタンス化
        input = iio.readImage(input_file_path) #額縁の画像の読み込み
        impose = iio.readImage(impose_file_path) #絵の画像の読み込み
        pasted = bip.imposeImage(input, impose, (result[0][0], result[0][1]))
         #画像の合成 　result[0][0](x座標)、result[0][1](y座標)が左上に来るように絵を貼り付ける
        iio.saveImage(outputName, pasted) #出来た画像の保存

    def resizeSys (self, input, result): #額縁に合うように絵のサイズを変更する　resultはテンプレートマッチングで取得した座標が入った配列

        h = result[1][1]-result[0][1] #高さの計算 　右下の座標のy座標-左上の座標のy座標
        w = result[1][0]-result[0][0] #幅の計算    右下の座標のx座標-左上の座標のx座標

        im = Image.open(input) #絵の画像の読み込み
        resizeIm = im.resize((w,h)) #横幅wに高さhに大きさ変更
        resizeIm.save("resizeImage.jpg") #出来た画像の保存
