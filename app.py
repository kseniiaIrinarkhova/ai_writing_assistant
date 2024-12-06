import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Page Config
st.set_page_config(page_title="AI Writing Tool")

# Page title
st.title("AI Writing Tool")

# LLM (Model)
llm = ChatGroq(groq_api_key=st.secrets["GROQ_API_KEY"], model="llama3-8b-8192")

# Prompt Template
prompt_template = ChatPromptTemplate([("system", "You're an expert at text summarizing"), ("user", "Summarize this text: {text}")])

# Output Parser
parser = StrOutputParser()

# Chain
chain = prompt_template | llm | parser 

# create a session for summarized text
st.session_state["summarized_text"] = ""

with st.form("summarize_form", clear_on_submit=True):
    # Text
    text_to_summarize = st.text_area('Enter text to summarize')
    submitted = st.form_submit_button('Submit')
    # If form is submitted
    if submitted:
        #clear the previous summarized text
        st.session_state["summarized_text"] = ""
        # Summarize the text
        with st.spinner("Summarizing..."):
            # Invoke the chain
            summarized_text = chain.invoke({"text": text_to_summarize})
            # Save the summarized text in session state
            st.session_state["summarized_text"] = summarized_text

# Display the summarized text
if st.session_state["summarized_text"]:
    input, output = st.columns(2)

    with input:
        st.markdown(f"## Your text \n\n{text_to_summarize}")

    with output:
        st.markdown(f"## Summarized text \n\n")
        st.markdown(st.session_state.summarized_text)
