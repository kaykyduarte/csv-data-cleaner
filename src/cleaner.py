
class CSVDataCleaner:

    def clean_name(self, dados):
        for linha in dados:
            
            linha["nome"] = linha["nome"].strip().lower().title()
            
        return dados
    
    def clean_city(self, dados):
        for linha in dados:

            linha["cidade"] = linha["cidade"].strip().lower().title()

        return dados