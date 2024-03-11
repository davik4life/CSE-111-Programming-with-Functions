def water_column_height(tower_height, tank_height):
    """
    This is a function that returns the water column height.
    """
    
    height = tower_height + (3*tank_height) / 4
    return height
    
def pressure_gain_from_water_height(height):
    """
    This is a function that returns the pressure gain from the water height.
    """
    p = 998.2
    g =  9.80665
    pressure_gain = (p * g * height) / 1000
    
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    This is the function that returns the pressure loss from pipe.
    """
    p = 998.2
    
    pressure_loss = (-friction_factor * pipe_length * p) *  (fluid_velocity**2) / (2000*pipe_diameter)
    
    return pressure_loss