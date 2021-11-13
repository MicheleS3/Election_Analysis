# import os
# dir(os)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# import os


# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the with statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.
#     txt_file.write("Countries in the Election\n")
#     # Write three countries to the file.
#     txt_file.write("--------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    