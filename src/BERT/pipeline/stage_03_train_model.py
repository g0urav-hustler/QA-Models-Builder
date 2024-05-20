from src.BERT import logger
from src.BERT.config.configuration import ConfigurationManager
from src.BERT.components.train_model import TrainModel


STAGE_NAME = "Train Model Stage"

class TrainModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        train_model_config = config.get_train_model_config()

        train_model = TrainModel(train_model_config)

        train_model.train_model()

        evaluation_metric = train_model.get_eval_metrics()

        return evaluation_metric

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainModelPipeline()
        evaluation_metric = obj.main()
        print("Model Trained.")
        print("Evalutaion Metric = ", evaluation_metric)
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e