from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

from scripts.components.Graph import Graph

class BarGraph(Graph):
    """
    Classe para criar gráficos de barras utilizando seaborn.

    Esta classe estende a classe Graph para gerar gráficos de barras usando seaborn,
    permitindo personalização adicional de paleta de cores e agrupamento por categorias.

    Atributos
    ---------
    title (str): Título do gráfico.
    x_axis (tuple[str, list]): Tupla contendo o rótulo e os dados do eixo x.
    y_axis (tuple[str, list]): Tupla contendo o rótulo e os dados do eixo y.

    Métodos:
    _bar() -> None:
        Gera o gráfico de barras usando seaborn com os dados fornecidos.

    show() -> None:
        Exibe o gráfico de barras na interface gráfica.

    save() -> None:
        Salva o gráfico de barras como um arquivo de imagem no diretório apropriado.

    Exemplo de Uso:
    >>> x_data = ("Categorias", ["A", "B", "C"])
    >>> y_data = ("Valores", [10, 20, 30])
    >>> bar_graph = BarGraph("Exemplo de Gráfico de Barras", x_data, y_data)
    >>> bar_graph.show()
    """

    def __init__(self, title: str, x_axis: tuple[str, list], y_axis: tuple[str, list]) -> None:
        super().__init__(title, x_axis, y_axis)

    def _bar(self) -> None:
        """
        Gera o gráfico de barras usando seaborn com os dados fornecidos.
        """

        plt.figure(figsize=(12, 6))
        sns.barplot(
            x = self.x_axis[1],
            y = self.y_axis[1],
            hue = self.x_axis[0],
            palette = "crest",
            legend = False,
            dodge = False,
            data = pd.DataFrame({
                self.x_axis[0]: self.x_axis[1],
                self.y_axis[0]: self.y_axis[1]
            }),
        )
        self._default_styles()
        self._y_spacing()
        self._load_labels()

    def show(self) -> None:
        """
        Exibe o gráfico de barras na interface gráfica.
        """

        self._bar()
        plt.show()

    def save(self) -> None:
        """
        Salva o gráfico de barras como um arquivo de imagem no diretório apropriado.
        """

        self._bar()
        title_formatted: str = self.title.replace(" ", "_").lower()
        plt.savefig(f"images/barra_{title_formatted}.png")
    