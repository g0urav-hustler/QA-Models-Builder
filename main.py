from src.BERT import logger
from src.BERT.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.BERT.pipeline.stage_02_data_preprocessing import DataPreprocessingPipeline    
from src.BERT.pipeline.stage_03_train_model import TrainModelPipeline                                                


class InvokePipeline:
    def __init__(self):
        pass

    def main(self):

        STAGE_NAME = "Data Ingestion Stage"

        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e


        STAGE_NAME = "Data Preprocessing Stage"

        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataPreprocessingPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        
        # for temporary execution
        return {'correct': 0, 'similar': 1, 'incorrect': 2, 'eval_loss': -0.3109431862831116}


        # STAGE_NAME = "Train Model Stage"

        # try:
        #     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        #     obj = TrainModelPipeline()
        #     evaluation_metric = obj.main()
        #     return evaluation_metric
        #     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        # except Exception as e:
        #     logger.exception(e)
        #     raise e
        
if __name__ == '__main__':
    try:
        obj = InvokePipeline()
        result = obj.main()
        print("Train Model results", result)
    except Exception as e:
        logger.exception(e)
        raise e