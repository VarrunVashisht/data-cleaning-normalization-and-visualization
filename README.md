# Salary Data Normalization and Visualization

## 📌 Project Overview

This project demonstrates how to **clean, preprocess, normalize, and visualize salary data** from a survey dataset using Python.
It focuses on handling missing values, applying normalization techniques, and comparing distributions using visualizations.

The dataset contains duplicate and missing values, making it suitable for practicing real-world data preprocessing techniques.

---

## 🎯 Objectives

* Identify and handle missing values in survey data
* Apply different normalization techniques to numerical data
* Understand how normalization affects data distribution
* Visualize original vs normalized data for comparison

---

## 🧰 Technologies Used

* **Python**
* **Pandas** – data manipulation and cleaning
* **Matplotlib** – data visualization

---

## 🧹 Data Cleaning Steps

### 1. Handling Missing Values

* Missing values in `CodingActivities` are filled using **forward fill**.
* Missing values in `ConvertedCompYearly` are filled using the **median**, which helps reduce the effect of outliers.

---

## 📊 Data Normalization Techniques

### 1. Min-Max Normalization

* Scales salary values between **0 and 1**
* Helps compare values on a uniform scale

### 2. Z-Score Normalization

* Standardizes data based on **mean and standard deviation**
* Useful for identifying how far values deviate from the average

---

## 📈 Data Visualization

Histograms are used to compare distributions of:

* Original salary values
* Min-Max normalized salary values
* Z-score normalized salary values

These visualizations help understand how normalization changes the data spread and shape.

---

## 📌 Key Learnings

* Importance of handling missing data before analysis
* Differences between Min-Max and Z-score normalization
* Visual comparison improves understanding of data transformations

---

## 📜 License

This project is for educational and learning purposes.

---

## Author: Varrun Vashisht
