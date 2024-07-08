from matplotlib import pyplot as plt
import numpy as np

class Graph:
    """
    Super-classe para criar e gerenciar gráficos básicos utilizando matplotlib.

    Esta classe permite criar uma base pra classes que geram gráficos personalizados com 
    títulos, rótulos de eixos e estilos padrão de formatação.

    Atributos
    ---------
    title (str): Título do gráfico.
    x_axis (tuple[str, list[any]]): Tupla contendo o rótulo e os dados do eixo x.
    y_axis (tuple[str, list[any]]): Tupla contendo o rótulo e os dados do eixo y.

    Métodos
    -------
    _default_styles() -> None:
        Aplica estilos padrão ao gráfico, incluindo layout ajustado, grade e margens.

    _load_labels() -> None:
        Define o título, rótulo do eixo x e rótulo do eixo y para o gráfico.

    _y_spacing() -> None:
        Ajusta o espaçamento dos ticks do eixo y com base no valor máximo nos dados do eixo y.

    show() -> None:
        Exibe o gráfico na interface gráfica.

    save() -> None:
        Salva o gráfico como um arquivo de imagem no diretório apropriado.
    """

    title: str
    x_axis: tuple[str, list[any]]
    y_axis: tuple[str, list[any]]

    def __init__(self, title: str, x_axis: tuple[str, list[any]], y_axis: tuple[str, list[any]]) -> None:
        self.title = title
        self.x_axis = x_axis
        self.y_axis = y_axis

    def __del__(self) -> None:
        plt.close()

    def _default_styles(self) -> None:
        """
        Aplica estilos padrão ao gráfico, incluindo layout ajustado, grade e margens.
        """

        plt.tight_layout()
        plt.grid(True)
        plt.margins(x = 0.025, y = 0.05)
        plt.subplots_adjust(top=0.95, bottom=0.08, left=0.08, right=0.95)

    def _load_labels(self) -> None:
        """
        Define o título, rótulo do eixo x e rótulo do eixo y para o gráfico.
        """

        plt.title(self.title)
        plt.xlabel(self.x_axis[0])
        plt.ylabel(self.y_axis[0])

    def _y_spacing(self) -> None:
        """
        Ajusta o espaçamento dos ticks do eixo y com base no valor máximo nos dados do eixo y.
        """

        max_value: int = max(self.y_axis[1])
        tick_spacing: int = max(50, int(np.ceil(max_value / 10)))

        plt.yticks(range(0, max_value + tick_spacing, tick_spacing))

    def show(self) -> None: ...
    def save(self) -> None: ...
    