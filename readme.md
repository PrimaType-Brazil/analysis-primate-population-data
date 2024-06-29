# Setup

## Instalando o projeto

1. Clonar o repositório;
2. Entrar no diretório do projeto;
3. Ter Python 3.10 (ou superior) e pip instalados;
4. (OPCIONAL): Ter Poetry instalado para gerenciamento das dependências.

### Instalação do Poetry

Caso não tenha o Poetry instalado, siga as instruções em [Poetry](https://python-poetry.org/docs/#installation).

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

Esse shell instala automaticamente as dependências do projeto de acordo com a sua preferência: se você quiser usar pip (package manager padrão do python) ou Poetry (package manager mais avançado).
Ele salva suas preferências criando um arquivo .config.
Se você prefere não usar um package manager, ou souber exatamente o que está fazendo, pode rodar o projeto com:

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

# O que foi feito até agora?

No processo de análise de dados, precisamos seguir alguns passos pra assegurar a precisão e concisão da análise. Dentre esses passos, destaca-se o EDA (Exploratory Data Analysis, ou Análise Exploratória de Dados). O objetivo do EDA é compreender melhor os dados, suas características, e garantir sua integridade antes de aplicar técnicas avançadas de análise ou modelagem.

### I. - Coleta de Dados

A princípio, coletamos os dados que serão analisados. No escopo desse projeto, é o primates_dataset.csv, um arquivo CSV, mas poderiam também ser extraídos de um banco de dados, APIs, dentre outras fontes.

Com o intuito de facilitar a visualização dos dados, foi criado uma classe de utilidade chamada **Query**. Essa classe é responsável por tratar o CSV como um banco de dados relacional, trazendo suporte à consultas em formato similar à ORMs como TypeORM, SQLAlchemy, Eloquent, dentre outros. Pra se parecer com a sintaxe de ORMs, a classe tem métodos encadeáveis que visam a padronização do SQL padrão ANSI.

### II. - Análise das variáveis

Em segundo passo, conhecemos as variáveis. Entender o que cada uma delas representa, suas unidades de medida. Essa etapa pode envolver tanto análise do próprio cientista de dados quanto de leitura da documentação dos dados, se disponível, à fim de obter mais contexto sobre como os dados foram coletados, e suas limitações.

#### II.1 - Quais são as variáveis disponíveis?

O CSV contém as colunas:

-   species_id -> Identificador de cada linha de 1 a 150;
-   species_name -> Nome da espécie de primata. São elas:
    -   Gorilla;
    -   Chimpanzee;
    -   Orangutan;
    -   Gibbon;
    -   Bonobo;
    -   Lemur;
    -   Tarsier;
    -   Howler Monkey;
    -   Spider Monkey;
    -   Macaque.

Todos os dados a seguir são referentes à devida espécie correspondente (na mesma linha).

-   population -> Quantidade de espécimes vivos.
-   year -> referente à qual ano é a informação dessa linha. Os anos vão de 2020 até 2006.
-   habitat_region -> Região em que habita a espécie. São elas:
    -   Central Africa;
    -   West Africa;
    -   Madagascar;
    -   Southeast Asia;
    -   East Asia;
    -   South America.
-   diet -> A dieta da espécie de primata. Pode ser:
    -   Herbivore;
    -   Omnivore;
    -   Frugivore;
    -   Insectivore.
-   avg_lifespan -> Um valor que representa quantos anos é o tempo de vida médio de um espécime.
-   social_behavior -> O comportamento social das espécies. Pode ser:
    -   Group;
    -   Solitary;
    -   Pair.
-   genetic_variation -> A variação genética da espécie.
-   health_status -> Classificação que indica o quão ameaçada de extinção está a espécie. São possíveis valores:
    -   Healthy;
    -   Near Threatened.
    -   Vulnerable;
    -   Endangered;
    -   Critically Endangered;
-   latitude -> A coordenada latitudinal da região em que habita a espécie.
-   longitude -> A coordenada longitudinal da região em que habita a espécie.

#### II.2 - Questionamentos referentes às variáveis

Dos dados reunidos acima, é possível inferir sobre cada um deles seus tipos primitivos. No entanto, dois levantam o questionamento: genetic_variation e health_status.

##### II.2.1 - genetic_variation

A variável genetic_variation implica variação genética da espécie, mas variação à oque? De acordo com [algumas informações](https://humanorigins.si.edu/evidence/genetics#:~:text=The%20DNA%20difference%20with%20gorillas,Asian%20great%20ape%2C%20the%20orangutan.), os valores batem com a variação genética do gene da espécie referente o gene humano. Mas nas mesmas fontes, outros valores são providenciados, e discutir a veracidade do fornecido pelo CSV é plausível.

##### II.2.2 - health_status

Podemos inferir que esses valores se referem à classificação determinada pela [União Internacional pela Conservação da Natureza](https://www.iucn.org/)União Internacional pela Conservação da Natureza. Na amostragem dos dados II.1, os dados referentes à variável "health_status" já estão em ordem (de cima pra baixo) pra mais próxima da extinção.

##### II.2.3 - latitude & longitude

Em primeira instância uma pessoa poderia se perguntar aonde se referem as coordenadas fornecidas em cada linha. Elas levam para a localização indicada pela variável "habitat_region". Cabe à etapa de limpeza dos dados verificar se isso é verossímil pra todas as linhas.

#### II.3 - Transformação das variáveis

É uma etapa importante da análise pós-coleta de dados que verifiquemos quais variáveis possuem mais correlação com o que desejamos. Para o escopo do projeto atual, percebe-se que as variáveis estão satisfatórias com sua exibição, talvez por exceção de "genetic_variation", que, ao invés de um float entre 0.00 à 0.10, poderia ser uma porcentagem. Depende de cada cientista. Além disso, a separação de dois campos "latitude" e "longitude" pode desagradar quem preferisse um único campo "coordinates".

O projeto ainda está interminado.
Segue abaixo o edital do desafio.

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
