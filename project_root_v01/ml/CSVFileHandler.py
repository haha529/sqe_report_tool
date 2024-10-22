import pandas as pd
from fastapi import UploadFile

class CSVFileHandler:
    def __init__(self, file: UploadFile):
        self.file = file

    def parse_csv(self):
        df = pd.read_csv(self.file.file)
        return df
