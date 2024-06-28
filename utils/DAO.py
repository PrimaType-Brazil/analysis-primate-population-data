import pandas as pd

from utils.Log import Log
from utils.Query import Query

class DAO:
    """
    DAO (Data Access Object) is a class that handles loading and
    basic operations on a CSV file containing primate data.

    Attributes
    ----------
    filename : str
        The name/path of the CSV file to be loaded.
    data : pd.DataFrame or None
        A DataFrame containing the loaded data, or None if the data is not loaded.
    """

    filename: str
    data: pd.DataFrame | None

    def __init__(self, filename: str) -> None:
        """
        Initializes the DAO with the given filename and attempts
        to load the data from the file.

        Parameters
        ----------
        filename : str
            The name/path of the CSV file to be loaded.
        """
        self.filename = filename
        self.data = None

        try:
            self.data = pd.read_csv(self.filename)
            Log.debug(f"Data loaded successfully from {self.filename}")

        except FileNotFoundError:
            Log.error(f"File {self.filename} not found.")

        except pd.errors.EmptyDataError:
            Log.error(f"File {self.filename} is empty.")

        except pd.errors.ParserError:
            Log.error(f"File {self.filename} does not appear to be a valid CSV.")

        except Exception as err:
            Log.error(f"An error occurred: {err}")

    def query(self):
        return Query(self.data)