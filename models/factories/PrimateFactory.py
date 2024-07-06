import pandas as pd
from utils.Types import Species, HabitatRegion, Diet, SocialBehavior, HealthStatus
from utils.Log import Log
from models.Primate import Primate
from typing import get_args

class PrimateFactory:
    @staticmethod
    def create_primate(row: pd.Series, primate_data: pd.DataFrame) -> Primate:     
        current_primate: pd.DataFrame = primate_data.query().where("species_name", "==", row["species_name"]).get()

        population: dict[str, list[int, float]] = {
            str(year): [population, lifespan] for year, population, lifespan in zip(
                current_primate["year"],
                current_primate["population"],
                current_primate["avg_lifespan"]
            )
        }

        structured_primate_data = {
            "species_name": row["species_name"],
            "habitat_region": row["habitat_region"],
            "population": population,
            "diet": row["diet"],
            "social_behavior": row["social_behavior"],
            "genetic_variation": row["genetic_variation"],
            "health_status": row["health_status"],
            "coordinates": (row["latitude"], row["longitude"])
        }

        PrimateFactory.validate_inputs(structured_primate_data)
        primate: Primate = Primate(**structured_primate_data)

        return primate

    @staticmethod
    def validate_inputs(primate_data: any):
        required_keys = [
            "species_name", "habitat_region", "population", "diet",
            "social_behavior", "genetic_variation", "health_status", "coordinates"
        ]

        missing_keys = [key for key in required_keys if key not in primate_data]
        if missing_keys:
            error_message = f"Dados ausentes na estrutura de dados fornecida pra criação de Primate: {', '.join(missing_keys)}"
            Log.error(error_message)
            raise KeyError(error_message)

        if primate_data["species_name"] not in get_args(Species):
            error_message: str = f"Esperado que species_name seja do tipo Species, mas recebeu {type(primate_data['species_name']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if primate_data["habitat_region"] not in get_args(HabitatRegion):
            error_message: str = f"Esperado que habitat_region seja do tipo HabitatRegion, mas recebeu {type(primate_data['habitat_region']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if not isinstance(primate_data["population"], dict):
            error_message: str = f"Esperado que population seja do tipo dict, mas recebeu {type(primate_data['population']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if not all(isinstance(key, str) and isinstance(value, list) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int) for key, value in primate_data["population"].items()):
            error_message: str = "Esperado que population seja do tipo dict com chaves como str e valores como list[int, int]"
            raise ValueError(error_message)
        if primate_data["diet"] not in get_args(Diet):
            error_message: str = f"Esperado que diet seja do tipo Diet, mas recebeu {type(primate_data['diet']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if primate_data["social_behavior"] not in get_args(SocialBehavior):
            error_message: str = f"Esperado que social_behavior seja do tipo SocialBehavior, mas recebeu {type(primate_data['social_behavior']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if not isinstance(primate_data["genetic_variation"], float):
            error_message: str = f"Esperado que genetic_variation seja do tipo float, mas recebeu {type(primate_data['genetic_variation']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if primate_data["health_status"] not in get_args(HealthStatus):
            error_message: str = f"Esperado que health_status seja do tipo HealthStatus, mas recebeu {type(primate_data['health_status']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
        if not (isinstance(primate_data["coordinates"], tuple) and len(primate_data['coordinates']) == 2 and isinstance(primate_data['coordinates'][0], float) and isinstance(primate_data["coordinates"][1], float)):
            error_message: str = f"Esperado que coordinates seja do tipo tuple de dois floats, mas recebeu {type(primate_data['coordinates']).__name__}"
            Log.error(error_message)
            raise TypeError(error_message)
