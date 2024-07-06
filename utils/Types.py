from typing import Literal

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