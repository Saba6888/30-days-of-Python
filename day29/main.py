#Basic edge AI simulation 
import random

def edge_inference(sensor_data):
    return "Alert" if sensor_data > 0.7 else "Normal"

data_stream = [random.random() for _ in range(10)]
results = [edge_inference(data) for data in data_stream]
print(results)
