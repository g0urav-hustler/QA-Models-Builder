import streamlit as st
import os
import yaml

# page config
st.set_page_config(page_title="QA-Model-Builder ", layout="wide",)

# title
st.title("QA Model Builder Application")

#subtitle
st.markdown("This application helps you to build your own question answer model ")

uploaded_file = st.file_uploader("Upload your question answer file in csv format")

if uploaded_file is not None:
    folder = 'web_files'
    with open(os.path.join(folder, "data.csv"), "wb") as f:
        f.write(uploaded_file.getbuffer())


yaml_data_format = {
    "data_processing":
        {
            "context_col": context_column,
            "question_col": question_column,
            "anwer_col": answer_column,
            "answer_start_col": answer_start_column,

            "train_data_size": train_data_size,
            "val_data_size": val_data_size,

        },
    "model_params":
        {
            "model_type": model_type,
            "model_name": model_name,
            "epochs": no_of_epochs,
            "train_batch_size": train_batch_size,
            "val_batch_size": val_batch_size
        }

}

