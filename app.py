from flask import Flask, render_template, request, redirect, send_from_directory
import numpy as np
import json
import uuid
import tensorflow as tf
import os

app = Flask(__name__)
model = tf.keras.models.load_model("models/plant_disease_recog_model_pwp.keras")

with open("plant_disease.json", 'r') as file:
    plant_disease = json.load(file)

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory('./uploadimages', filename)

@app.route('/')
def home():
    return render_template('home.html')

def extract_features(image):
    image = tf.keras.utils.load_img(image, target_size=(160, 160))
    feature = tf.keras.utils.img_to_array(image)
    return np.array([feature])

def model_predict(image):
    img = extract_features(image)
    prediction = model.predict(img)
    prediction_label = plant_disease[prediction.argmax()]
    return prediction_label

@app.route('/upload/', methods=['GET', 'POST'])
def uploadimage():
    if request.method == "POST":
        image = request.files['img']
        temp_name = f"uploadimages/temp_{uuid.uuid4().hex}_{image.filename}"
        image.save(temp_name)
        prediction = model_predict(temp_name)
        image_url = '/' + temp_name.replace("\\", "/")
        return render_template('upload.html', result=True, imagepath=image_url, prediction=prediction)
    return render_template('upload.html', result=False)

if __name__ == "__main__":
    if not os.path.exists("uploadimages"):
        os.mkdir("uploadimages")
    app.run(debug=True)
