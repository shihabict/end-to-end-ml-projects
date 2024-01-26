import os


# change the project directory
# print(os.getcwd())
os.chdir('../')
# print(os.getcwd())
from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# if __name__ == '__main__':
