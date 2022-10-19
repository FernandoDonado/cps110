

produce_file = open("produce_sales.csv")

produce_file.readline()  # discard first line
lines = produce_file.readlines() # read rest of lines

produce_totals = {}
for line in lines:
  [produce_type, cost_per_pound, pounds_sold, total] = line.split(',')
  if produce_type in produce_totals:
    produce_totals[produce_type] = produce_totals[produce_type] + float(total)
  else:
    produce_totals[produce_type] = float(total)

for produce_type in sorted(produce_totals):
  print('{0} - ${1:.2f}'.format(produce_type, produce_totals[produce_type]))

  
