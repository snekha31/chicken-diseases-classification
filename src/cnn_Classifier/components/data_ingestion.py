import os
import zipfile
from pathlib import Path
from cnn_Classifier import logger
from cnn_Classifier.utils.common import get_size, download_file_from_google_drive
from cnn_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not Path(self.config.local_data_file).exists():
            # Build Google Drive direct URL from file ID
            file_id = self.config.source_URL
            url = f"https://drive.google.com/uc?id={file_id}"

            # Use your gdown wrapper to download
            download_file_from_google_drive(url, Path(self.config.local_data_file))

            logger.info(f"Downloaded file to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        if zipfile.is_zipfile(self.config.local_data_file):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}")
        else:
            logger.error(f"File {self.config.local_data_file} is not a valid zip archive")
            raise ValueError("Downloaded file is not a valid zip file")









