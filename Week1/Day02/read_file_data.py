from pathlib import Path
import pandas as pd


class DataExtractor():
    def __init__(self,file_path):
        self.file_path=file_path
        
    def read(self):
        path=Path(self.file_path)
        if path.suffix==".csv":
            self._read_csv_file()
        elif path.suffix==".json":
            self._read_json_file()
        else:
            raise ValueError("Invalid file type")
    
    def _read_csv_file(self):
        df=[]
        try:
            df = pd.read_csv(self.file_path)
            print(df)
        except Exception as e:
            raise RuntimeError("Error reading CSV file") from e
        
    def _read_json_file(self):
        data=[]
        
        data=pd.read_json(self.file_path)
        print(data)
        
        
extractor=DataExtractor(r"filepath")
data=extractor.read()
print(data)