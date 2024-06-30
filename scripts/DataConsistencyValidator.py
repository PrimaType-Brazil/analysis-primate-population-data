import pandas as pd
from utils.Log import Log

class DataConsistencyValidator:
    """
    Classe para validar a consistência dos dados em um DataFrame.

    Esta classe oferece métodos para verificar e assegurar a integridade dos dados
    em um DataFrame, identificando entradas vazias e registrando eventuais erros.

    Métodos
    -------
    verify_all_data_entries(data: pd.DataFrame)
        Verifica a consistência dos dados no DataFrame fornecido.
    """

    @classmethod
    @Log.track
    def verify_all_data_entries(cls, data: pd.DataFrame) -> bool:
        """
        Verifica a consistência dos dados em um DataFrame.

        Este método percorre todas as entradas do DataFrame fornecido e imprime uma mensagem
        indicando as posições onde valores vazios são encontrados.

        É contado quantas linhas foram detectadas com valores ausentes, pulando processamento
        desnecessário se for 0 (nenhuma linha).

        Na mostragem ao final do processamento, é somado 1 ao índice da linha pra contar o
        cabeçalho.

        Parâmetros
        ----------
        data : pd.DataFrame
            O DataFrame contendo os dados a serem verificados.

        Retorna
        -------
        bool
            True se o processamento ocorreu corretamente, False se algo deu errado.

        Lança
        ------
        Exception
            Se ocorrer um erro durante o processamento dos dados.

        Notas
        -----
        Este método não trata exceções internamente, mas as registra usando o logger configurado.

        Exemplo
        -------
        >>> data = pd.DataFrame({'A': [1, 2, None], 'B': ['x', None, 'z']})
        >>> DataConsistencyValidator.verify_all_data_entries(data)
        Vazio encontrado na linha 1, coluna 'B'
        Vazio encontrado na linha 2, coluna 'A'
        """

        try:
            na_positions: pd.DataFrame = data.isna()

            how_many_empty_values_found: int = na_positions.values.sum()

            if (how_many_empty_values_found == 0):
                print("Nenhum valor vazio encontrado.")
                return True

            for row_index, row_name in na_positions.iterrows():
                for column_name in na_positions.columns:
                    if row_name[column_name]:
                        print(f"Vazio encontrado na linha {row_index + 1}, coluna '{column_name}'")
            return True

        except Exception as err:
            Log.error(err)
            return False
