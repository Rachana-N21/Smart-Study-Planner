import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Study Planner", layout="centered")

st.title("📚 Automated Study Planner")
st.write("Enter your subjects and available study hours")

subjects = []
hours = []

num_subjects = st.number_input("How many subjects?", min_value=1, max_value=10, step=1)

for i in range(num_subjects):
    subject = st.text_input(f"Subject {i+1} Name")
    hour = st.number_input(f"Hours needed for {subject if subject else 'Subject ' + str(i+1)}",
                           min_value=1, max_value=20, step=1)
    subjects.append(subject)
    hours.append(hour)

if st.button("Generate Study Plan"):

    total_hours = sum(hours)

    if total_hours == 0:
        st.error("Please enter valid hours.")
    else:
        st.subheader("📅 Your Study Plan")

        for i in range(len(subjects)):
            st.write(f"{subjects[i]} → {hours[i]} hours")

        st.success(f"Total Study Time: {total_hours} hours")

        # Visualization
        fig, ax = plt.subplots()
        ax.pie(hours, labels=subjects, autopct='%1.1f%%')
        ax.set_title("Study Time Distribution")

        st.pyplot(fig)