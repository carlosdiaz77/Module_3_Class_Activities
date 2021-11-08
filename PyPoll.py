import csv
import os


txtpath = os.path.join("analysis", "election_analysis.txt")
csvpath = os.path.join("Resources", "election_results.csv")


    #-----------------------------------------------------------------------------------------
    # 1. Initialize a total vote counter. (Declare a new variable)
total_votes= 0

    # Candidate Options (Declare a new, empty list)
candidate_options = []

# Each Candidate votes(Declare an empty disctionary)
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#--------------------------------------------------------------------------------------


# Open the CSV
#read and analyze the data here
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Print the header row. ( this option prints only the headers)
    headers = next(csvreader)
    #print(headers)

    # TO CALCULATE ALL THE ROWS/LINES

    for row in csvreader:
        # 2. Add to the total vote count.
        total_votes += 1


            # Print the candidate name from each row.
        candidate_name = row[2]
    
            # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                # Add the candidate name to the list of candidates.
            candidate_options.append(candidate_name)
                # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
with open(txtpath, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")

    txt_file.write("-------------------------\n")
    txt_file.write("***ELECTION RESULTS***\n")
    txt_file.write(F"Total votes:{total_votes:,}\n")
    txt_file.write("-------------------------\n")
    
    # Determine the percentage of votes for each candidate by looping through the counts.
        #1. Iterate through the candidate list.
        
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100,1)
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.    
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,} votes)\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    

        
    
    

    #-------------PRINT OUTPUTS------------------------------------------
    # Print candidate list
    #print(candidate_options)
    # Print the candidate vote dictionary.
    #print(candidate_votes)
    #Print the total votes.
    #print(total_votes)