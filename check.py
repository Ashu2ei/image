# from PIL import Image
# image = Image.open('frog.jpg')
import numpy
# import json
# numpydata = numpy.array(image)
# json_object = json.dumps(str(numpydata), indent=4)
# with open("sample.json", "w") as outfile:
#     outfile.write(str(numpydata))



from keras.utils import image_utils
img=image_utils.load_img("frog.jpg",target_size=(32,32))
image_to_test=image_utils.img_to_array(img)/255
for data in image_to_test:
    print(data)
# list_of_images=numpy.expand_dims(image_to_test,axis=0)
# with open("sample.json", "w") as outfile:
#     outfile.write(str(image_to_test))