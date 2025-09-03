def calculate_forest_area (trees,area_per_tree=10, deforestation_factor=0.2):
    total_area = trees * area_per_tree
    net_forest = total_area * deforestation_factor
    return net_forest
result = calculate_forest_area(50, 5, 0.3)
print(result)

def tree_planting_campaign (initial_trees,*trees_per_campaign):
    total_trees = initial_trees

    for trees_planted in trees_per_campaign:
        total_trees +=trees_planted
    return total_trees
total = tree_planting_campaign(100,20,30,50)
print (total)


def deforestation_impact_report (**impact_value):
    print("Deforestation Impact Report:")

    for aspect in impact_value:
        value = impact_value[aspect]
        print(f"- {aspect}: {value}")

deforestation_impact_report(
    loss_of_biodiversity=30,
    carbon_emission=500,
    soil_erosion=20
)