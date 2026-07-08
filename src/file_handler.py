import csv

class CSVFileHandler:

    def __init__(self, file_path): 
        self.file_path = file_path


    def read_file(self):
        try: 
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                leitor = csv.DictReader(file)
                dados = list(leitor)
            return dados
        
        except FileNotFoundError: 
            print('Arquivo Inexistente')
            return []
        