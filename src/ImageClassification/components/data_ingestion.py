import os
import urllib.request as request
import zipfile

from pathlib import Path
from ImageClassification import logger
from ImageClassification.utils.common import get_size
from ImageClassification.entity.config_entity import DataIngestionConfig
from urllib.error import HTTPError


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if self.config.source_URL and self.config.local_data_file:
            local_data_file_path = Path(self.config.local_data_file)
            if not os.path.exists(local_data_file_path.parent):
                os.makedirs(local_data_file_path.parent, exist_ok=True)
            
            if not os.path.exists(self.config.local_data_file):
                try:
                    filename, headers = request.urlretrieve(
                        url=self.config.source_URL,
                        filename=self.config.local_data_file
                    )
                except HTTPError as e:
                    logger.error(f'HTTP Error: {e}')
                    raise
                except Exception as e:
                    logger.error(f'Error during file download : {e}')
                    raise
            else:
                logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')
        else:
            logger.info('Skipping download, source_URL or local_data_file not provided.')

    # def extract_zip_file(self):
    #     if self.config.unzip_dir and self.config.local_data_file:
    #         unzip_dir_path = Path(self.config.unzip_dir)
    #         if not unzip_dir_path.exists():
    #             os.makedirs(unzip_dir_path, exist_ok=True)
            
    #         if not any(unzip_dir_path.iterdir()):  # Check if Directory is empty
    #             with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #                 zip_ref.extractall(unzip_dir_path)
    #             logger.info(f'Extracted Zip file to {unzip_dir_path}')
    #         else:
    #             logger.info(f'Unzip directory already exists: {unzip_dir_path}')
    #     else:
    #         logger.info('Skipping unzip, unzip_dir or local_data_file not provided.')

    # def extract_zip_file(self):
    #     if self.config.unzip_dir and self.config.local_data_file:
    #         if not os.path.exists(self.config.unzip_dir):
    #             os.makedirs(self.config.unzip_dir, exist_ok=True)
    #             with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #                 zip_ref.extractall(self.config.unzip_dir)
    #         else:
    #             logger.info(f'Unzip directory already exists: {self.config.unzip_dir}')
    #     else:
    #         logger.info('Skipping unzip, unzip_dir or local_data_file not provided.')

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    def setup_local_data(self):
        # Use the / operator to join paths
        self.config.train_dir = Path(self.config.root_dir) / self.config.train_dir
        self.config.validation_dir = Path(self.config.root_dir) / self.config.validation_dir
        self.config.test_dir = Path(self.config.root_dir) / self.config.test_dir

        for path in [self.config.train_dir, self.config.validation_dir, self.config.test_dir]:
            if not os.path.exists(path):
                logger.warning(f'Missing expected directory: {path}')
