class Ecosystem:
    def __init__(self, name, description, biodiversity_index):
        self.name = name
        self.description = description
        self.biodiversity_index = biodiversity_index
        
    def describe (self):
        
        return f"A {self.name} has the decription of {self.description} def has {self.biodiversity_index} with 1 indictaion high biodversity"
eco = Ecosystem(name="Savanna", description= "prolly dry", biodiversity_index=1)

print(eco.describe())

class Forest(Ecosystem):
    def __init__(self, name, description, biodiversity_index, tree_species, carbon_sequestration_rate):
        super().__init__(name, description, biodiversity_index)
        self.tree_species = tree_species
        self.carbon_sequestration_rate = carbon_sequestration_rate

    def for_obj(self):
        return f"{self.name}with this {self.description} description with a {self.biodiversity_index} and {self.carbon_sequestration_rate}tons for carbon is crazy bro"