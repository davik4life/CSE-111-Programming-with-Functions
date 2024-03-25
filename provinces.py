def main():
    """This is the provinces.py main function that returns the provinces on the 
    province.txt file.
    """
    provinces_text = read_provinces("provinces.txt")
    # next(provinces_text)
    count = 0
    
    # Count  the number of Alberta present in the modified file.
    for i in provinces_text:
        if i == "Alberta":
            count += 1
    
    # print(provinces_text)
    
    print()
    print(f"Alberta occurs {count} times in the modified list.")    
    
def read_provinces(filename):
    text_file = []
    with open(filename, "rt") as provinces:
        for line in provinces:
            cleaned_line = line.strip()
            text_file.append(cleaned_line)
        
        # Print the entire list.    
        print(text_file)
            
        #Replace all occurence of "AB" in the list with "Alberta"
        for i in range(len(text_file)):
            if text_file[i] == "AB":
                text_file[i] = "Alberta"

        # Remove the first occurence.            
        text_file.pop(0)
        
        # Remove the last occurence.
        text_file.pop()
            
    return text_file


if __name__ == "__main__":
    main()