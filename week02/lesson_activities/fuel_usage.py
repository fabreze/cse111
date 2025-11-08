def miles_per_gallon(start_miles, end_miles, amount_gallons):
    miles_per_gallon = (end_miles - start_miles)/amount_gallons
    return miles_per_gallon

def lp100k_from_mpg(miles_per_gallon):
    lp100k = 235.215/miles_per_gallon
    return lp100k


def main():
    start_miles = int(input("Enter the first odometer reading (miles): "))
    end_miles = int(input("Enter the second odometer reading (miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.2f} miles per gallon \n"
          f"{lp100k:.2f} liters per 100 kilometers")
    pass

main()