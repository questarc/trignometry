import streamlit as st

def show_trig_puzzles_games():
    st.header("Puzzles & Games")
    st.markdown("Match ratios to triangles or identify quadrants in these fun challenges!")
    
    st.subheader("Ratio Matching Game")
    ratios = ["sin(θ) = 0.5", "cos(θ) = 0.5", "tan(θ) = 1"]
    triangles = ["Triangle A: Opp=3, Hyp=6", "Triangle B: Adj=3, Hyp=6", "Triangle C: Opp=4, Adj=4"]
    answers = {0: 0, 1: 1, 2: 2}
    
    selections = {}
    for i, ratio in enumerate(ratios):
        selections[ratio] = st.selectbox(f"Match {ratio}", triangles, key=f"ratio_{i}")
    
    if st.button("Check Matches"):
        correct = sum(1 for i, ratio in enumerate(ratios) if selections[ratio] == triangles[answers[i]])
        st.markdown(f"You got {correct}/{len(ratios)} correct!")
