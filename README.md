#  Flipkart Mobile Price Prediction

A **Machine Learning web application** that predicts the **price of mobile phones** based on specifications such as brand, model, color, memory, storage, and rating using **Random Forest Regression**.

The project uses a **Flipkart mobile dataset** and provides an interactive **Streamlit web interface** where users can select phone specifications and instantly get a predicted price.

---

# Live Demo

🔗 **Streamlit App**
https://flipkart-mobile-price-prediction-ang3t7fdidulzd9wbu9gnc.streamlit.app/

---

# Project Overview

This project focuses on building an **end-to-end Machine Learning pipeline** for mobile price prediction including:

* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Model deployment using Streamlit

The goal is to demonstrate how **machine learning can estimate smartphone prices based on product features.**

---

# Machine Learning Workflow

### 1. Data Collection

Dataset containing mobile phone specifications from **Flipkart**.

Features include:

* Brand
* Model
* Color
* Memory
* Storage
* Rating
* Original Price
* Selling Price

---

### 2. Data Preprocessing

Steps performed:

* Checked missing values
* Removed rows with null values
* Feature selection
* Encoding categorical variables
* Text feature extraction using TF-IDF

---

### 3. Feature Engineering

Different preprocessing techniques were applied based on data types:

| Feature Type | Method Used       |
| ------------ | ----------------- |
| Numerical    | StandardScaler    |
| Categorical  | OneHotEncoder     |
| Text         | TF-IDF Vectorizer |

---

### 4. Model Training

The model used:

**Random Forest Regressor**

Why Random Forest?

* Handles non-linear relationships
* Works well with mixed feature types
* Reduces overfitting using ensemble learning

The model was trained using:

* **80% Training Data**
* **20% Testing Data**

---

# Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Random Forest Regression
* Joblib
* Streamlit

---

# Project Structure

```
Mobile-Price-Prediction
│
├── Flipkart_Mobiles.csv
├── Mobile_Prices.joblib
├── app.py
├── main.ipynb
├── requirements.txt
└── README.md
```

---

#  Installation & Usage

### 1. Clone the Repository

```
git clone https://github.com/chaitanyagadwalait-droid/mobile-price-prediction.git
```

---

### 2. Install Required Libraries

```
pip install -r requirements.txt
```

---

### 3. Run the Application

```
streamlit run app.py
```

---

# How the App Works

1. User selects mobile **Brand**
2. Selects **Model**
3. Chooses **Color**
4. Selects **Memory**
5. Selects **Storage**
6. Chooses **Rating**
7. Clicks **Check Price**

The model then predicts the **estimated selling price** of the phone.

---

# Key Features

✔ End-to-End Machine Learning Project
✔ Feature Engineering with TF-IDF
✔ Pipeline-based Model Training
✔ Interactive Web Application
✔ Real-time Price Prediction
✔ Deployed using Streamlit Cloud

---

# Future Improvements

* Add more phone specifications
* Improve model accuracy
* Add price comparison visualization
* Integrate real-time Flipkart data
* Deploy using Docker or AWS

---

# Author

**Chaitanya Gadwala**

Email: [chaitanyagadwalait@gmail.com](mailto:chaitanyagadwalait@gmail.com)

LinkedIn
https://www.linkedin.com/in/chaitanya-gadwala-b18972192

GitHub
https://github.com/chaitanyagadwalait-droid

---

If you like this project, consider **starring the repository**.
