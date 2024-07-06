from utils.Types import Species, HabitatRegion, Diet, SocialBehavior, HealthStatus

class Primate:
    species_name: Species
    population: dict[str, list[int, int]]
    habitat_region: HabitatRegion
    diet: Diet
    social_behavior: SocialBehavior
    genetic_variation: float
    health_status: HealthStatus
    coordinates: tuple[float, float]

    def __init__(self,
                species_name: Species,
                habitat_region: HabitatRegion,
                population: dict[str, list[int, int]],
                diet: Diet,
                social_behavior: SocialBehavior,
                genetic_variation: float,
                health_status: HealthStatus,
                coordinates: tuple[float, float]) -> None:

        self.species_name = species_name
        self.population = population
        self.habitat_region = habitat_region
        self.diet = diet
        self.social_behavior = social_behavior
        self.genetic_variation = genetic_variation
        self.health_status = health_status        
        self.coordinates = coordinates

    def __repr__(self) -> str:
        return (f"Primate(species_name={self.species_name}, population={self.population}, "
                f"habitat_region={self.habitat_region}, diet={self.diet}, "
                f"social_behavior={self.social_behavior}, genetic_variation={self.genetic_variation}, "
                f"health_status={self.health_status}, coordinates={self.coordinates})")