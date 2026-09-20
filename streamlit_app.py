import streamlit as st

st.title("SAT Prep App 🚀")

st.write("My SAT app is working!")

st.write("Question: What is 3x + 6 = 21?")

answer = st.radio(
    "Choose your answer:",
    ["A) 3", "B) 5", "C) 7", "D) 9"]
)

if st.button("Submit"):
    if answer == "B) 5":
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect. Try again!")
