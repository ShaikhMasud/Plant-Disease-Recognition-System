# 🌿 Plant Disease Recognition System

This project uses **EfficientNetB4** and **Transfer Learning** to detect plant diseases from images of individual leaves. It is built using **TensorFlow**, trained on the **PlantVillage dataset**, and deployed as a **Flask web application**.

---

## 🚀 Overview

This project demonstrates a practical application of computer vision in agriculture by diagnosing plant diseases using images of single leaves. It includes:

* Training an image classifier using **EfficientNetB4** with **Transfer Learning**.
* A simple **Flask-based web UI** to upload and classify leaf images.
* Visualization of **training statistics** and prediction results.

---

## 📊 Model Training

### ✅ Dataset

We used the **PlantVillage** dataset, which contains **39 classes** representing both **diseased** and **healthy** plant leaf images. All images in this dataset are of **single leaves on a plain background** — ideal for controlled environment recognition.

⚠️ **Note:** The model may not work well with real-world tree or plant images that have multiple leaves or complex backgrounds.

### 🧠 Transfer Learning Process

We followed the two-step **Transfer Learning** approach as recommended by TensorFlow:

1. **Feature Extraction**: We froze the base EfficientNetB4 model and trained only the top classifier layers.
2. **Fine-tuning**: We unfroze the top layers of the base model and trained it together with the classifier for improved performance.

📚 Refer to the TensorFlow guide here:
👉 [Transfer Learning with TensorFlow](https://www.tensorflow.org/tutorials/images/transfer_learning)

---

## 📈 Model Performance and Statistics

The model achieved **high accuracy** on validation data thanks to:

* Preprocessing with data augmentation
* Early stopping and learning rate scheduling
* Fine-tuned EfficientNetB4 architecture

📌 *Add some training/validation accuracy/loss plots here if available (e.g., from TensorBoard or Matplotlib)*

---

## 🌐 Web Interface using Flask

The Flask app provides a minimal and intuitive UI:

### 1. **Home Page**

* Project description and purpose.
* Encourages users to try uploading their own leaf images.

### 2. **Upload Page**

* Upload a `.jpg`, `.png`, or `.jpeg` image of a single leaf.
* On submission, the model predicts the disease or healthy status of the leaf.
* The result is shown on the same page with the **predicted class label**.

---

## 🧠 Model File

The actual trained `.keras` model file (≈208MB) is **not included** in this GitHub repository due to size constraints.

🔗 **Download the model file here**:
[Google Drive Link](https://drive.google.com/file/d/1HKboASxq4nN05xRAf3-QQlXJOXrUTG0n/view?usp=drive_link)

📁 **After downloading, place the model inside the `/models` directory.**

---

## 🛠️ Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/plant-disease-recognition.git
   cd plant-disease-recognition
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the model from the link above and place it inside the `models/` folder.

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`.

---

## 📷 Sample Inputs & Outputs

*Include a few example input leaf images and the corresponding predictions made by the model.*

---

## 🧪 Limitations

* Trained only on images with plain backgrounds — may not generalize to complex real-world images.
* Not suitable for diagnosing diseases from full plant/tree images.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Let me know if you want this converted into a `README.md` file directly or want to embed specific image examples.
