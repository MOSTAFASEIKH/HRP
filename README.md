# 🏠 House Rent Prediction Using Machine Learning

An end-to-end Machine Learning project that predicts monthly house rental prices based on property characteristics such as size, location, furnishing status, floor details, and other relevant features.

---

# 📌 Project Overview

The real estate rental market is influenced by multiple factors, making it difficult to estimate an appropriate rental price manually. This project applies supervised machine learning techniques to develop a regression model capable of predicting monthly house rent using historical property data.

The project follows a complete machine learning pipeline, including:

* Problem Definition
* Dataset Understanding
* Exploratory Data Analysis (EDA)
* Data Cleaning
* Feature Engineering
* Train-Test Split
* Model Training
* Model Evaluation
* Model Comparison
* Model Selection
* Model Saving

The final model can be reused for future predictions and deployment.

---

# 🎯 Problem Statement

Rental prices depend on several factors such as:

* Property Size
* Number of Bedrooms (BHK)
* Bathroom Count
* City
* Area Locality
* Area Type
* Furnishing Status
* Floor Information
* Tenant Preference

The objective of this project is to build a machine learning model that accurately predicts monthly house rental prices using these property features.

---

# 🎯 Project Objectives

* Perform Exploratory Data Analysis (EDA)
* Clean and preprocess the dataset
* Engineer meaningful features
* Transform categorical variables into numerical representations
* Train multiple regression models
* Compare model performance
* Select the best-performing model
* Save the trained model for future predictions

---

# 📊 Dataset Description

The dataset contains residential rental property information collected from multiple cities in India.

### Input Features

* BHK
* Size
* Floor
* Area Type
* Area Locality
* City
* Furnishing Status
* Tenant Preferred
* Bathroom
* Point of Contact
* Posted On

### Target Variable

* Rent (Monthly House Rent)

---

# 🛠 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook

---

# 🔄 Project Workflow

```text
Problem Definition
        ↓
Dataset Understanding
        ↓
Exploratory Data Analysis (EDA)
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Model Selection
        ↓
Model Saving
```

---

# ⚙️ Data Preprocessing

The following preprocessing steps were performed:

* Converted date column into datetime format
* Extracted Year, Month, and Day features
* Split Floor into Current Floor and Total Floors
* Converted special floor names to numerical values
* Converted Total Floors to numeric values
* Handled missing values
* Encoded categorical variables
* Prepared the dataset for machine learning

---

# 🤖 Machine Learning Models

The following regression algorithms were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

---

# 📈 Model Performance

| Model                       |   R² Score |          MAE |         RMSE |
| --------------------------- | ---------: | -----------: | -----------: |
| Gradient Boosting Regressor | **0.5684** | **13086.69** | **41471.62** |
| Linear Regression           |     0.5251 |     21764.50 |     43504.43 |
| Random Forest Regressor     |     0.0667 |     13279.40 |     60989.55 |
| Decision Tree Regressor     |    -2.8518 |     19428.14 |    123898.06 |

---

# 🏆 Best Model

Based on the evaluation metrics, the **Gradient Boosting Regressor** achieved the best overall performance.

**Performance Metrics**

* R² Score: **0.5684**
* MAE: **13,086.69**
* RMSE: **41,471.62**

The trained model was saved using **Joblib** for future predictions.

---

# 📁 Project Structure

```
House-Rent-Prediction/
│
├── data/
│   └── House_Rent_Dataset.csv
│
├── notebooks/
│   └── House_Rent_Prediction.ipynb
│
├── models/
│   └── house_rent_prediction_model.pkl
│
├── images/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/House-Rent-Prediction.git
```

Navigate to the project folder:

```bash
cd House-Rent-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebook and run all cells.

---

# 📦 Requirements

* Python 3.x
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook

---

# 💡 Future Improvements

Possible enhancements include:

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Feature selection techniques
* Outlier detection and treatment
* Advanced boosting algorithms such as XGBoost, LightGBM, and CatBoost
* Streamlit web application for rent prediction
* Model deployment using Flask or FastAPI
* Docker containerization
* CI/CD integration for automated deployment

---

# 🎓 Learning Outcomes

This project demonstrates practical experience in:

* Data preprocessing
* Feature engineering
* Exploratory Data Analysis
* Regression modeling
* Model evaluation
* Model comparison
* Model selection
* Model persistence
* End-to-end machine learning workflow

---

# 👤 Author

**Mostafa Sk**

Assistant Professor (AI & Machine Learning)

M.Tech in VLSI Design

Aspiring AI/ML Engineer | Machine Learning | Data Science | Python | Scikit-learn

---

# ⭐ Acknowledgements

This project was developed as part of a practical machine learning portfolio to demonstrate end-to-end regression modeling using Python and Scikit-learn.
