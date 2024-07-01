from typing import Union
import pandas as pd
from utils.DAO import DAO
from utils.Log import Log

class DataConsistencyValidator:
    """
    Classe para validar a consistência dos dados em um DataFrame.

    Esta classe oferece métodos para verificar e assegurar a integridade dos dados
    em um DataFrame, identificando entradas vazias e registrando eventuais erros.

    Métodos
    -------
    verify_all_data_entries(data: pd.DataFrame)
        Verifica valores nulos nos dados no DataFrame fornecido.
    verify_column_consistency(data: 'DAO', columns: Union[str, list[str]]) -> bool
        Verifica a consistência dos valores colunas especificadas para cada espécie 
        de primata, tendo fornecido o DAO.
    """

    @classmethod
    @Log.track
    def verify_all_empty_entries(cls, data: pd.DataFrame) -> bool:
        """
        Verifica valores nulos nos dados em um DataFrame.

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

    @classmethod
    @Log.track
    def verify_column_consistency(cls, data: 'DAO', columns: Union[str, list[str]]) -> bool:
        """
        Verifica a consistência dos valores colunas especificadas para cada espécie de primata, 
        tendo fornecido o DAO.

        Este método percorre todas as espécies únicas e verifica se os valores nas colunas 
        especificadas são consistentes para cada ocorrência da espécie.

        Parâmetros
        ----------
        data : DAO
            O DAO contendo os dados a serem verificados.
        columns : str or list[str]
            O nome da coluna ou lista de nomes das colunas a serem verificadas.

        Retorna
        -------
        bool
            True se a verificação for concluída sem erros, False caso contrário.

        Lança
        ------
        Exception
            Se ocorrer um erro durante o processamento dos dados.

        Notas
        -----
        Este método utiliza o método `query` do DAO para realizar a consulta e limita a verificação
        aos primeiros 10 registros de cada espécie para conseguir cada espécie unicamente uma vez.
        Este método não trata exceções internamente, mas as registra usando o logger configurado.

        Exemplo
        -------
        >>> dao = DAO("exemplo.csv")
        >>> DataConsistencyValidator.verify_column_consistency(dao, "habitat_region")
        Valor diferente na linha 10 para a espécie Gorilla na coluna habitat_region
        Valor diferente na linha 20 para a espécie Gorilla na coluna habitat_region
        """
        try:
            if isinstance(columns, str):
                columns = [columns]

            all_species_names = data.query().limit(10).get()["species_name"].values
            had_any_inconsistency: bool = False

            for species_name in all_species_names:
                all_rows = data.query().where("species_name", "==", species_name).get()

                for column in columns:
                    first_value = all_rows.iloc[0][column]

                    for index, row in all_rows.iterrows():
                        if index == 0:
                            continue
                        current_value = row[column]

                        if current_value != first_value:
                            print(f"Valor diferente na linha {index} para a espécie {species_name} na coluna {column}")
                            if (not had_any_inconsistency): 
                                had_any_inconsistency = True
            
            if (not had_any_inconsistency):
                print(f"Nenhum valor inconsistente encontrado.")

            return True

        except Exception as err:
            Log.error(err)
            return False
