import pandas as pd
from utils.DAO import DAO

def main():
    primate: DAO = DAO("storage/data/primates_dataset.csv")
    desired_information: pd.DataFrame = (primate.query()
                                         .where("species_name", "==", "Gorilla")
                                         .order_by("population", ascending=True)
                                         .limit(14)
                                         .get()
                                        )

    print(desired_information)

if __name__ == "__main__":
    main()