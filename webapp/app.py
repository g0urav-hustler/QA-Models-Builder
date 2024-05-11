import streamlit as st
import os

# page config
st.set_page_config(page_title="QA-Model-Builder ", layout="wide",)

# title
st.title("QA Model Builder Application")

#subtitle
st.markdown("This application helps you to build your own question answer model ")

uploaded_file = st.file_uploader("Upload your question answer file in csv format")

if uploaded_file is not None:
    folder = 'uploaded_files'
    with open(os.path.join(folder, "version1.csv"), "wb") as f:
        f.write(uploaded_file.getbuffer())

print(uploaded_file)
print('Type --', type(uploaded_file))