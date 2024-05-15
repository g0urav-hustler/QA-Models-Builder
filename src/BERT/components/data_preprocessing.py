import os
import pandas as pd
from pathlib import Path
from src.BERT.entity.config_entity import DataProcessing
from src.BERT.utils.common import save_json, load_json, join_path

class DataPreprocessing():
    def __init__(self, config = DataProcessing):
        self.config = config

    def find_word_index(self, context, answer):
        for word in answer.split(" "):
            res = context.find(word)
            if res != -1:
                return res
        return -1
    
    def create_json_dataset(self, context_list, question_list, answer_list , ans_start_list):

        data = []
        ids = 1
        
        for i in range(len(context_list)):
            context = context_list[i]
            question = question_list[i]
            answer = answer_list[i]

            if ans_start_list == None:
                if context.find(answer) == -1:
                    ans_start = self.find_word_index(context, answer)
                else:
                    ans_start = context.find(answer)
            else:
                ans_start = ans_start_list[i]

            
            q_a_dict = {
                            "id": str(ids).zfill(5),
                            "is_impossible": False,
                            "question": question,
                            "answers": [
                                {
                                    "text": answer,
                                    "answer_start": int(ans_start),
                                }
                            ]
                    }
            ids = ids + 1

            row_dict = {
                "context" : context,
                "qas": q_a_dict
            }

            data.append(row_dict)

        return data

    
    def get_processed_data(self):

        data_file = os.listdir(self.config.raw_data_dir)[0]

        df = pd.read_csv(data_file, nrows= 10)

        context_list = df[self.config.context_col].to_list()
        question_list = df[self.config.question_col].to_list()
        answer_list = df[self.config.answer_col].to_list()
        answer_start_list = df[self.config.answer_start_col].to_list()

        processed_data = self.create_json_dataset(context_list,question_list, answer_list, answer_start_list)

        save_json(Path(join_path(self.config.processed_data_dir, "processed_data.json")), processed_data)

    
    def get_split_data(self):
        
        processed_data = load_json(Path(join_path(self.config.processed_data_dir, "processed_data.json")))

        train_range = int((100*self.config.train_data_size)/ len(processed_data))
        val_range = int((100*self.config.val_data_size)/ len(processed_data))

        train_data = processed_data[:train_range]
        val_data = processed_data[-(val_range):]

        
        # save training data
        save_json(Path(join_path(self.config.split_data_dir, "train_data.json")), train_data)

        # save val data
        save_json(Path(join_path(self.config.split_data_dir, "val_data.json")), val_data)


        
