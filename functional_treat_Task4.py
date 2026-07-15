list1 = []
total_element = 0
avg_value = 0.0

# case 1
def funct1():
    """Inputs a 1D list/array from the user."""
    global list1
    user1 = input("\nEnter data for a 1d array (separated by spaces):\n")
    duplicate_value1 = [int(x) for x in user1.split()]
    list1=list(set(duplicate_value1))
    print("\nData has been stored successfully!")


# case 2
def print_characteristics(**kwargs):
    """Prints a summary of dataset characteristics using **kwargs."""
    for key, value in kwargs.items():
        print(f" - {key.replace('_', ' ').title()}: {value}")
def display_data_func():
    """Demonstrates usage of built-in functions to display basic statistics."""
    global total_element, avg_value
    if len(list1) == 0:
        print("Error! List is empty.")
        return
    # built in function
    total_element = len(list1)
    minimum = min(list1)
    maximum = max(list1)
    total_sum = sum(list1)
    avg_value = total_sum / total_element
    print("\nData summary:")
    print_characteristics(
        total_elements=total_element,
        minimum_value=minimum,
        maximum_value=maximum,
        sum_of_all_values=total_sum,
        average_value=f"{avg_value:.2f}"
    )

# case3 
def factorial_recursion_func(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion_func(n - 1)


def factorial_input_func():
    """Handles user interaction for calculating factorial."""
    num1 = int(input("\nEnter a number to calculate its factorial: "))
    if num1 < 0:
        print("Error!")
    else:
        result1 = factorial_recursion_func(num1)
        print(f"\nFactorial of {num1} is: {result1}")

#case 4
def filter_func():
    """Filters values based on user input using lambda and filter() functions."""
    if not list1:
        print("\nList is empty! please input data first.")
        return
    threshold1 = int(input("\nEnter a threshold value to filter out data above this value:\n"))
    filter_data=list(filter(lambda x:x >= threshold1,list1))
    print(f"\nFiltered data (values>={threshold1}):\n{', '.join(map(str,filter_data))}")

# case 5
def sort_data():
    """Sorts data in ascending or descending order using sort() method."""
    if not list1:
        print("\nDataset is empty! Please input data first.")
        return
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    sort_num1=int(input("\nEnter your choice: "))
    if sort_num1 == 1:
        list1.sort()
        print(f"\nSorted Data in Ascending order: \n{ ', ' .join(map(str, list1))}")
    elif sort_num1 == 2:
        list1.sort(reverse=True)
        print(f"\nSorted Data in Descending order: \n{', '.join(map(str, list1))}")
    else:
        print("\nInvalid Choice!")

# case 6
def  dataset_func(*args):
    """Return Multiple statistics of the Dataset."""
    if not args:
        return None
    minimum=min(args)
    maximum=max(args)
    total_sum=sum(args)
    average=total_sum/len(args)

    return minimum, maximum, total_sum, average
def display_data(*args):
    """Displays multiple statistics of the dataset."""
    value1=dataset_func(*args)
    if value1 is None:
        print("\nDataset is empty! please enter data first.")
        return 
    minimum, maximum, total_sum, average= value1
    print("\nDataset Statistics:")
    print(f" - Minimum value: {minimum}")
    print(f" - Maximum value: {maximum}")
    print(f" - Sum of all values: {total_sum}")
    print(f" - Average value: {average:.2f}") 


print("Welcome to the Data Analyzer and Transformer Program!")

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    match choice:
        case 1:
            print(funct1.__doc__)
            funct1()
        case 2:
            print(display_data_func.__doc__)
            display_data_func()
        case 3:
            print(factorial_input_func.__doc__)
            factorial_input_func()
        case 4:
            print(filter_func.__doc__)
            filter_func()
        case 5:
            print(sort_data.__doc__)
            sort_data()
        case 6:
            print(display_data.__doc__)
            if not list1:
                print("\nDataset is empty! Please input data .")
            else:
                display_data(*list1)
        case 7:  
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:  
            print("\nInvalid number! Please enter a number between 1 and 7.") 
