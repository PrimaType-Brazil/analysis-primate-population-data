from utils.DAO import DAO
from scripts.DataConsistencyValidator import DataConsistencyValidator
from scripts.Outliers import Outliers

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
    DataConsistencyValidator.verify_column_consistency(primate_filled, ["habitat_region", "diet", "social_behavior", "genetic_variation", "health_status", "latitude", "longitude"])

    # Procurando por outliers
    Outliers.z_score(primate_filled.data["population"])

if __name__ == "__main__":
    main()