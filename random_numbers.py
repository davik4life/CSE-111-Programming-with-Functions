import random

def main():
    """
    Creates a list of numbers, appends more numbers onto the list, and prints the list. 
    The program must have two functions named main and append_random_numbers 
    as follows:
    """
    
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    appended_numbers = append_random_numbers(numbers)
    print(appended_numbers)
    appended_numbers = append_random_numbers(numbers, 3)
    print(appended_numbers)
    
    
def append_random_numbers(numbers_list, quantity = 1):
    """

    Args:
        numbers_list (list): List of numbers
        quantity (int, optional): Requires an interger or Defaults to 1.
    """
    
    # if quantity == 1:
    #     numbers_list.append(round(random.uniform(0, quantity), 1))
    # else:
    #     for i in range(quantity):
    #         numbers_list.append(round(random.uniform(0, quantity), 1))
    
    for i in range(quantity):
        numbers_list.append(round(random.uniform(0, quantity), 1))
            
    return numbers_list
    

if __name__ == "__main__":
    main()