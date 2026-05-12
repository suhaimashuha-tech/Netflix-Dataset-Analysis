# 🎬 Netflix Dataset Analysis & Recommendation System

## 📌 Project Overview

This project is a **Netflix Dataset Analysis and Content-Based Recommendation System** built using Python. It analyzes the Netflix Movies & TV Shows dataset and provides meaningful insights along with personalized content recommendations.

The application also includes a **Streamlit web interface** for interactive visualization and user-friendly recommendations.

---

## 🚀 Features

### 📊 Data Analysis

* Distribution of Movies vs TV Shows
* Top Countries producing content
* Most popular genres
* Content trends over the years

### 🎬 Recommendation System

* Content-based filtering using **TF-IDF**
* Suggests similar movies/TV shows based on:

  * Title
  * Description

### 🌐 Web Interface

* Built with **Streamlit**
* Interactive charts and visualizations
* User input for movie recommendations

---

## 🧠 Technologies Used

* Python 🐍
* Pandas
* Scikit-learn
* Streamlit
* Matplotlib / Seaborn

---

## 📂 Project Structure

```
netflix-analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── recommender.py
│
├── app.py          # Streamlit app
├── main.py         # CLI version
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/netflix-analysis.git
cd netflix-analysis
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🔹 Run Streamlit App

```
python -m streamlit run app.py
```

### 🔹 Run CLI Version

```
python main.py
```

---

## 📊 Sample Analysis Output

* Movies vs TV Shows distribution
* Top 5 Countries producing content
* Most common genres
* Year-wise content growth

---

## 🎬 Example Recommendation

**Input:**

```
Stranger Things
```

**Output:**

```
Dark
The OA
Black Mirror
Sense8
```

---

## 💡 Future Improvements

* 🎨 Enhanced UI with better styling
* 🔍 Search suggestions & autocomplete
* 🎬 Movie posters integration
* 🌐 Deployment on cloud (Streamlit Cloud / Render)
* 🤖 Hybrid recommendation system

---

## 👨‍💻 Author

**Suhaima Farha**

---
