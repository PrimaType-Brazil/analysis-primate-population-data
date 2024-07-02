import pandas as pd

from utils.Log import Log

class Outliers:
    """
    A classe Outliers oferece métodos para detectar anomalias em colunas de um DataFrame utilizando
    diferentes técnicas estatísticas.

    Métodos
    -------
    z_score(column: pd.Series) -> bool
        Calcula o Z-Score para os valores de uma coluna e identifica anomalias.
    interquartile_range(column: pd.Series) -> bool
        Calcula o Intervalo Interquartil (IQR) para os valores de uma coluna e identifica anomalias.
    """

    @classmethod
    @Log.track
    def z_score(cls, column: pd.Series) -> bool:
        """
        Calcula o Z-Score para os valores de uma coluna e identifica anomalias.

        Este método calcula o Z-Score para cada valor na coluna fornecida e imprime mensagens
        indicando as posições onde anomalias (valores cujo Z-Score absoluto é maior que 3) são encontradas.

        Parâmetros
        ----------
        column : pd.Series
            A coluna cujos valores serão analisados para identificar anomalias.

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
        Este método não trata exceções internamente, mas as registra usando o logger configurado.

        Exemplo
        -------
        >>> data = pd.DataFrame({'A': [1, 2, 3, 4, 100]})
        >>> DataConsistencyValidator.z_score(data['A'])
        Anomalia encontrada na linha 4 coluna A
        100
        """

        try:
            mean: float = column.mean()
            standard_deviation: float = column.std()

            z_score: pd.Series = (column - mean) / standard_deviation

            outliers: pd.Series = z_score.abs() > 3
            how_many_outliers: int = outliers.values.sum()

            if how_many_outliers == 0:
                print(f"Nenhuma anomalia encontrada na coluna {column.name} usando a métrica de Z-Score.")
                return True

            for row_index in outliers[outliers].index:
                print(f"Anomalia encontrada na linha {row_index} coluna {column.name}")
                print(column[row_index])
            return True

        except Exception as err:
            Log.error(err)
            return False

    @classmethod
    @Log.track
    def interquartile_range(cls, column: pd.Series) -> bool:
        """
        Calcula o Intervalo Interquartil (IQR) para os valores de uma coluna e identifica anomalias.

        Este método calcula o IQR para a coluna fornecida e imprime mensagens indicando
        as posições onde anomalias (valores fora do intervalo [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]) são encontradas.

        Parâmetros
        ----------
        column : pd.Series
            A coluna cujos valores serão analisados para identificar anomalias.

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
        Este método não trata exceções internamente, mas as registra usando o logger configurado.

        Exemplo
        -------
        >>> data = pd.DataFrame({'A': [1, 2, 3, 4, 100]})
        >>> DataConsistencyValidator.interquartile_range(data['A'])
        Anomalia positiva encontrada na linha 4 coluna A
        100
        """

        try:
            q1: float = column.quantile(0.25)
            q3: float = column.quantile(0.75)
            iqr: float = q3 - q1

            outliers_negative: pd.Series = column < (q1 - 1.5 * iqr)
            outliers_positive: pd.Series = column > (q3 + 1.5 * iqr)
            how_many_outliers: int = outliers_negative.values.sum() + outliers_positive.values.sum()

            if how_many_outliers == 0:
                print(f"Nenhuma anomalia encontrada na coluna {column.name} usando a métrica de IQR.")

            for row_index in outliers_negative[outliers_negative].index:
                print(f"Anomalia negativa encontrada na linha {row_index} coluna {column.name}")

            for row_index in outliers_positive[outliers_positive].index:
                print(f"Anomalia positiva encontrada na linha {row_index} coluna {column.name}")
                print(column[row_index])

            return True

        except Exception as err:
            Log.error(err)
            return False
