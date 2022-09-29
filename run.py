import pickletools
import model_service
import pickle
import mlflow
from PIL import Image
import numpy as np
from keras.utils import image_utils
import requests
from mlflow.models.signature import infer_signature
import tensorflow as tf
print('FIRST')

class ModelFunction:

        def __init__(self):
          self.model_service_obj = model_service.MlflowModelService() 

        def store_model(self,pickle_file): #pickle file will be in string format
          print('inside store_model...')
          infile = open(pickle_file,'rb+') #type = _io.BufferedRandom',class io. BufferedRandom 
          #(raw, buffer_size=DEFAULT_BUFFER_SIZE) A buffered binary stream providing higher-level access to a 
          # seekable RawIOBase raw binary stream. It inherits BufferedReader and BufferedWriter . 
          # The constructor creates a reader and writer for a seekable raw stream, given in the first argument.

          model = pickle.load(infile) #load is used to load pickled data from a file-like object

          print('model pickle file loaded....')
          infile.close() #You should always close your files, in some cases, 
          #due to buffering, changes made to a file may not show until you close the file
          self.model_service_obj.saveModel(model,"keras","ImageClassification","preprocess.py")


        def load_model(self):
           self.model = self.model_service_obj.loadModel("ImageClassification","1")
           return self.model

class_labels=[
	"Plane",
	"Car",
	"Bird",
	"Cat",
	"Deer",
	"Dog",
	"Frog",
	"Horse",
	"Horse",
	"Boat",
	"Truck"
]

obj = ModelFunction()
obj.store_model("image_pickle.pkl")
model = obj.load_model()
#print(model.predict(["It is a day"]))
#model.predict(["It is a day"])
# print(model.predict("frog.jpg"))
#img = Image.open("frog.jpg")

# import cv2
# img = cv2.imread('frog.jpg')
# img = cv2.resize(img,(320,240))
# img = np.reshape(img,[1,320,240,3])

# print(model.predict(img))
img=image_utils.load_img("frog.jpg",target_size=(32,32))

#convert img to numpy array
image_to_test=image_utils.img_to_array(img)/255

#image_to_test = tf.convert_to_tensor(image_to_test)
#print(type(image_to_test) , 'typeeeeeeeeeee')

#add dimension

list_of_images=np.expand_dims(image_to_test,axis=0)

#predict

results=model.predict(list_of_images)

#since single image so only first element
single_result=results[0]

#likelihood score of all 10 classes
most_likely_class_index=int(np.argmax(single_result))
class_likelihood=single_result[most_likely_class_index]

#class label of the predicted image
class_label=class_labels[most_likely_class_index]

print("This is image is a {} - Likelihood: {:2f}".format(class_label,class_likelihood))
