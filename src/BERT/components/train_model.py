from src.BERT.entity.config_entity import TrainModelConfig
from simpletransformers.question_answering import QuestionAnsweringModel

class TrainModel:
    def __init__(self, config = TrainModelConfig):
        self.config = config

    def train_model(self):
        config = self.config

        training_args = {
            "num_train_epochs": config.epochs,
            "train_batch_size": config.train_batch_size,
            "eval_batch_size": config.val_batch_size,
            "max_seq_length": 128,
            "output_dir": config.save_model_dir,
            "use_cuda" : False,
            "overwrite_output_dir": True,
        }


        model = QuestionAnsweringModel(
                    config.model_type,
                    config.model_name, 
                    args=training_args,
                    use_cuda = False
        )

        model.train_model(config.train_data_path)

