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

            if (how_many_outliers == 0):
                print("Nenhuma anomalia encontrada.")
                return True
            
            for row_index in outliers[outliers].index:
                print(f"Anomalia encontrada na linha {row_index}")
            return True

        except Exception as err:
            Log.error(err)
            return False
