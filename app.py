import shutil
import streamlit as st
import os
import time
import yaml
import pandas as pd
from main import InvokePipeline


def compressing_model(model_path, zip_file_name):
    for dirs in os.listdir(model_path):
        if "checkpoint" in dirs:
            shutil.rmtree(os.path.join(model_path,dirs))

    shutil.make_archive(zip_file_name, "zip", model_path)
    
model_result = None

# page config
st.set_page_config(page_title="QA-Model-Builder ", layout="wide",)

# title
st.title("QA Model Builder Application")

#subtitle
st.markdown("This application helps you to build your own question answer model ")

uploaded_file = st.file_uploader("Upload your data set file in csv format")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df_columns = list(df.columns)
    
    df_columns.insert(0, "None")

    with st.form("my_form"):

        #subtitle
        st.markdown("Enter the data from dataset")
        col1, col2, col3 , col4 = st.columns(4)
        
        # context
        with col1:
            context_column = st.selectbox(label = "Select the context column", options= df_columns)

        # question column input
        with col2:
            question_column = st.selectbox(label = "Select the question column", options= df_columns)

        # answer_column input 
        with col3:
            answer_column = st.selectbox(label = "Select the answer column", options = df_columns )

        # answer_start_column
        with col4: 
            answer_start_column = st.selectbox(label = "Select the answer start column", options= df_columns)


        train_data_range = list(range(10,100,10))
        data_size_col1, data_size_col2 = st.columns(2)

        # train_data_size input
        # train_data_range = 80 
        with data_size_col1:
            train_data_size = st.selectbox("Enter training data size ", options=train_data_range)

        # val_data_size input
        validation_data_range = list(range(10, (100-train_data_size) + 10, 10))
        with data_size_col2:
            val_data_size = st.selectbox("Enter validation data size ", options= validation_data_range)

        st.markdown("Select the model parameter")
        
        par_col1, par_col2, par_col3, par_col4 = st.columns(4)

        model_options = ["bert", "roberta", "distilbert", "distilroberta", "electra-base", "electra-small", "xlnet"]

        # model type input
        with par_col1:
            model_type = st.selectbox(label="Enter the model ", options= model_options)

        # epochs input
        with par_col2:
            no_of_epochs = st.number_input("Enter the no of epochs", value=0)

        # train batch size
        with par_col3:
            train_batch_size = st.number_input("Enter train batch size ", value = 4)

        # val batch size input
        with par_col4:
            val_batch_size = st.number_input("Enter val batch size", value = 4)

        sb_col1, sb_col2, sb_col3, sb_col4, sb_col5 = st.columns(5)
        with sb_col3:
            submitted = st.form_submit_button(label = "Submit Parameters")

    
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

                "train_data_size": train_data_size / 100,
                "val_data_size": val_data_size /100 ,

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

    if submitted:
        folder = 'web_files'
        file_path = os.path.join(folder, "data_file.csv")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with open('params.yaml', 'w') as outfile:
            yaml.dump(params_data, outfile, default_flow_style=False)

    button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)
    if os.path.isfile("params.yaml"):
        with button_col3:
            train_button = st.button("Train The Model")
        if train_button and not submitted:
            with st.status("Training Status", expanded=True) as status:
                st.write("Data Loading.")
                time.sleep(3)
                st.write("Data Preprocessing")
                time.sleep(2)
                st.write("Training model..")
                time.sleep(5)
                pipline_object = InvokePipeline()
                model_result = pipline_object.main()

                shutil.copytree("/home/gourav/ML/QA_Models_Builder/logs/bert", os.path.join("artifacts","models", model_type))
                compressing_model(os.path.join("artifacts","models",model_type), model_type)
                status.update(label="Model Trained Succesfully", state="complete", expanded=False)
 
            st.success('Done!')

        
    if os.path.isdir(os.path.join("artifacts","models",model_type)):

        if model_result != None:

            result_col1, result_col2 = st.columns(2)
                
            with result_col1:
                st.write("Model Parameters")
                st.write(params_data["model_params"])

            with result_col2:
                # result_data = {"Configs": model_result.keys(), "Values": model_result.values()}
                # result_dataframe = pd.DataFrame.from_dict(result_data)
                # st.write("Result Model Metrics")
                st.write(model_result)
                    

        st.write("Try Trained Model Output")

        title = st.text_input("Try any question ",None, placeholder= "Write question here..")
        if title:
            st.write("Answer:")
            st.write("The current movie title is", title)


        with open(f"{model_type}.zip", "rb") as fp:
            btn = st.download_button(
                label="Download Trained Model",
                data=fp,
                file_name=f"{model_type}.zip",
                mime="application/octet-stream"
                )
            
footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;background-color: #000;color: white;text-align: center;}
</style><div class='footer'><p>Made By Gourav Chouhan</p></div>"""
st.markdown(footer, unsafe_allow_html=True)
            
# footer_html = """<div style='text-align: center;'>
#   <p>Developed with ❤️ by Gourav Chouhan </p>
# </div>"""
# st.markdown(footer_html, unsafe_allow_html=True)
# st.divider() 

# st.caption("Made by Gourav Chouhan ")
