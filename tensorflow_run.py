
import tensorflow_core as tensorflow_core 
from dbmanager import DBManager

def tensor_run():
  nl = tensorflow_core.NodeLookup()
  tensorflow_core.set_ImagePath(ImagePath)
  re,sc =tensorflow_core.main(nl)
  print(re)
  print(sc)
  return re, sc


def Image_set():
  global ImagePath
  path_file = open("path.txt","r")
  ImagePath = path_file.readline()
  ImagePath = ImagePath.rstrip()
  path_file.close()

def Insert_db(result,score):
  dbManager = DBManager()
  dbManager.data_insert(ImagePath,result,score)

if __name__ == '__main__':
  Image_set()
  result,score = tensor_run()
  Insert_db(result,score)

