import streamlit as st

st.title("SAT Prep App 🚀")
st.write("Adaptive SAT practice")

questions = [
    {
        "question": "What is x if x + 5 = 12?",
        "choices": ["5", "6", "7", "8"],
        "answer": "C",
        "skill": "Linear Equations",
        "difficulty": 1,
        "explanation": "Subtract 5 from both sides: x = 7."
    },
    {
        "question": "What is x if 3x + 6 = 21?",
        "choices": ["3", "5", "7", "9"],
        "answer": "B",
        "skill": "Linear Equations",
        "difficulty": 2,
        "explanation": "Subtract 6: 3x = 15. Divide by 3: x = 5."
    },
    {
        "question": "What is 20% of 50?",
        "choices": ["5", "10", "15", "20"],
        "answer": "B",
        "skill": "Percentages",
        "difficulty": 1,
        "explanation": "20% of 50 is 10."
    },
    {
        "question": "If x² = 49, what could x be?",
        "choices": ["5", "6", "7 or -7", "9"],
        "answer": "C",
        "skill": "Quadratics",
        "difficulty": 1,
        "explanation": "The square root of 49 is 7, so x can be 7 or -7."
    },
    {
        "question": "If x² - 9 = 0, what are the possible values of x?",
        "choices": ["3 only", "-3 only", "3 or -3", "9"],
        "answer": "C",
        "skill": "Quadratics",
        "difficulty": 2,
        "explanation": "Add 9 to both sides: x² = 9. Therefore x = 3 or x = -3."
    },
    {
        "question": "If x² - 5x + 6 = 0, what are the possible values of x?",
        "choices": ["1 and 6", "2 and 3", "3 and 4", "1 and 5"],
        "answer": "B",
        "skill": "Quadratics",
        "difficulty": 3,
        "explanation": "Factor the equation: (x - 2)(x - 3) = 0. Therefore x = 2 or x = 3."
    }
]

# -------------------------
# SESSION STATE
# -------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "skill_results" not in st.session_state:
    st.session_state.skill_results = {}

if "answered" not in st.session_state:
    st.session_state.answered = False

if "finished" not in st.session_state:
    st.session_state.finished = False


# -------------------------
# PRACTICE QUESTIONS
# -------------------------

if not st.session_state.finished:

    question = questions[st.session_state.current_question]

    st.subheader(
        f"Question {st.session_state.current_question + 1} "
        f"of {len(questions)}"
    )

    st.write(question["question"])

    choices = ["A", "B", "C", "D"]

    options = [
        f"{letter}) {choice}"
        for letter, choice in zip(choices, question["choices"])
    ]

    selected = st.radio(
        "Choose your answer:",
        options,
        key=f"question_{st.session_state.current_question}"
    )

    if st.button("Submit Answer"):

        selected_letter = selected[0]
        skill = question["skill"]

        if skill not in st.session_state.skill_results:
            st.session_state.skill_results[skill] = {
                "correct": 0,
                "total": 0
            }

        st.session_state.skill_results[skill]["total"] += 1

        if selected_letter == question["answer"]:

            st.success("✅ Correct!")

            st.session_state.score += 1
            st.session_state.skill_results[skill]["correct"] += 1

        else:

            st.error("❌ Not quite.")

            st.write(
                f"Correct answer: {question['answer']}"
            )

        st.info(
            f"**Explanation:** {question['explanation']}"
        )

        st.session_state.answered = True

    # -------------------------
    # NEXT QUESTION
    # -------------------------

    if st.session_state.answered:

        if st.session_state.current_question < len(questions) - 1:

            if st.button("Next Question ➡️"):

                st.session_state.current_question += 1
                st.session_state.answered = False

                st.rerun()

        else:

            if st.button("Finish Practice 🎯"):

                st.session_state.finished = True

                st.rerun()


# -------------------------
# RESULTS
# -------------------------

else:

    st.header("🎯 Your Results")

    st.write(
        f"Overall Score: "
        f"**{st.session_state.score} / {len(questions)}**"
    )

    st.subheader("Skill Performance")

    weakest_skill = None
    weakest_percentage = 101

    for skill, results in st.session_state.skill_results.items():

        percentage = (
            results["correct"] /
            results["total"]
        ) * 100

        st.write(
            f"**{skill}:** "
            f"{results['correct']} / {results['total']} "
            f"({round(percentage)}%)"
        )

        if percentage < weakest_percentage:

            weakest_percentage = percentage
            weakest_skill = skill

    st.divider()

    st.subheader("🧠 Adaptive Recommendation")

    st.write(
        f"Your weakest skill is **{weakest_skill}** "
        f"with **{round(weakest_percentage)}%**."
    )

    if weakest_percentage < 50:

        recommended_difficulty = 1

    elif weakest_percentage < 80:

        recommended_difficulty = 2

    else:

        recommended_difficulty = 3

    st.write(
        f"Recommended difficulty: "
        f"**{recommended_difficulty}**"
    )

    # Find personalized question

    personalized_question = None

    for question in questions:

        if (
            question["skill"] == weakest_skill
            and question["difficulty"] == recommended_difficulty
        ):

            personalized_question = question
            break

    if personalized_question:

        st.subheader("🔥 Personalized Practice")

        st.write(
            personalized_question["question"]
        )

        choices = ["A", "B", "C", "D"]

        options = [
            f"{letter}) {choice}"
            for letter, choice in zip(
                choices,
                personalized_question["choices"]
            )
        ]

        practice_answer = st.radio(
            "Choose your answer:",
            options,
            key="personalized_question"
        )

        if st.button("Submit Personalized Practice"):

            selected_letter = practice_answer[0]

            if (
                selected_letter ==
                personalized_question["answer"]
            ):

                st.success("🎉 Correct!")

            else:

                st.error("❌ Not quite.")

                st.write(
                    f"Correct answer: "
                    f"{personalized_question['answer']}"
                )

            st.info(
                f"**Explanation:** "
                f"{personalized_question['explanation']}"
            )
