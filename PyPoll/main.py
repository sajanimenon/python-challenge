import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv') 
output_data = os.path.join('Resources', 'election_result.csv')

#Declare variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winner = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries

with open(csvpath) as dataset:
    reader = csv.DictReader(dataset)

    for row in reader:
        # The total number of votes cast
        total_votes = total_votes + 1
     
        # Extract the candidate name from each row
        candidate_name = row["Candidate"]
     
        # If the candidate does not match any existing candidate...
        
        if candidate_name not in candidate_options:
     
            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)
     
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
     
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_data, "w") as txt_file:

    # Print the final vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winner_summary)


