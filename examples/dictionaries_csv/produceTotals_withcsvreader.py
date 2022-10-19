import csv

produce_file = open("produce_sales_altered.csv")
csv_reader = csv.reader(produce_file)

produce_data = list(csv_reader) # Get a list of lists

produce_totals = {}
for csv_line in produce_data[1:]:
    # Extract data from current line
    # [produce_type, _, _, total] = csv_line
    produce_type = csv_line[0]  # produce type is in position 0 of list
    total = csv_line[3]        # produce total is in position 3 of list

    if produce_type in produce_totals:
        produce_totals[produce_type] = produce_totals[produce_type] + float(total)
    else:
        produce_totals[produce_type] = float(total)

for produce_type in sorted(produce_totals):
    print('{0} - ${1:.2f}'.format(produce_type, produce_totals[produce_type]))

  
