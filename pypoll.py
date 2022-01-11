# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   # Print the header row.
    headers = next(file_reader)
    print(headers)
   

election_data.close()
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()




#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.ls