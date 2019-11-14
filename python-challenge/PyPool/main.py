import os
import csv

CandidateList ={} # dictionary
candidatename = []
votes = 0


#read files
Pool_csv = os.path.join("PyPolldata.csv")

with open (Pool_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',' )
    csv_header = next(csvfile)
    #print(f"Header :{csv_header}") 
    for row in csv_reader:
        votes = votes + 1
        
        total_candidates = 0
        
        if row[2] not in candidatename:
            candidatename.append(row[2])
            CandidateList[row[2]] = 1
        else:
            CandidateList[row[2]]= CandidateList[row[2]] + 1
            
print (votes)  
winningcounts=0          
for candidate in CandidateList:
    if CandidateList[candidate] > winningcounts:
       winningcounts =  CandidateList[candidate]
       winner = candidate


    Candidate_results = (candidate + " " + str(round(((CandidateList[candidate]/votes)*100))) + "%" + " (" + str(CandidateList[candidate]) + ")") 
          

output_file =  os.path.join("PyPoolResults.csv")
with open(output_file,"w", newline="") as datafile:

    
    datafile.write(f'[Election Results]\n')
    datafile.write(f'[-----------------]\n')
    datafile.write(f'[Total Votes]: {str(votes)}\n')
    datafile.write(f'[-----------------]\n')
    for candidate in CandidateList:
        if CandidateList[candidate] > winningcounts:
            winningcounts =  CandidateList[candidate]
            winner = candidate

        Candidate_results = (candidate + " " + str(round(((CandidateList[candidate]/votes)*100))) + "%" + " (" + str(CandidateList[candidate]) + ")") 
        datafile.write(f' {Candidate_results}\n')

    datafile.write(f'[-----------------]\n')
    datafile.write(f'[Winner: {winner} ]\n')
    datafile.write(f'[-----------------]\n')