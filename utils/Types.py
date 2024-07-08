from typing import Literal
"""
Literals para representar diferentes aspectos (tipagens) de primatas.

- `Species`: Espécies de primatas.
- `HabitatRegion`: Regiões de habitat onde os primatas vivem.
- `Diet`: Tipos de dieta dos primatas.
- `SocialBehavior`: Comportamentos sociais dos primatas.
- `HealthStatus`: Estados de saúde dos primatas.

Cada Literal define um conjunto específico de valores que podem ser utilizados para representar
diferentes propriedades dos primatas.
"""

Species = Literal[
    "Gorilla",
    "Chimpanzee",
    "Orangutan",
    "Gibbon",
    "Bonobo",
    "Lemur",
    "Tarsier",
    "Howler Monkey",
    "Spider Monkey",
    "Macaque"
]

HabitatRegion = Literal[
    "Central Africa",
    "West Africa",
    "Madagascar",
    "Southeast Asia",
    "East Asia",
    "South America"
]

Diet = Literal[
    "Frugivore",
    "Herbivore",
    "Insectivore",
    "Omnivore"
]

SocialBehavior = Literal[
    "Group",
    "Solitary",
    "Pair"
]

HealthStatus = Literal[
    "Healthy",
    "Near Threatened",
    "Vulnerable",
    "Endangered",
    "Critically Endangered"
]