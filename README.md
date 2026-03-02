# Student Result Analysis System

A lightweight, menu-driven web application built with **Streamlit** and **Pandas** to analyze student performance data without the need for complex charting libraries.

## Overview

This project provides an intuitive interface for educators and students to interact with academic datasets. By uploading a simple CSV file, users can perform deep dives into student marks, subject averages, and passing criteria dynamically.

## Key Features

The application is divided into several functional modules:

* **📊 Raw Data:** View the entire uploaded dataset in a searchable table.
* **📈 Student Result:** Automatically calculates total and average marks for every student.
* **🏆 Topper Analysis:** Filter the top $N$ students based on their cumulative scores.
* **🔍 Search Student:** Quick lookup for individual student records and summaries.
* **📘 Subject Analysis:** Breakdown of average performance across different subjects.
* **📌 Pass/Fail Logic:** Interactive slider to set passing marks and instantly categorize students.
* **📑 Pivot Table:** A matrix view comparing Students vs. Subjects for a bird's-eye view of marks.

## 🛠️ Technology Stack

* **Python:** Core logic.
* **Streamlit:** Web framework for the UI.
* **Pandas:** Data manipulation and analysis.
* **Streamlit Option Menu:** For the polished sidebar navigation.

## 📋 Prerequisites

Ensure you have a CSV file with the following columns for the app to function correctly:

1. `Name` (Student Name)
2. `Subject` (Subject Name)
3. `Marks` (Numerical Score)

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Student_Result_Analysis.git
cd Student_Result_Analysis

```


2. **Install dependencies:**
```bash
pip install streamlit pandas streamlit-option-menu

```


3. **Run the application:**
```bash
streamlit run your_filename.py

```



---

## 💡 How to Use

1. Launch the app and use the **Sidebar** to upload your student CSV file.
2. Navigate through the **📌 Menu** to select different analysis modes.
3. For the **Pass/Fail** section, use the slider to adjust the threshold dynamically.
4. In the **Topper** section, input the number of top-performing students you wish to display.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

---
