import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Roadmap Generator", page_icon="🚀")

st.title("🚀 AI Roadmap Generator")
st.write("Apna goal likho, AI tumhare liye poora roadmap bana de ga.")

api_key = st.text_input("Apni Groq API Key Yahan Dalo", type="password")
goal = st.text_input("Tumhara Goal Kya Hai? (e.g. Python seekhna hai)")

if st.button("Roadmap Banao"):
    if not api_key:
        st.warning("Pehle Groq API Key dalo!")
    elif not goal:
        st.warning("Pehle Goal likho!")
    else:
        with st.spinner("Roadmap ban raha hai..."):
            try:
                client = Groq(api_key=api_key)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": f"Mujhe {goal} ke liye step by step detailed roadmap banao, Roman Urdu me, beginner se advanced tak. Har week kya seekhna hai, wo bhi batao."}
                    ]
                )
                st.success("Ho gaya! Tumhara Roadmap tayyar hai 👇")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error aa gaya: {e}")
