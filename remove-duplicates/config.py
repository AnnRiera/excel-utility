import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
load_dotenv()

class Config():

    SOURCE_FOLDER: str = os.environ['SOURCE_FOLDER']
    FILE_NAME: str = os.environ['FILE_NAME']
    RESULT_FILE: str = os.environ['RESULT_FILE']
    REGEX_PATTERN: str = os.environ['REGEX_PATTERN']

    @property
    def SOURCE_FILE(self) -> str:
        return BASE_DIR / self.SOURCE_FOLDER / self.FILE_NAME

    @property
    def TARGET_FILE(self) -> str:
        return BASE_DIR / self.SOURCE_FOLDER / self.RESULT_FILE

config = Config()
