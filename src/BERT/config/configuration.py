import os
from src.BERT.constants import *
from src.BERT.utils.common import read_yaml, create_directories
from src.BERT.entity.config_entity import (DataIngestionConfig, 
                                           DataProcessing,
                                           TrainModelConfig)


class ConfigurationManager:

    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.raw_data_dir])

        data_ingestion_config = DataIngestionConfig(
            raw_data_dir= config.raw_data_dir,
            web_data_dir= config.web_data_dir
        )

        return data_ingestion_config
    
    def get_data_processing_config(self) ->DataProcessing:

        config = self.config.data_processing
        params = self.params.data_processing

        create_directories([config.processed_data_dir, config.split_data_dir])

        data_processing_config = DataProcessing(
            raw_data_dir= config.raw_data_dir,
            processed_data_dir= config.processed_data_dir,
            split_data_dir= config.split_data_dir,

            context_col= params.context_col,
            question_col= params.question_col,
            answer_col= params.answer_col,
            answer_start_col= params.answer_start_col,

            train_data_size= params.train_data_size,
            val_data_size= params.val_data_size
        )

        return data_processing_config
    
    def get_train_model_config(self) -> TrainModelConfig:

        config = self.config.train_model
        params = self.params.model_params

        train_model_config = TrainModelConfig(
            train_data_path= config.train_data_path,
            val_data_path= config.val_data_path,
            save_model_dir= config.save_model_dir,

            model_type = params.model_type,
            model_name = params.model_name,
            epochs = params.epochs,
            train_batch_size = params.train_batch_size,
            val_batch_size = params.val_batch_size
        )

        return train_model_config
    

