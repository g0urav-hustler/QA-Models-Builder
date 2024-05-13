import os
from src.BERT.constants import *
from src.BERT.utils.common import read_yaml, create_directories
from src.BERT.entity.config_entity import DataIngestionConfig


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

        create_directories(config.raw_data_dir)

        data_ingestion_config = DataIngestionConfig(
            raw_data_dir= config.root_raw_data_dir
            data_from_web= config.data_from_web
        )

        return data_ingestion_config
    
