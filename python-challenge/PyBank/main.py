import os
import csv

Date = []
ProfitLosses = []
Total = 0
changeaverage = 0
greatestincrease = 0
greatestdecrease = 0

Bank_csv = os.path.join("PyBankdata.csv")

with open (Bank_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',' )
    csv_header = next(csvfile)
    #print(f"Header :{csv_header}") 
    
    for row in csv_reader:
        Date.append(row[0])
        ProfitLosses.append(int(row[1]))
    
        #net amount of "Profit/Losses" over the entire period
        Total = Total + int(row[1])
        
        a = int( row[1])
        if a > greatestincrease:
            greatestincrease = a
            greatestINC_DATE= row[0]
            
        if a  <  greatestdecrease:
            greatestdecrease = a
            greatestDEC_DATE= row[0]    
          
    #The total number of months included in the dataset
    totalmonths = len(Date)
    
    dftotal=0
    for i in range(totalmonths-1) :
        df = ProfitLosses[i+1]-ProfitLosses[i]
        dftotal= dftotal+ df
    AverageChange = round(dftotal/ (totalmonths-1),2)
    
   print(['Finantial Analysis'])
   print(['-----------------'])
   print(f'Total Months: {str(totalmonths)}' )
   print(f'[Total]:  $ {Total}')
   print(f'[Average Change] : $ {AverageChange}')
   print(f'[Greatest Increase in Profits] : {greatestINC_DATE} ($ {greatestincrease})')
   print(f'[Greatest Decrease in Profits] : {greatestINC_DATE} ($ {greatestdecrease})')  

output_file =  os.path.join("PyBankResults.txt")
with open(output_file,"w", newline="") as datafile:

  
    datafile.write(f'[Finantial Analysis]\n')
    datafile.write(f'[-----------------]\n')
    datafile.write(f'[Total Months]: {str(totalmonths)}\n')
    datafile.write(f'[Total]:  $ {Total}\n')
    datafile.write(f'[Average Change] : $ {AverageChange}\n')
    datafile.write(f'[Greatest Increase in Profits] : {greatestINC_DATE} ($ {greatestincrease})\n')
    datafile.write(f'[Greatest Decrease in Profits] : {greatestDEC_DATE} ($ {greatestdecrease})\n')


