from utils.DAO import DAO
from scripts.DataConsistencyValidator import DataConsistencyValidator

def main():
    primate_raw: DAO = DAO("storage/data/raw/primates_dataset.csv")

    DataConsistencyValidator.verify_all_data_entries(primate_raw.data)
    print(primate_raw.query().where("species_name", "==", "Orangutan").get())

    primate_filled: DAO = DAO("storage/data/processed/primates_dataset_filled.csv")

    DataConsistencyValidator.verify_all_data_entries(primate_filled.data)
    print(primate_filled.query().where("species_name", "==", "Orangutan").get())

if __name__ == "__main__":
    main()