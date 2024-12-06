# AI Writing Assistant

Application that help to summarize you text with the help of *llama3-8b-8192* model. Using Streamlit, Groq anf Langchain frameworks.

## Project content
- **app.py** - main program
- **requirements.txt** - list of libs
- **.streamlit/secrets.toml.example** - example of sectrets settings

## Installation

1. Copy repository.
2. Create Python Environment (venv) in VS Code. 
3. Register in [Groq.com](https://console.groq.com/) and create an API key
4. Rename **secrets.toml.example** to **secrets.toml**
5. Save your API key in **secrets.toml**
6. Install the packages: `pip install -r requiements.txt`
7. Run the app: `streamlit run app.py`
