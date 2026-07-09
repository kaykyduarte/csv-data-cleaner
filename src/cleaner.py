

class CSVDataCleaner:

    def clean_name(self, dados):
        for linha in dados:
            
            linha["nome"] = linha["nome"].strip().lower().title()
            
        return dados
    
    def clean_city(self, dados):
        for linha in dados:

            linha["cidade"] = linha["cidade"].strip().lower().title()

        return dados
    
    def remove_nulls(self, dados):
        lista_limpa = []
        colunas_obrigatorias = ["nome", "idade", "cidade"]
        
        for linha in dados:

            if all(linha.get(coluna) is not None and str(linha.get(coluna)).strip() != "" for coluna in colunas_obrigatorias):
                    lista_limpa.append(linha)
            
                 
        return lista_limpa
    
    def remove_duplicates(self, dados):
        lista_limpa = []
        chaves_vistas = set()

        for linha in dados:
              assinatura = (linha["nome"], linha["idade"], linha["cidade"])

              if assinatura not in chaves_vistas:
                   lista_limpa.append(linha)
                   chaves_vistas.add(assinatura)

        return lista_limpa
    
    def clean_all(self, dados):
        dados = self.clean_name(dados)
        dados = self.clean_city(dados)

        dados = self.remove_nulls(dados)
        after_nulls = len(dados)

        dados = self.remove_duplicates(dados)
        after_duplicates = len(dados)

        return dados, after_nulls, after_duplicates