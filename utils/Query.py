import pandas as pd

from utils.Log import Log

class Query:
    """
    Class to perform fluent queries on a pandas DataFrame.

    Methods
    -------
    where(column: str, operator: str, value: any) -> 'Query'
        Applies a filter to the query.
    order_by(column: str, ascending: bool = True) -> 'Query'
        Sorts the query results.
    limit(how_much: int) -> 'Query'
        Limits the number of results.
    get() -> pd.DataFrame
        Returns the resulting DataFrame from the query.
    """

    _data: pd.DataFrame
    _query: pd.DataFrame

    def __init__(self, data_frame: pd.DataFrame) -> None:
        self._data = data_frame
        self._query = data_frame

    def where(self, column: str, operator: str, value: any) -> 'Query':
        """
        Applies a filter to the query.

        Parameters
        ----------
        column : str
            The column to be filtered.
        operator : str
            The comparison operator ('==', '!=', '>', '>=', '<', '<=').
        value : any
            The value to be compared.

        Returns
        -------
        Query
            The current instance of the class to allow method chaining.

        Raises
        ------
        ValueError
            If the operator is not one of the following: '==', '!=', '>', '>=', '<', '<='.
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
                error_message: str = f"An operator was used for where(), which is not compatible: {operator}. should be any of these: ==, !=, >, >=, <, <="
                Log.error(error_message)
                raise ValueError(error_message)
        return self

    def order_by(self, column: str, ascending: bool = False):
        """
        Sorts the query results.

        Parameters
        ----------
        column : str
            The column to sort by.
        ascending : bool, optional
            If True, sort in ascending order. If False, descending. Default is True.

        Returns
        -------
        Query
            The current instance of the class to allow method chaining.
        """

        self._query = self._query.sort_values(by = column, ascending = ascending)
        return self

    def limit(self, how_much: int):
        """
        Limits the number of results in the query.

        Parameters
        ----------
        how_much : int
            The maximum number of results to return.

        Returns
        -------
        Query
            The current instance of the class to allow method chaining.
        """

        self._query = self._query.head(how_much)
        return self

    def get(self) -> pd.DataFrame:
        """
        Returns the resulting DataFrame from the query.

        Returns
        -------
        pd.DataFrame
            The filtered and modified DataFrame.
        """

        return self._query