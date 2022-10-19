import csv

with open("2010_city_state_postal_pop.csv") as f:
    rdr = csv.reader(f)
    next(rdr) # read and ignore (i.e., skip) the header row

    pops = {}
    for (zipcode, city, state, rawpop) in rdr:  # tuple assignment from row
        key = (city, state) # group by both city+state together
        pop = int(rawpop)

        try:
            pops[key] = pops[key] + pop
        except KeyError:
            pops[key] = pop

for key in sorted(pops):
    print(f"{key[0]}, {key[1]}\t{pops[key]:,}")

