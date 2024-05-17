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



#subtitle
st.markdown("Enter the data from datset")

# context
context_column = st.text_input(label = "Enter the context column from dataset")

# question column input
question_column = st.text_input(label = "Enter the question column from dataset")

# answer_column input 
answer_column = st.text_input(label = "Enter the answer column from dataset" )

# answer_start_column 
answer_start_column = st.text_input(label = "Enter the answer start column if it was in dataset else leave this.")

# train_data_size input
train_data_size = st.number_input("Enter training data size ", value=None, placeholder="0 - 1")

# val_data_size input
val_data_size = st.number_input("Enter val data size ", value=None, placeholder="0 - 1")

st.markdown("Select the model parameter")

model_options = ["bert", "roberta", "distilbert", "distilroberta", "electra-base", "electra-small", "xlnet"]

# model type input
model_type = st.selectbox(label="Enter the model type you want to train ", options= model_options)

# epochs input
no_of_epochs = st.number_input("Enter the epochs  ", value=0)

# train batch size
train_batch_size = st.number_input("Enter train batch size ", value = 4)

# val batch size input
val_batch_size = st.number_input("Enter val batch size", value = 4)



model_name = None
if model_type == "bert":
    model_name = "bert-base-cased"

elif model_type == "roberta":
    model_name = "roberta-base"

elif model_type == "distilbert":
    model_name = "distilbert-base-cased"

elif model_type == "distilroberta":
    model_type = "roberta"
    model_name = "distilroberta-base"

elif model_type == "electra-base":
    model_type = "electra"
    model_name = "google/electra-base-discriminator"

elif model_type == "electra-small":
    model_type = "electra"
    model_name = "google/electra-small-discriminator"

elif model_type == "xlnet":
    model_name = "xlnet-base-cased"


params_data = {
    "data_processing":
        {
            "context_col": context_column,
            "question_col": question_column,
            "answer_col": answer_column,
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
if st.form_submit_button(label="Submit", help=None, on_click=None,):
    with open('temp.yaml', 'w') as outfile:
        yaml.dump(params_data, outfile, default_flow_style=False)

