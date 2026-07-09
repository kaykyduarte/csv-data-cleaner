class CleaningReport:
    

    def generate_report(self, linhas_originais, after_nulls, after_duplicates):
        nulls_removidos = linhas_originais - after_nulls
        duplicates_removidas = after_nulls - after_duplicates
        linhas_restantes = after_duplicates

        print("========== RELATÓRIO ==========")
        print(f"Linhas originais: {linhas_originais}")
        print(f"Valores nulos removidos: {nulls_removidos}")
        print(f"Duplicatas removidas: {duplicates_removidas}")
        print(f"Linhas restantes: {linhas_restantes}")
        print("===============================")