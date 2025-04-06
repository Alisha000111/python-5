import streamlit as st
import random
from datetime import datetime, timedelta

def main():
    
    st.set_page_config(
        page_title="Alisha",
        page_icon="",
        layout="centered"
    )
    
    st.markdown("""
    <style>
    .big-font {
        font-size:22px !important;
        font-family: 'Arial', sans-serif;
    }
    .challenge-box {
        border-left: 5px solid rgb(143, 240, 146);
        padding: 10px;
        background-color:rgb(235, 230, 129);
        border-radius: 0px 10px 10px 0px;
        margin: 10px 0px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    st.title("💚✨ MindGrow Daily")
    st.markdown("""
    *"Every small step grows your mind"*  
    *Created with care by Team GrowBetter*
    """)
    
   
    name = st.text_input("Hey there! What's your name?", "Alisha")
    
    
    st.subheader(f"Hi {name}! Ready for today's growth challenge?")
    
    challenges = [
        "Try learning one new thing outside your comfort zone today",
        "When you face a problem, say 'I can't do this YET' out loud",
        "Write down 3 things you improved at this week, no matter how small",
        "Ask a colleague/friend for constructive feedback on something you're working on",
        "Spend 10 minutes practicing a skill you want to improve",
        "Reflect on a recent mistake and list 2 lessons you learned from it"
    ]
    
    if st.button("Give me today's challenge!"):
        today_challenge = random.choice(challenges)
        st.markdown(f"""
        <div class="challenge-box">
            <p class="big-font"><b>Your Challenge:</b></p>
            <p class="big-font">💚✨ {today_challenge} 💚✨</p>
        </div>
        """, unsafe_allow_html=True)
        
        
        st.write("")
        progress = st.slider("How much did this challenge stretch you?", 1, 15, 30)
        
        if progress >= 7:
            st.success(f"Awesome growth, {name}! Keep pushing those boundaries!")
        else:
            st.info(f"Every effort counts, {name}! Tomorrow's another opportunity.")
    
    
    st.subheader("Daily Growth Reflection")
    reflection = st.text_area(f"What's one way you grew today, {name}? (Optional)")
    
    if reflection:
        st.balloons()
        st.success("Thanks for sharing! Reflection is key to growth.")
    
    
    st.markdown("---")
    st.caption("Made with care for growth-minded people like you 💚✨")

if __name__ == "__main__":
    main()