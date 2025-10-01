import streamlit as st

def show_trig_quiz():
    st.header("Trigonometry Quiz")
    st.markdown("Test your knowledge with these multiple-choice questions!")

    questions = [
        {
            "question": "What is sin(90°)?",
            "options": ["0", "1", "-1", "Undefined"],
            "answer": "1"
        },
        {
            "question": "What does SOH stand for?",
            "options": ["Sine = Opposite/Hypotenuse", "Cosine = Adjacent/Hypotenuse", "Tangent = Opposite/Adjacent", "None"],
            "answer": "Sine = Opposite/Hypotenuse"
        },
        {
            "question": "The period of tan(x) is:",
            "options": ["360°", "180°", "90°", "270°"],
            "answer": "180°"
        },
        {
            "question": "Pythagorean identity:",
            "options": ["sin² + cos² = 1", "sin + cos = 1", "tan = sin/cos", "All of the above"],
            "answer": "sin² + cos² = 1"
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}: {q['question']}")
        answer = st.radio("Choose:", q["options"], key=f"quiz_{i}")
        if st.button(f"Submit Q{i+1}", key=f"submit_q{i}"):
            if answer == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! Correct answer: {q['answer']}")

    if st.button("Show Score"):
        st.markdown(f"Your score: {score}/{len(questions)}")
