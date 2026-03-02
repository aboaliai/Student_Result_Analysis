import streamlit as st
import pandas as pd

st.title("🎓 Student Result Analysis System")

data = {
    "Name": ["Ravi", "Ravi", "Ravi",
             "Anjali", "Anjali", "Anjali",
             "Aman", "Aman", "Aman"],
    "Subject": ["Math", "Science", "English",
                "Math", "Science", "English",
                "Math", "Science", "English"],
    "Marks": [85, 78, 90,
              92, 88, 95,
              70, 75, 80]
}

df = pd.DataFrame(data)

st.subheader("📊 Raw Data")
st.dataframe(df)

# Total
total = df.groupby("Name")["Marks"].sum()
st.subheader("🏆 Total Marks")
st.write(total)

# Average
avg = df.groupby("Name")["Marks"].mean()
st.subheader("📈 Average Marks")
st.write(avg)

# Topper
topper = total.idxmax()
st.success(f"🏆 Topper is {topper}")

# Subject wise
subject_avg = df.groupby("Subject")["Marks"].mean()
st.subheader("📘 Subject Wise Average")
st.write(subject_avg)

# Pivot
pivot = df.pivot_table(values="Marks", index="Name", columns="Subject")
st.subheader("📑 Student vs Subject Table")
st.dataframe(pivot)