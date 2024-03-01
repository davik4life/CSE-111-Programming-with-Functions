import math

def main ():
    """
    This is the main Function and it returns the entire functions
    within this program
    """
    
    # Create a list of the values so I can iterate and compute based off each value
    # in the list.
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost_per_can = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
               
    best_storage = -1
    best_cost = -1
    max_can = None
    max_cost = None
    for i in range(len(names)):
        can_names = names[i]
        can_radius = radius[i]
        can_height = height[i]
        can_cost_per_can = cost_per_can[i]
        
        storage_efficiency = compute_storage_efficiency(can_radius, can_height)
        cost_efficiency = compute_cost_efficiency(can_radius, can_height, can_cost_per_can)

        print(f"{can_names} {storage_efficiency:.2f} {cost_efficiency:.0f}")    

        
        # Find the best storage effeciency
        if storage_efficiency > best_storage:
            max_can = can_names
            best_storage = storage_efficiency
        
        # Find the best cost effeciency
        if cost_efficiency > best_cost:
            max_cost = can_names
            best_cost = cost_efficiency
            
            
    print()
    print(f"The best storage efficiency is: {max_can}")
    print(f"The best cost efficiency is: {max_cost}")
            


def compute_volume(radius, height):
    """
    This is the function that computes the compute volume 
    and returns the compute colume value.
    """
    volume = math.pi * (radius ** 2) * height
    return volume
    
    
def compute_surface_area(radius, height):
    """
    This is the compute surface area function that computes
    and returns the surface area.
    """
    surface_area =  2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(radius, height):
    """
    This is the function that computes the storage efficiency.
    and returns the value.
    """
    # Calling the function to calculate volume.
    volume = compute_volume(radius, height) 
    # Calling the function to calculate surface_area.
    surface_area = compute_surface_area(radius, height) 

    storage_efficiency = volume / surface_area
    
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    """
    This is the function that computes cost efficiency
    and returns the value
    """
    
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost
    
    return cost_efficiency
    
main()