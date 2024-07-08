from utils.Types import Species, HabitatRegion, Diet, SocialBehavior, HealthStatus

class Primate:
    """
    Representa um primata com características específicas.

    Atributos
    ---------
    species_name : Species
        O nome da espécie do primata (um valor literal).
    population : dict[str, list[int, int]]
        Dados da população do primata ao longo dos anos, onde as chaves são anos e os valores são listas de dois inteiros (população e expectativa de vida).
    habitat_region : HabitatRegion
        A região do habitat natural do primata (um valor literal).
    diet : Diet
        O tipo de dieta do primata (um valor literal).
    social_behavior : SocialBehavior
        O comportamento social do primata (um valor literal).
    genetic_variation : float
        A variação genética dos genes do primata.
    health_status : HealthStatus
        O nível de extinção do primata (um valor literal).
    coordinates : tuple[float, float]
        As coordenadas geográficas do habitat do primata.
    """

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