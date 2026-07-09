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
        
    def save_file(self, output_path, dados):
        if not dados:
            return
        with open(output_path, "w", newline= "", encoding="utf-8") as arquivo:
            colunas = dados[0].keys()
            writer = csv.DictWriter(arquivo, fieldnames=colunas)

            writer.writeheader()
            writer.writerows(dados)