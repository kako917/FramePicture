import os
import sys
from MyModules.ObjectDetectionUsingTemplateMatching import ObjectDetectionUsingTemplateMatching
from MyModules.ImageIO import ImageIO
from TmpSys import TmpSys
from MakeImage import MakeImage
# ***************************************
#START THE MAIN METHOD
# ***************************************
if __name__=="__main__":

    #Read the file name to be processed from the command-line arguments
    args = sys.argv   
    inputName = args[1] #額縁の画像のファイル名
    outputName = args[2] #出力する画像ファイルの名前
    templateName = args[3] #額縁のテンプレートの画像名
    imposeName = args[4] #貼り付けたい絵のファイル名
    
    # 画像の読み込み + グレースケール化
    # convert the received filenames into their file paths, respectrively
    current = os.getcwd() #get the current directory
    input_image = './' + inputName
    template_image = './' + templateName
    impose_image = './' + imposeName
    impose_file_path = current + "/" + imposeName
    input_file_path = current + "/" + inputName

    #Instantiate four classes, BasicImageProcessing, ObjectDetectionUsingTemplateMatching, ImageIO, and VideoIO
    odtm = ObjectDetectionUsingTemplateMatching()
    iio = ImageIO()
    
    tmpSys = TmpSys() #インスタンス化
    result = tmpSys.tmpSys(input_image, template_image) #resultにはテンプレートマッチングで取得した額縁の中身の座標が格納されている

   
    makeImage = MakeImage() #インスタンス化
    makeImage.resizeSys(impose_image, result) 
    makeImage.imposeSys(input_file_path, outputName, result)
    