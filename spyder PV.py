import math

# Step 1: Define inputs (building and panel parameters)
building_width = 8  # in meters
building_length = 28  # in meters
roof_angle_deg = 22  # in degrees
pv_width_mm = 1690  # in millimeters
pv_height_mm = 1046  # in millimeters
pv_power_wp = 400  # in watts (Wp)

# Step 2: Convert PV dimensions to meters for consistency
pv_width_m = pv_width_mm / 1000  # convert to meters
pv_height_m = pv_height_mm / 1000  # convert to meters

# Step 3: Calculate effective roof area
roof_angle_rad = math.radians(roof_angle_deg)  # convert angle to radians
effective_roof_length = building_length / math.cos(roof_angle_rad)  # effective length due to angle
effective_roof_area = building_width * effective_roof_length  # total roof area available

# Step 4: Calculate maximum number of panels that can fit
max_panels_width = int(building_width / pv_width_m)
max_panels_length = int(effective_roof_length / pv_height_m)
total_number_of_panels = max_panels_width * max_panels_length

# Step 5: Calculate total power capacity in kWp
total_capacity_kwp = (total_number_of_panels * pv_power_wp) / 1000  # convert Wp to kWp

# Output results
print("Total number of panels:", total_number_of_panels)
print("Total capacity (kWp):", total_capacity_kwp)
