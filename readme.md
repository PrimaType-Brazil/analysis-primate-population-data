# Setup

## Instalando o projeto

1. Clonar o repositório;
2. Entrar no diretório do projeto;
3. Ter python3 e pip instalados.

## Rodando o projeto

É necessário ter o `primates_dataset.csv` no diretório `storage/data`.

Se estiver em Linux, rode:

```bash
sudo chmod 775 ./run.sh
```

para dar permissões ao shell que roda o projeto automaticamente.
Rode o shell com:

```bash
./run.sh
```

Esse shell existe pra não precisar rodar `python3 main.py` toda vez, facilitando, mas se for da preferência do usuário, não é necessário usar esse shell.
Ele inclusive instala as dependências automaticamente.

```bash
python3 main.py
```

## Assegurando-se de ter todas as dependências necessárias

O script shell `run.sh` instala as dependências pra você, então, use-o sempre que possível.
Caso queira instalar as dependências você mesmo, use:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` lista as dependências do projeto em um único arquivo pra não ser necessário olhar arquivo por arquivo, ou baixar dependência por dependência.

# Análise de Dados Populacionais de Primatas

## Descrição

Como parte do Sprint 1, sua tarefa é realizar uma análise detalhada dos dados populacionais de diferentes espécies de primatas. Esta tarefa envolve várias etapas fundamentais de ciência de dados, incluindo a coleta, limpeza, análise e visualização dos dados.

Você utilizará a linguagem Python e bibliotecas essenciais para a ciência de dados como NumPy e Pandas para manipular os dados, e Matplotlib ou Seaborn para criar visualizações. A análise deve focar em identificar e ilustrar as tendências populacionais ao longo do tempo para diferentes espécies de primatas.

## Passos Detalhados

1. Coleta de Dados

    - Utilize o dataset fornecido (primates_dataset.csv). Certifique-se de entender a estrutura do dataset e os tipos de dados que ele contém.

2. Limpeza de Dados

    - Verifique se há dados ausentes ou inconsistentes no dataset.
    - Utilize técnicas de manipulação de dados com Pandas para tratar esses problemas, como preenchimento de valores ausentes ou remoção de registros inválidos.

3. Análise de Dados

    - Explore os dados para entender melhor as distribuições e tendências. Isso pode incluir:
        - Resumir as populações médias por espécie.
        - Comparar a população de diferentes espécies ao longo dos anos.

4. Visualização de Dados

    - Crie gráficos que ilustrem as tendências populacionais das espécies ao longo do tempo. Use Matplotlib ou Seaborn para isso.
        - Gráficos de linha para mostrar a mudança populacional ao longo dos anos.
        - Gráficos de barras para comparar populações de diferentes espécies em um ano específico.

5. Documentação e Relatório

    - Compile suas descobertas em um relatório bem-estruturado.
    - O relatório deve incluir:
        - Uma introdução explicando o objetivo da análise.
        - Metodologia usada para a limpeza e análise dos dados.
        - Gráficos criados durante a análise.
        - Insights e conclusões baseadas nos dados analisados.

**Ferramentas Recomendadas**

-   **Python**: Linguagem de programação para realizar toda a análise.
-   **Pandas**: Para manipulação e limpeza dos dados.
-   **NumPy**: Para operações matemáticas e de array.
-   **Matplotlib/Seaborn**: Para visualização de dados.

**Requisitos para Cumprimento da Tarefa**

-   Dataset Limpo: Os dados devem estar livres de inconsistências e prontos para análise.
-   Gráficos de Qualidade: As visualizações devem ser claras, precisas e informativas.
-   Relatório Detalhado: O relatório deve ser bem-escrito, abrangendo todos os aspectos da análise e incluindo todos os gráficos relevantes.
-   Metodologia Clara: Cada etapa do processo (coleta, limpeza, análise, visualização) deve ser claramente documentada.

**Resultado Esperado**

-   Relatório Final: Um documento contendo:
    -   Introdução e objetivo da análise.
    -   Descrição das etapas de limpeza e manipulação de dados.
    -   Gráficos de visualização das tendências populacionais.
    -   Insights e conclusões derivadas dos dados analisados.
-   Código Bem-Documentado: Scripts Python usados para realizar a análise, com comentários explicativos onde necessário.

## Notas Adicionais

-   Certifique-se de seguir boas práticas de programação, como a utilização de comentários e a organização do código em funções.
-   Mantenha seu código e relatório bem-organizados e fáceis de seguir, facilitando futuras análises ou revisões.
