import pandas as pd
from numpy import ndarray
from models.Primate import Primate
from models.factories.PrimateFactory import PrimateFactory
from utils.DAO import DAO
from scripts.DataConsistencyValidator import DataConsistencyValidator
from scripts.Outliers import Outliers
from scripts.BarGraph import BarGraph

def main():
    # Recomenda-se que leia o relatório final como acompanhamento ao código.

    # Dados não editados
    primate_raw: DAO = DAO("storage/data/raw/primates_dataset.csv")

    # Encontrando quantos valores vazios existem
    DataConsistencyValidator.verify_all_empty_entries(primate_raw.data)

    # Exibindo todas as linhas sobre Orangotangos, mostrando como falta dois dados quanto à população
    print(primate_raw.query().where("species_name", "==", "Orangutan").get())

    # Foi criado uma base de dados idêntica à anterior, mas sem os valores vazios, preenchidos à mão
    primate_filled: DAO = DAO("storage/data/processed/primates_dataset_filled.csv")

    # Mostrando como não há mais dados vazios
    DataConsistencyValidator.verify_all_empty_entries(primate_filled.data)
    print(primate_filled.query().where("species_name", "==", "Orangutan").get())

    # Verificando consistência de valores fixos
    unique_row_name: str = "species_name"
    all_species_names: ndarray = primate_filled.query().limit(10).get()[unique_row_name].values
    DataConsistencyValidator.verify_column_consistency(unique_row_name, all_species_names, primate_filled, ["habitat_region", "diet", "social_behavior", "genetic_variation", "health_status", "latitude", "longitude"])

    # Procurando por outliers
    Outliers.z_score(primate_filled.data["population"])
    Outliers.z_score(primate_filled.data["avg_lifespan"])
    Outliers.interquartile_range(primate_filled.data["population"])
    Outliers.interquartile_range(primate_filled.data["avg_lifespan"])

    # Organizando todas as espécies de primatas em uma estrutura de dados adaptada
    structured_primates: list[Primate] = []
    all_primates: pd.DataFrame = primate_filled.query().limit(10).get()
    for _, row in all_primates.iterrows():
        structured_primates.append(PrimateFactory.create_primate(row, primate_filled))

    # Exibindo e salvando os gráficos referentes às populações
    for primate in structured_primates:
        print(primate)
        species_name: str = primate.species_name
        population: dict[str, list[int, int]] = primate.population

        years: list[str] = list(population.keys())[::-1]
        population_values: list[int] = [pop_data[0] for pop_data in population.values()][::-1]
        # Não está sendo usado o segundo valor (avg_lifespan) por hora.

        bar_graph: BarGraph = BarGraph(f"População de {species_name}", ("Anos", years), ("População", population_values))
        bar_graph.show()
        bar_graph.save()

if __name__ == "__main__":
    main()
