"""
Authors: Fabrizio Caballero
Enhancements: I added a message at the bottom the shows the return by date.
"""
import csv
from datetime import datetime, timedelta
SALES_TAX_RATE = 0.06

def main():
    products_file = "products.csv"
    requests_file = "request.csv"
    raw_date = datetime.today()
    today = raw_date.strftime('%c')
    return_by_date = raw_date + timedelta(days = 30)
    return_by_date = return_by_date.strftime('%c')

    try:
        products_dict = read_dictionary(products_file, 0)
        with open(requests_file, "rt") as requests:
            reader = csv.reader(requests)
            next(reader)
            print("Welcome to the Python Super Market!\n")
            subtotal = 0
            number_of_items = 0
            sales_tax = 0
            total = 0
            try:
                for request in requests:
                    request_list = request.split(",")
                    product_info = products_dict[request_list[0]]

                    product_name = product_info[1].capitalize()
                    product_price = float(product_info[2])
                    requested_quantity = int(request_list[1])

                    number_of_items += requested_quantity
                    subtotal += requested_quantity * product_price

                    print(f"{product_name}: {requested_quantity}    @    {product_price}")
            except KeyError:
                print(f"Error: unknown product ID in the request.csv file {request_list[0]}")
            
            sales_tax = subtotal * SALES_TAX_RATE
            total = subtotal + sales_tax

            print(f"\nNumber of Items: {number_of_items}\n"
                f"Subtotal: {subtotal:.2f}\n"
                f"Sales Tax: {sales_tax:.2f}\n"
                f"Total: {total:.2f}\n"
                "Thank you for shopping at Python Super Market!\n"
                f"{today}\n"
                f"Refunds are only given if returned by: {return_by_date}")
            
    except FileNotFoundError:
            print("Error: missing file\n"
                  f"[Errno 2] No such file or directory: '{requests_file}'")
    except PermissionError:
            print("You do not have permission to access that file.")

def read_dictionary(file_name, key_column_index):
    products_dict = {}

    try:
        with open(file_name, "rt") as dictionary:
            reader = csv.reader(dictionary)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]

                    products_dict[key] = row_list

    except FileNotFoundError:
            print("Error: missing file\n"
                  f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
            print("You do not have permission to access that file.")

    return products_dict

if __name__ == "__main__":
    main()