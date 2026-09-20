import streamlit as st

st.title("SAT Prep App 🚀")

questions = [
    {
        "question": "What is 3x + 6 = 21?",
        "answers": ["A) 3", "B) 5", "C) 7", "D) 9"],
        "correct": "B) 5",
        "skill": "Linear Equations"
    },
    {
        "question": "What is 20% of 50?",
        "answers": ["A) 5", "B) 10", "C) 15", "D) 20"],
        "correct": "B) 10",
        "skill": "Percentages"
    },
    {
        "question": "What is x + 7 = 15?",
        "answers": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "correct": "C) 8",
        "skill": "Linear Equations"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

question = questions[st.session_state.current_question]

st.subheader(f"Question {st.session_state.current_question + 1}")

st.write(question["question"])

answer = st.radio(
    "Choose your answer:",
    question["answers"]
)

if st.button("Submit"):

    if answer == question["correct"]:
        st.success("Correct! 🎉")
        st.session_state.score += 1
    else:
        st.error("Incorrect ❌")

    st.write(f"Skill: {question['skill']}")

    if st.session_state.current_question < len(questions) - 1:
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.success(
            f"You finished! Score: {st.session_state.score} / {len(questions)}"
        )
