import os, csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#declaring my variables
sum_months = 0
list_months = []
list_diferences = []
change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

#open file as csv
with open(csvpath, encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    # print('Financial Analysis')
    # print('------------------------')
    next(pointer)

    from statistics import mean
    current_value = 0

    for m in pointer:
        months = m[0]
        sum_months = sum_months + float(m[1])
        list_months.append(months)

        if current_value ==0:
            current_value = float(m[1])
        else:
            
            list_diferences.append(float(m[1])-current_value)
            

            change = (float(m[1]) - current_value)
            

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = m[0]
                

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = m[0]
            
            current_value = float(m[1])


list_avg = mean(list_diferences)

#printing the output
output = f"""
Financial Analysis
------------------------
Total Months: {str(len(list_months))}
Total: ${round(sum_months)}
Average Change: ${str(round(list_avg,2))}
Greatest Increase in Profits: {greatest_increase_month} (${str(round(greatest_increase))})
Greatest Decrease in Profits: {greatest_decrease_month} (${str(round(greatest_decrease))})
"""

print(output)

#creating text file with the results
with open("analysis/pybank.text","w") as f:
    f.write(output)