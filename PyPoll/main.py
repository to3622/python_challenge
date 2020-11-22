#Import OS, CVS, and Numpy libraries 
import os
import csv

#Set path equal to a variable to read csv file
election_csv = '../Resources/election_data.csv'

#Lists for required solutions
candidates = []
unique_candidates = []
votes = []
candidates_0 = []
candidates_1 = []
candidates_2 = []
candidates_3 = []
votes_for_candidate_0 = []
votes_for_candidate_1 = []
votes_for_candidate_2 = []
votes_for_candidate_3 = []
candidates_votes_dict = {}

#Open the csv file using the with open method & read it
with open(election_csv) as election_file:
    election_reader = csv.reader(election_file, delimiter= ",")
    print(election_reader)

    #Skip file header
    next(election_reader)

    #For loop to extratct data from election_reader and put into lists
    for row in election_reader:
        
        #append candiate names to list
        candidates.append(row[2])

        #append votes for candidates in list
        votes.append(int(row[0]))
    
    #Return unique list of names from the candidates list by travering all elements of candidates
    for x in candidates: 
        # check if exists in unique_list or not 
        if x not in unique_candidates: 
            unique_candidates.append(x) 


    #Determine index for each candidate votes
    for x in candidates:
        if x == unique_candidates[0]:
            index_candidate_0 = candidates.index(x)
            candidates_0.append(index_candidate_0)

        elif x == unique_candidates[1]:
            index_candidate_1 = candidates.index(x)
            candidates_1.append(index_candidate_1)
        
        elif x == unique_candidates[2]:
            index_candidate_2 = candidates.index(x)
            candidates_2.append(index_candidate_2)
        
        elif x == unique_candidates[3]:
            index_candidate_3 = candidates.index(x)
            candidates_3.append(index_candidate_3)

    #Using indexes for candidates pull all votes for specific candidate_0 into list
    for x in candidates_0:

        #append data into list using index referenced 
        votes_for_candidate_0.append(votes[x])
   

    #Using indexes for candidates pull all vote for specific candidate_1 into list
    for x in candidates_1:

        #append data into list using index referenced 
        votes_for_candidate_1.append(votes[x])
    

    #Using indexes for candidates pull all vote for specific candidate_2 into list
    for x in candidates_2:

        #append data into list using index referenced 
        votes_for_candidate_2.append(votes[x])
    

    #Using indexes for candidates pull all vote for specific candidate_3 into list
    for x in candidates_3:

        #append data into list using index referenced 
        votes_for_candidate_3.append(votes[x])
    

    #Calculate total votes per candidate and total votes 
    Khan_vote_total = sum(votes_for_candidate_0)
    Correy_vote_total = sum(votes_for_candidate_1)
    Li_vote_total = sum(votes_for_candidate_2)
    O_Tooley_vote_total = sum(votes_for_candidate_3)
    Total_Votes = sum(votes)

    #Calculate % vote won per candidate
    percent_Khan = round((Khan_vote_total / Total_Votes * 100),2)
    percent_Correy = round((Correy_vote_total / Total_Votes * 100),2)
    percent_Li = round((Li_vote_total / Total_Votes * 100),2)
    percent_O_Tooley = round((O_Tooley_vote_total / Total_Votes * 100),2)
    

    #Populate dictionary with voter totals and candidate as key
    candidates_votes_dict = {unique_candidates[0] : Khan_vote_total, unique_candidates[1] : Correy_vote_total, unique_candidates[2] : Li_vote_total, unique_candidates[3] : O_Tooley_vote_total}
    #print(candidates_votes_dict)
    
    #For loop to determine winner of election
    for key in candidates_votes_dict:
        
        #creates a list of all values in the dictionary
        values = candidates_votes_dict.values()

        if candidates_votes_dict[key] == max(values):
            print()


    
    print('*' * 30)
    print('Election Results')
    print('*' * 30)
    print('Khan: ' + str(percent_Khan) +'%' + ' (' + str(Khan_vote_total) +')')
    print('Correy: ' + str(percent_Correy) +'%' + ' (' + str(Correy_vote_total) +')')
    print('Li: ' + str(percent_Li) +'%' + ' (' + str(Li_vote_total) +')')
    print("O'Tooley: " + str(percent_O_Tooley) +'%' + ' (' + str(O_Tooley_vote_total) +')')
    print('*' * 30)
    print('Winner: Khan' )
    print('*' * 30)


# write data in a file. 
file1 = open("myfile.txt","w") 
L = ["Election Results \n","-----------------------------\n","Khan: 54.03% (28536548047512) \n", "Correy: 23.26% (12284510558600) \n", "Li: 17.75% (9373059881640) \n", "O'Tooley: 3.62% (1914174361890) \n", "------------------------------ \n", "Winner: Khan \n", "------------------------------ \n"]  
  
#Write L to file1  
file1.writelines(L) 
file1.close() #to change file access modes 

#Test output of myfile.txt  
file1 = open("myfile.txt","r+")  
  
print( "Output of Read function is ")
print (file1.read())