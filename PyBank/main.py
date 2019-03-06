import os
import csv
csvfile = os.path.join('Resources', 'budget_data.csv') 

with open(csvfile, newline="") as csvfile:              
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
	
    # Initialize variables
    total_rev=0             
    old_rev=0       
    total_monthly_change=0  
    rev_inc_max=0   
    rev_dec_max=0 
    rowcounter = 0
      
    

    for row in csvreader:

        date=row[0]

        #2. The net total amount of "Profit/Losses" over the entire period                 
        total_rev = total_rev + float(row[1])    
                
        # 3.Calculate monthly revenue change, for average
        if csvreader.line_num==2:
            monthly_change=0
        else:
            monthly_change=float(row[1])-old_rev
            rowcounter = rowcounter + 1
        total_monthly_change+=monthly_change

       # 4&5. Calculate greatest increase and decrease
        if monthly_change > rev_inc_max:
            rev_inc_max=monthly_change
            date_max_rev_inc=date
        elif monthly_change < rev_dec_max:
            rev_dec_max=monthly_change
            date_max_rev_dec=date

        old_rev=float(row[1])
    
    total_months=int(csvreader.line_num-1) 

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(int(total_rev))) 
    print("Average Revenue Change $" + str(int(total_monthly_change/rowcounter)))
    print("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(rev_inc_max))+")")
    print("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
           str(int(rev_dec_max)) + ")" )



output_path = os.path.join('Resources', 'Financial_Analysis.txt')
with open(output_path, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total Revenue: $" + str(int(total_rev)) + "\n")
    f.write("Average Revenue Change $" + str(int(total_monthly_change/rowcounter)) + "\n")
    f.write("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(rev_inc_max)) + ")" + "\n")
    f.write("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
           str(int(rev_dec_max)) + ")" + "\n")