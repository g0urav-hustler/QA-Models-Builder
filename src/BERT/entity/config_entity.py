from dataclasses import dataclass
from pathlib import Path

# data ingestion class
@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_dir : Path
    web_data_dir : Path


# data preprocessing class
@dataclass(frozen= True)
class DataProcessing:
    raw_data_dir: Path
    processed_data_dir : Path
    split_data_dir : Path

    context_col: str
    question_col : str
    answer_col : str
    answer_start_col : str

    train_data_size: float
    val_data_size: float

# train model class
@dataclass(frozen= True)
class TrainModelConfig:
    train_data_path: Path 
    val_data_path: Path
    save_model_dir: Path
    model_type : str
    model_name : str
    epochs : int
    train_batch_size : int
    val_batch_size : int