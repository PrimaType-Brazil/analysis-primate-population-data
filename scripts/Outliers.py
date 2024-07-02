import pandas as pd

from utils.Log import Log

class Outliers:
    @classmethod
    @Log.track
    def z_score(cls, column: pd.Series):
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
    def interquartile_range(cls, column: pd.Series):
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
