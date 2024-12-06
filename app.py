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