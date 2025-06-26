# 📊 Sentilyzer – Real-Time Sentiment Analyzer for Social Media

**Sentilyzer** is an AI-powered sentiment analysis tool built using Python and Streamlit. It analyzes text from social media or datasets (like YouTube comments) in real time, classifying sentiments as **Positive**, **Negative**, or **Neutral**.

---

## 🚀 Features

- 🔍 Real-time sentiment detection for typed input
- 📁 Bulk sentiment analysis from the YouTube comments dataset
- 📊 Visual bar chart for sentiment distribution
- 📄 CSV export of predictions

---

## 🗂️ Project Structure

```

sentilyzer/
├── streamlit_app.py              # Streamlit UI and sentiment analysis
├── sentiment.py                  # VADER sentiment engine
├── visualize.py                  # Chart for sentiment summary
├── YoutubeCommentsDataSet.csv   # Sample dataset
├── youtube_predictions.csv       # Auto-generated predictions
└── requirements.txt              # Required Python packages

````

---

## 🛠️ Installation

### 1. Clone / Extract Project

Unzip or clone the project folder into your local system.

### 2. Install Dependencies

Make sure you have Python 3.8+ installed.

Then install the required libraries:

```bash
pip install -r requirements.txt
````

---

## ▶️ How to Run

Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

It will open automatically in your browser.

---

## 📥 Dataset

This project includes a small sample from:

**Dataset Source:**
[YouTube Comments Sentiment Dataset](https://www.kaggle.com/datasets/atifaliak/youtube-comments-dataset)

To analyze a larger dataset, replace `youtube_comments_sample.csv` with the full Kaggle file.

---

## 📊 Visualize Results

After running sentiment analysis, you can generate a bar chart summary with:

```bash
python visualize.py
```

---

## ✅ Output

![image](https://github.com/user-attachments/assets/a971b6f6-a618-4929-a89d-408c08e247c1)


---

## 🧠 Built With

* [Streamlit](https://streamlit.io/)
* Pandas, Matplotlib

---

## 📬 Author

**[Sandeep Mopidevi](https://www.linkedin.com/in/sandeepmopidevi)**

---
