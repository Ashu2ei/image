# Image-Recognition-CIFAR-10
Image Recognition using CIFAR-10 dataset
<br/>
![Dataset CIFAR](https://github.com/sidvsukhi/Image-Recognition-CIFAR-10/blob/master/dataset.png)
<br/>
How to use this repository?
1. load_cifar.py- It is the model training file which consists of dataset split, normalization, developing neural network, training and storing the structure as well as the weights in json format.
<br/>
This is the neural network model that is built.
<br/>
![Model summary](https://github.com/sidvsukhi/Image-Recognition-CIFAR-10/blob/master/summary.PNG)
<br/>
2. use_cifar.py- It is the file that uses the stored neural network structure and weights to predict.
<br/>
![Test image](https://github.com/sidvsukhi/Image-Recognition-CIFAR-10/blob/master/frog.jpg)
<br/>
3. model_structure.json- It is the stored json file with the trained neural network structure
<br/>
4. model_weights.h5- It has the stored weights of the model.

<br/>
[Medium article](https://medium.com/@siddhantsukhatankar/hello-world-in-image-recognition-136eba581464)
<br/>

#################

pip3 install -r requirements.txt

export MLFLOW_TRACKING_URI="sqlite:///mlruns.db"

python3 model_service.py

mlflow models serve -m models:/SentimentAnalysis/latest -p 5000 --no-conda


curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{"instances":[ "It is a bad day"]}'
                                            or
###################

