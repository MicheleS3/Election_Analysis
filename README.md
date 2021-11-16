# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election unit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were "x" votes cast in the election.
- The candidates were:
  - Candidate 1
  - Candidate 2
  - Candidate 3
- The candidate results were:
  - Candidate 1 received "x%" of the vote and "y" number of votes.
  - Candidate 2 received "x%" of the vote and "y" number of votes.
  - Candidate 3 received "x%" of the vote and "y" number of votes.
- The winner of the election was:
  -Candidate (1, 2, or 3), who received "x%" of the vote and "y" number of votes.

## Challenge Overview
The purpose of this audit is to provide a complete list of each candidate, how many votes they received, what counties voted, and who won the congressional election.  The election commission needs to know the voter turnout for each county, the percentage of votes from each county, and the county with the highest turnout.  
## Challenge Summary
Election-Audit Results
-	Total Votes cast = 369,711
-	County Votes breakdown
County Votes:
  -Jefferson: 10.5% (38,855)
  -Denver: 82.8% (306,055)
  -Arapahoe: 6.7% (24,801)
-	Largest County Turnout: Denver
-	Candidate Vote & Percentage breakdown
  -Charles Casper Stockham: 23.0% (85,213)
  -Diana DeGette: 73.8% (272,892)
  -Raymon Anthony Doane: 3.1% (11,606)
-	Election Winner
  -Winner: Diana DeGette
  -Winning Vote Count: 272,892
  -Winning Percentage: 73.8%

Election-Audit Summary

The audit election code that has been written to provide the results above can be used for other elections in your area or other cities, counties, and even states.  A few modifications to the reference files are needed to calculate the desired results.  The file_to_load and file_to_save can easily be updated to pull new election files.  If election results were needed at a city or state level, the code could easily reference them instead of a county.  
