import json

# If there are any errors, handle them in the except block.
try:
    with open('input.json', 'r') as input_file:     # Open the input.json file in read mode ('r')
        data = json.load(input_file)                # Read the file and load its content as a Python object (list or dictionary)

    if data:
        headers = list(data[0].keys())              # Get the keys from the first dictionary (like the headers in CSV)
    else:
        header =  []                                # If data is empty, set headers as an empty list

    output = ', '.join(headers)                     # Join the headers into a single string with commas between them


    # Loop through each item (each dictionary) in the data
    for obj in data:
        row = [str(obj.get(header, '')) for header in headers]        # For each dictionary, create a list of values for each header
        output += '\n' + ', '.join(row)                               # Add the row of values to the output, separated by commas

    with open('output.csv', 'w') as output_file:                     # Open output.csv file in write mode ('w') and write the CSV content to it
        output_file.write(output)

except Exception as error:            # If there is any error, print the error message
    print(f'Error: {str(error)}')
