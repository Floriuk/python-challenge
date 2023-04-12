import os, csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    print('Financial Analysis')
    print('------------------------')
    next(pointer)
    # Declaring my variables to analyze
    from statistics import mean
    sum_months = 0
    list_months = []
    current_value = 0
    list_diferences = []
    for m in pointer:
        months = m[0]
        sum_months = sum_months + float(m[1])
        list_months.append(months)
        if current_value ==0:
            current_value = float(m[1])
        else:
            list_diferences.append(float(m[1])-current_value)
            current_value = float(m[1])
        

print("Total Months: " + str(len(list_months)))
print("Total: $", round(sum_months))
list_avg = mean(list_diferences)
print("Average Change: $" + str(round(list_avg,2)))
print('Greatest Increase in Profits: '+ m[0] + ' ($' + str(round(max(list_diferences)))+')')
print('Greatest Decrease in Profits: '+ m[0] + ' ($' + str(round(min(list_diferences)))+')')
