def split_and_join(line):
    # Split the input string on space delimiter and join using hyphen
    return "-".join(line.split())

if __name__ == '__main__':
    input_string = input()  # Read the input string
    result = split_and_join(input_string)  # Call the function
    print(result)  # Print the resulting string
