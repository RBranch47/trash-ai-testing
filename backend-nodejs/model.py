from imageai.Detection import ObjectDetection
import os

BACKEND_PATH = "C:\\Users\\Huy\\Documents\\Code\\trash-ai\\backend-nodejs"

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(BACKEND_PATH, "models\\resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

detections = detector.detectObjectsFromImage(
    input_image=os.path.join(BACKEND_PATH, "images\\000111.jpg"), 
    output_image_path=os.path.join(BACKEND_PATH, "output\\out.jpg"), 
    minimum_percentage_probability=20,
    display_percentage_probability=True,
    display_object_name=True,
    #extract_detected_objects=True
)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])