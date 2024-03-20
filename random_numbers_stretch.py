import random

def main():
    """
    Creates a list of numbers, appends more numbers onto the list, and prints the list. 
    The program must have two functions named main and append_random_numbers 
    as follows:
    
    Stretch Challenge:
        Statements: Create a list of Words, call the append_random_words function,
        and print the lists of words.
    """
    
    numbers = [16.2, 75.1, 52.3]
    words = ["tap", "cheer"]
    print(f"numbers {numbers}")
    appended_numbers = append_random_numbers(numbers)
    print(f"numbers {appended_numbers}")
    appended_numbers = append_random_numbers(numbers, 3)
    print(f"numbers {appended_numbers}")
    appended_words = append_random_words(words, 3)
    print(f"words {appended_words}")
    
    
def append_random_numbers(numbers_list, quantity = 1):
    """

    Args:
        numbers_list (list): List of numbers
        quantity (int, optional): Requires an interger or Defaults to 1.
    """
    
    for i in range(quantity):
        numbers_list.append(round(random.uniform(0, quantity), 1))
            
    return numbers_list
    
def append_random_words(words_list, quantity = 1):
    """
    Appends a randomly selected word from the provided list to another list.
    
    Args:
        words_list (list): List of workds
        quantity (int, optional): Number of words to be appended. Defaults to 1.
    """
    
    word_bank = ["happy", "code", "computer", "think", "python"]
    
    for i in range(quantity):
        random_word = random.choice(word_bank)
        words_list.append(random_word)
    # while len(word_bank) > quantity:
    #     words_list.append(random_word)
    
    return words_list
    

if __name__ == "__main__":
    main()