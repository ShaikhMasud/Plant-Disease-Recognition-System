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

📚 Refer to the TensorFlow Documentation here:
👉 [Transfer Learning with TensorFlow](https://www.tensorflow.org/tutorials/images/transfer_learning)

---

## 📈 Model Performance and Statistics

This model achieved 97% accuracy on test data by:

* Preprocessing with data augmentation
* Early stopping and learning rate scheduling
* Fine-tuned EfficientNetB4 architecture

Google collab link for traing the Model:(https://colab.research.google.com/drive/1M60m6lwKBTm5QwZVlnmYic2h7s93NNbc?usp=sharing)



Stats of training the model:


![image](https://github.com/user-attachments/assets/02466803-67ad-4a54-8dd5-be932c2cbbec)



Model Architecture:


![image](https://github.com/user-attachments/assets/1899ba9d-d8a6-4b51-ad8f-ee1315d7a421)

---

## 🌐 Web Interface using Flask

The Flask app provides a minimal and intuitive UI:

### 1. **Home Page**
Description:
![image](https://github.com/user-attachments/assets/a1a02fa8-78eb-4803-a4af-b99217aa441d)
Supported Diseases:
![image](https://github.com/user-attachments/assets/c03d10ed-acb8-45d9-8f78-1abc46722935)
![image](https://github.com/user-attachments/assets/2f8a9348-cb6f-42a9-9855-684128991e09)

### 2. **Upload Page**

Landing page:
![image](https://github.com/user-attachments/assets/23275761-ecd9-4f26-a1e3-9bf8c12bfd73)

Output:
![image](https://github.com/user-attachments/assets/479fda4a-a6d7-45eb-bfae-ed73b76a2f84)


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
