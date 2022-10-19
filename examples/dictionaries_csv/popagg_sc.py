import csv

with open("2010_city_state_postal_pop.csv") as f:
    rdr = csv.reader(f)
    next(rdr) # read and ignore (i.e., skip) the header row

    sc_pop = 0
    for (zipcode, city, state, rawpop) in rdr:  # tuple assignment from row
        if state == "SC":
            sc_pop += int(rawpop)

print(f"SC\t{sc_pop:,}")
