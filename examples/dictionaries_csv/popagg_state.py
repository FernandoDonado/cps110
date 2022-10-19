import csv

with open("2010_city_state_postal_pop.csv") as f:
    rdr = csv.reader(f)
    next(rdr) # read and ignore (i.e., skip) the header row

    pops = {}
    for (zipcode, city, state, rawpop) in rdr:  # tuple assignment from row
        pop = int(rawpop)

        try:
            pops[state] = pops[state] + pop
        except KeyError:
            pops[state] = pop

for state in sorted(pops):
    print(f"{state}\t{pops[state]:,}")

