import streamlit as st
import requests

# Title of the application
st.title("GenAI SQL + Auto-Doc Assistant")

# Mode selection for either SQL Assistant or Auto-Doc Assistant
mode = st.radio("Choose Assistant", ["SQL Assistant", "Auto-Doc Assistant"])

# SQL Assistant Mode
if mode == "SQL Assistant":
    prompt = st.text_area("Describe your SQL query")
    if st.button("Generate SQL"):
        if prompt:
            with st.spinner('Generating SQL...'):
                try:
                    res = requests.post("http://localhost:8000/sql-assistant/", json={"prompt": prompt})
                    res.raise_for_status()  # Raises an HTTPError for bad responses

                    response_json = res.json()

                    # Check if the 'sql' key exists in the response
                    if 'sql' in response_json:
                        st.code(response_json['sql'])
                    else:
                        st.error("No SQL code returned from the assistant.")
                except requests.exceptions.RequestException as e:
                    st.error(f"API request failed: {e}")
                except ValueError:
                    st.error("Failed to parse the response.")
        else:
            st.warning("Please enter a prompt to generate SQL.")

# Auto-Doc Assistant Mode
else:
    code = st.text_area("Paste your Spark/SQL pipeline code")
    if st.button("Generate Documentation"):
        if code:
            with st.spinner('Generating documentation...'):
                try:
                    res = requests.post("http://localhost:8000/auto-doc/", json={"code": code})
                    res.raise_for_status()  # Raises an HTTPError for bad responses

                    response_json = res.json()

                    # Check if the 'documentation' key exists in the response
                    if 'documentation' in response_json:
                        st.markdown(response_json['documentation'])
                    else:
                        st.error("No documentation returned from the assistant.")
                except requests.exceptions.RequestException as e:
                    st.error(f"API request failed: {e}")
                except ValueError:
                    st.error("Failed to parse the response.")
        else:
            st.warning("Please paste your code to generate documentation.")
