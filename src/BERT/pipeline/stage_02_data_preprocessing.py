from src.BERT.config.configuration import ConfigurationManager
from src.BERT.components.data_preprocessing import DataPreprocessing
from src.BERT import logger

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessingPipeline():

    def __init__(self):
        pass
    

    def main(self):
        config = ConfigurationManager()

        data_processing_config = config.get_data_processing_config()

        data_processing = DataPreprocessing(data_processing_config)

        data_processing.get_processed_data()
        data_processing.get_split_data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreprocessingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e