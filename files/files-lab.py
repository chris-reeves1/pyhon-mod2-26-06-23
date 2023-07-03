import csv

companies = []
sales = []

with open("output.csv") as csvfile: # dont need r or w as csv module handles this. 
    reader = csv.reader(csvfile) # reader function from the cvs module, which reads all the lines.
    next(reader) # skips the first line dont need the header data
    for row in reader:
        companies.append(row[0])
        sales.append([int(x.replace(",", "")) for x in row[1:]]) # iterates from index 1 to the end, changes from str to int and gets rid of ","

#print(sales)
monthly_sum = [sum(x) for x in zip(*sales)] # unpacks the list of lists into tuples, and sums.

#print(monthly_sum)

yearly_sum = {}
for i in range(len(companies)):
    yearly_sum[companies[i]] = sum(sales[i])

print("monthly sales:", monthly_sum)
print("yearly sales:")
for company, sales in yearly_sum.items():
    print(company, sales)

