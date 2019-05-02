from imageai.Prediction.Custom import CustomImagePrediction
from PIL import Image
import process
import numpy as np
import os
import sys

loc = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(loc, "udang\models\model_ex-003_acc-0.375000.h5"))
prediction.setJsonPath(os.path.join(loc, "predicted.json"))
prediction.loadModel(num_objects=2)

filename = sys.argv[1]
impros = process.process(filename)

predictions, probabilities = prediction.predictImage(impros, result_count=2)
    
print(filename)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
"""
location1 = os.path.join(loc, "udang\test\sehat\\")
location2 = os.path.join(loc, "udang\test\cacat\\")

image_name = []
image_array = []

for r, d, f in os.walk(location1):
    print("in here")
    for file in f:
        print("heey")
        filename = os.path.join(r, file)
        img = process.process(filename)
        
        image_name.push(filename)
        image_array.push(img)
        

for r, d, f in os.walk(location2):
    print("in here2")
    for file in f:
        print("heey2")
        filename = os.path.join(r, file)
        img = process.process(filename)
        
        image_name.push(filename)
        image_array.push(img)

print(image_array)
print("you are here")
for i in range(len(image_array)):
    print("got here")
    predictions, probabilities = prediction.predictImage(image_array[i], result_count=2)
    
    print(image_name[i])
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
"""
"""
res = prediction.predictMultipleImage(image_array, result_count_per_image=2)

i = 0
for each_result in results_array:
    print(image_name[i])
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    
    for index in range(len(prediction)):
        print(predictions[index], " : ", percentage_probabilities[index])
        print("------------------------")
    i+=1
"""