import csv

def main():
    file_name = 'students.csv'
    students_dict = read_dictionary(file_name)
    I_NUMBER_LENGTH = 9

    i_number = input("Please enter an I-Number (xxxxxxxxx):")
    
    # Remove any dashes found in the entry
    i_number = i_number.replace("-", "")
    
    # Check for the length of the input before proceeding.
    if len(i_number) < I_NUMBER_LENGTH:
        print("Invalid I-Number: too few digits")
    elif len(i_number) > I_NUMBER_LENGTH:
        print("Invalid I-Number: too many digits")
    elif i_number.isdigit() == False:
        print("Invalid Number")
    else:
        if i_number in students_dict:
            print("Student name:", students_dict[i_number])
        else:
            print("No such student")
        
        
def read_dictionary(filename):
    """Read the contents of a CSV file into a
        dictionary and return the dictionary.
    
        Parameters
            filename: the name of the CSV file to read.
        Return: a dictionary that contains
            the contents of the CSV file.
    """
    students_dict = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        # Iterate the entire csv file and organize it into a dictionary.
        for row in reader:
            i_number, name = row
            students_dict[i_number] = name
    return students_dict


if __name__ == "__main__":
    main()