from file_handler import CSVFileHandler
from cleaner import CSVDataCleaner
from report import CleaningReport

file_handler = CSVFileHandler("data/raw/dirty_dataset.csv")
cleaner = CSVDataCleaner()
report = CleaningReport()

arquivo_lido = file_handler.read_file()
linhas_originais = len(arquivo_lido)

dados_finais, after_nulls, after_duplicates = cleaner.clean_all(arquivo_lido)

report.generate_report(linhas_originais, after_nulls, after_duplicates)

file_handler.save_file("data/processed/clean_dataset.csv", dados_finais)
