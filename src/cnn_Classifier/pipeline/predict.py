import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

       



    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename

        test_image = image.load_img(imagename, target_size=(128,128))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0  # <-- Add this line to normalize
        test_image = np.expand_dims(test_image, axis=0)

        # Get prediction probabilities
        probs = model.predict(test_image)
        print("Probabilities:", probs)

        # Get predicted class index
        result = np.argmax(probs, axis=1)
        print("Predicted index:", result)

        # Map prediction to label
        if result[0] == 1:
            prediction = 'Healthy'
        else:
            prediction = 'Coccidiosis'

        return [{"image": prediction}]