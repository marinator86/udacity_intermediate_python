from typing import List
import pandas

from .ImportInterface import ImportInterface
from .Cat import Cat

class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception(f"cannot ingest {path}")
        
        cats = []
        df = pandas.read_csv(path, header=0)
        
        for i, row in df.iterrows():
            cats.append(Cat(row['Name'],row['Age'],row['isIndoor']))
        
        return cats