import pandas as pd

from utils.Log import Log
from utils.Query import Query

class DAO:
    """
    DAO (Data Access Object) é uma classe que lida com o carregamento e
    operações básicas em um arquivo CSV contendo dados de primatas.

    Atributos
    ----------
    filename : str
        O nome/caminho do arquivo CSV a ser carregado.
    data : pd.DataFrame ou None
        Um DataFrame contendo os dados carregados, ou None se os dados não foram carregados.
    """

    filename: str
    data: pd.DataFrame | None

    def __init__(self, filename: str) -> None:
        """
        Inicializa o DAO com o nome do arquivo fornecido e tenta
        carregar os dados do arquivo.

        Parâmetros
        ----------
        filename : str
            O nome/caminho do arquivo CSV a ser carregado.
        """
        self.filename = filename
        self.data = None

        try:
            self.data = pd.read_csv(self.filename)
            Log.debug(f"Dados carregados com sucesso de {self.filename}")

        except FileNotFoundError:
            Log.error(f"Arquivo {self.filename} não encontrado.")

        except pd.errors.EmptyDataError:
            Log.error(f"Arquivo {self.filename} está vazio.")

        except pd.errors.ParserError:
            Log.error(f"Arquivo {self.filename} não parece ser um CSV válido.")

        except Exception as err:
            Log.error(f"Ocorreu um erro: {err}")

    def query(self):
        return Query(self.data)
