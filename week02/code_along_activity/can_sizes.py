import math
def main ():
    can_names = ["#1 Picnic","#1 Tall","#2","#2.5","#3 Cylinder","#5","#6Z","#8Z short","#10","#211","#300","#303"]
    can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    for index in range(len(can_names)):
        volume = compute_volume(can_radius[index], can_height[index])
        surface_area = compute_surface_area(can_radius[index], can_height[index])

        storage_efficiency = volume/surface_area
        print(f"{can_names[index]} {storage_efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

main()