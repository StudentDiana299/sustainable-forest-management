def analyse_carbon_impact (deforested_areas,planted_trees,carbon_emission_factor,carbon_offset_per_tree):
    total_emission = sum(deforested_areas*carbon_emission_factor)
    total_offset = sum(planted_trees*carbon_offset_per_tree)
    overall_impact = total_emission - total_offset

    if total_offset >= total_emission:
        print("Positive")
    elif total_offset == total_emission:
        print("Neutral")
    else:
        print("Negative")

    return overall_impact

deforested_areas = [10, 15, 8, 12, 20]
planted_trees = [30, 40, 25, 35, 50]
carbon_emission_factor = 30
carbon_offset_per_tree = 5

impacted = analyse_carbon_impact (deforested_areas,
                                  planted_trees,carbon_emission_factor,carbon_offset_per_tree)
print("impacted")

def project_future_tree_planting(initial_planted_trees, annual_growth_rate, projection_years):
        projected_planting = [initial_planted_trees * (1 + annual_growth_rate) ** year for year in range(1, projection_years + 1)]
        return projected_planting
    
initial_planted_trees= 100
annual_growth_rate = 0.05
projection_years = 10

list = project_future_tree_planting(initial_planted_trees, annual_growth_rate, projection_years)
print(list)


def calculate_region_offset (region_name, **factors):
         total_offset = sum(factors.values())/len(factors)
         return region_name, total_offset
calculate_region_offset_with_kwargs("Amazon", deforested_area=30, planted_trees=40, carbon_emission_factor=10)