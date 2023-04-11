import os, csv
# csvpath = os.path.join('Resources', 'budget_data.csv')
with open('budget_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    print('Financial Analysis')
    print('------------------------')
    next(pointer)
    
    for m in pointer:
        months = m[0]
        sum_months = 0
        list_months = []
        if months!= '':
            sum_months = sum_months + 1
            list_months.append(sum_months)
print("Total Months: " + str(len(list_months)))

    
   