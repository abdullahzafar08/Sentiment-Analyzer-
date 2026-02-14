import streamlit as st
import json
import main

st.set_page_config(
    page_title="Vibe Check - Sentiment Analyzer",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Vibe Check")
st.subheader("Analyze the sentiment of your text with Gemini AI")

# Text Input
user_input = st.text_area("Enter text to analyze:", height=150, placeholder="Type something here...")

if st.button("Analyze Vibe 🚀", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Analyzing vibe..."):
            result = main.analyze_text(user_input)
        
        if "error" in result:
            st.error(f"Error: {result['error']}")
        else:
            st.success("Analysis Complete!")
            
            # Create columns for metrics
            col1, col2 = st.columns(2)
            
            sentiment = result.get("sentiment", "Unknown")
            score = result.get("score", 0)
            
            with col1:
                st.metric("Sentiment", sentiment)
            
            with col2:
                st.metric("Score", f"{score}/10")
            
            st.markdown("### Summary")
            st.write(result.get("summary", "No summary available."))
            
            with st.expander("See Reasoning"):
                st.write(result.get("reasoning", "No reasoning available."))
            
            # Display raw JSON for debugging/transparency
            with st.expander("Raw Data"):
                st.json(result)
