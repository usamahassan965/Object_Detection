### We can prepare data (1.Prepare_data) on local machine and run training on colab for fast training.

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=25)  # train the model
