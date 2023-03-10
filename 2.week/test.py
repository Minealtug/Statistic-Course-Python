import numpy as np
import  pandas as pd

class Samples:
    def __init__(self,cvs_file,delimiter=";") :
        self.cvs_file=cvs_file
        self.delimiter=delimiter
        self.df=pd.read_csv(self.cvs_file,delimiter=self.delimiter)