import pandas as pd

from utils.Log import Log

class Query:
    """
    Classe para realizar consultas fluentes em um DataFrame do pandas.

    Métodos
    -------
    where(column: str, operator: str, value: any) -> 'Query'
        Aplica um filtro à consulta.
    order_by(column: str, ascending: bool = True) -> 'Query'
        Ordena os resultados da consulta.
    limit(how_much: int) -> 'Query'
        Limita o número de resultados.
    get() -> pd.DataFrame
        Retorna o DataFrame resultante da consulta.
    """

    _data: pd.DataFrame
    _query: pd.DataFrame

    def __init__(self, data_frame: pd.DataFrame) -> None:
        self._data = data_frame
        self._query = data_frame

    def where(self, column: str, operator: str, value: any) -> 'Query':
        """
        Aplica um filtro à consulta.

        Parâmetros
        ----------
        column : str
            A coluna a ser filtrada.
        operator : str
            O operador de comparação ('==', '!=', '>', '>=', '<', '<=').
        value : any
            O valor a ser comparado.

        Retorna
        -------
        Query
            A instância atual da classe para permitir o encadeamento de métodos.

        Lança
        ------
        ValueError
            Se o operador não for um dos seguintes: '==', '!=', '>', '>=', '<', '<='.
        """

        match operator:
            case "==":
                self._query = self._query[self._query[column] == value]
            case "!=":
                self._query = self._query[self._query[column] != value]
            case ">":
                self._query = self._query[self._query[column] > value]
            case "<":
                self._query = self._query[self._query[column] < value]
            case ">=":
                self._query = self._query[self._query[column] >= value]
            case "<=":
                self._query = self._query[self._query[column] <= value]
            case _:
                error_message: str = f"Um operador foi usado no where(), que não é compatível: {operator}. Deve ser um destes: ==, !=, >, >=, <, <="
                Log.error(error_message)
                raise ValueError(error_message)
        return self

    def order_by(self, column: str, ascending: bool = False):
        """
        Ordena os resultados da consulta.

        Parâmetros
        ----------
        column : str
            A coluna pela qual ordenar.
        ascending : bool, opcional
            Se True, ordena em ordem ascendente. Se False, descendente. O padrão é True.

        Retorna
        -------
        Query
            A instância atual da classe para permitir o encadeamento de métodos.
        """

        self._query = self._query.sort_values(by = column, ascending = ascending)
        return self

    def limit(self, how_much: int):
        """
        Limita o número de resultados na consulta.

        Parâmetros
        ----------
        how_much : int
            O número máximo de resultados a serem retornados.

        Retorna
        -------
        Query
            A instância atual da classe para permitir o encadeamento de métodos.
        """

        self._query = self._query.head(how_much)
        return self

    def get(self) -> pd.DataFrame:
        """
        Retorna o DataFrame resultante da consulta.

        Retorna
        -------
        pd.DataFrame
            O DataFrame filtrado e modificado.
        """

        return self._query
