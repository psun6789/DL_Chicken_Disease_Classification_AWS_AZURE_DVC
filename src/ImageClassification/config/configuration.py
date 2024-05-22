import yaml
from pathlib import Path
from ImageClassification.utils.common import read_yaml, create_directories
from ImageClassification.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from ImageClassification.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH):

        self.config_filepath = config_filepath  # Store config filepath as attribute
        self.params_filepath = params_filepath

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        with open(self.config_filepath, 'r') as file:
            self.config = yaml.safe_load(file)

        data_root_path = Path(self.config['data_root_path'])
        data_ingestion = self.config['data_ingestion']

        return DataIngestionConfig(
        root_dir=Path(data_ingestion['root_dir']),
        train_dir=data_root_path / data_ingestion['train_dir'],
        validation_dir=data_root_path / data_ingestion['validation_dir'],
        test_dir=data_root_path / data_ingestion['test_dir'],
        source_URL=data_ingestion['source_URL'],
        local_data_file=data_root_path / data_ingestion['local_data_file'],
        unzip_dir=data_root_path / data_ingestion['unzip_dir']
        )

