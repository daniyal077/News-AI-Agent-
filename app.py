import streamlit as st
from crew import crew  

st.set_page_config(page_title="CrewAI Newsletter Generator", layout="wide")

st.title("CrewAI Financial Trends Newsletter Automation")
st.write("This app uses a multi-agent CrewAI workflow with Groq-powered LLM inference to generate a newsletter on emerging financial trends.")

topic = st.text_input("Enter the topic for your newsletter:", value="Artificial Intelligence in Finance")

if st.button("Generate Newsletter"):
    st.info("Processing your request... This might take a moment.")
    try:
        result = crew.kickoff(inputs={"topic": topic})
        
        st.success("Newsletter generated successfully!")
        st.markdown(result)
                
    except Exception as e:
        st.error(f"An error occurred: {e}")
