from imageai.Classification import ImageClassification #imports the imageAI image prediciton class and 
import os                                #python os class
execution_path = os.getcwd()    # create a variable which holds the reference to path containing py file
prediction = ImageClassification()
prediction.aetModelTypeAsResNet50()
prediction.setModelPath( execution_path + "\resnet50_imagenet_tf.2.0.h5")
#creation of instance ImagePrediction() class from first line
#set model type of prediciton object to resnet by calling setmodeltype as res net() in the second line
#then set model path of the prediction object to the path of model file
        #(resnet50_weight_tf_dim_ordering_tf_kernels.h5)

prediction.loadModel()


predictions, percentage_probabilities = prediction.classifyImage("C:\Users\MyUser\Downloads\sample.jpg", result_count=5)
#define 2 variables to be equal to the function called to predict an image
# we parsed the path to our image and also state the number of prediction results we want 
#to have (values from 1 to 1000) parsing result_count =5
#classify image() function will return 2 array objects with the first predictions 
# being an array of the corresponding precentage probability for each prediciton
for index in range(len(predictions)):
    print(predictions[index], ":" , percentage_probabilities[index])
#contains each object in the prediction array, and also obtains corresponding percentage 
# probability from the percetage prob..., and finally prints result of both to console