# Program to Read from a Text File and Write to a New File

def read_and_write_files(input_file, output_file):
    try:
        # Reading the contents of the input file
        with open(input_file, 'r') as infile:
            contents = infile.read()
        
        # Writing the contents to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(contents)
        
        print(f"Contents have been successfully copied from '{input_file}' to '{output_file}'.")
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify input and output file names
input_file_name = input("Enter the name of the file to read from: ").strip()
output_file_name = input("Enter the name of the file to write to: ").strip()

# Call the function
read_and_write_files(input_file_name, output_file_name)
