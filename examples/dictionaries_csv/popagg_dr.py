import csv

with open("2010_city_state_postal_pop.csv") as f:
    rdr = csv.DictReader(f)

    pops = {}
    for fields in rdr: # fields is a dictionary { "header-name": "row-value"... } 
        key = fields['State']
        pop = int(fields['2010 Population'])

        try:
            pops[key] = pops[key] + pop
        except KeyError:
            pops[key] = pop

for key in sorted(pops):
    print(f"{key}\t{pops[key]:,}")

