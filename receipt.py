import csv

def main():
    """
    This is the main function.
    """
    # Create a variable to store the csv file.
    filename = "products.csv"
    
    # Create a constant variable to avoid directly hard-coding the parameter
    KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    
    # Create a variable that calls the read_dictionary function and stores it for later reference,
    products_dict = read_dictionary(filename, KEY_INDEX)
    
    
    print()
    print("All Products")
    print()
    # Print the products_dict.
    print(products_dict)
    request_file = "request.csv"
    
    # Open the request.csv file for reading.
    with open(request_file, "rt") as request_data:
        reader = csv.reader(request_data)
        
        # Skip the first line of the file.
        next(reader)
        
        print()
        print("Reqeusted Items")
        for request in reader:
            product_name, quantity = request
             
            if product_name in products_dict:
                print(f"{products_dict[product_name][PRODUCT_NAME_INDEX]}: {quantity} @ {products_dict[product_name][PRODUCT_PRICE_INDEX]}")

    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dictionary = {}
    
    with open(filename, "rt") as product_data:
        reader = csv.reader(product_data)
        
        # Skip the first line or header.
        next(reader)
        
        
        # Iterate through the csv file and copy the items into a dictionary.
        
        # This is the first methogd I used. Having to explicitly specify my key with a named variable.
        # I love this method better, and I am keeping this for my note taking.
        
        # for row in reader:
        
        # With this method, I don't need the second key_column_index pararmeter
            
        #     # Assign a named variable to each row for clarity 
        #     # and to be able to use them as a dictionary.
        #     product_num, name, price = row
            
        #     # Specify the key to be used in the dictionary.
        #     products_dict[product_num] = [product_num, name, price]
        
        for row in reader:
            
            # Assign a named variable to each row for clarity 
            # and to be able to use them as a dictionary.
            key = row[key_column_index]
            
            # Specify the key to be used in the dictionary.
            products_dictionary[key] = row
                        
    return products_dictionary
    
if __name__ == "__main__":
    main()
    