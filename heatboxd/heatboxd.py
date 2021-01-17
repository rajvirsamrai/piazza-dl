import csv
import matplotlib.pyplot as plot
import sys

ratings = open(sys.argv[1], "r")
tally = {}

# Tally data
for row in csv.DictReader(ratings):
    if int(row["Year"]) not in tally:
        tally[int(row["Year"])] = 1
    else:
        tally[int(row["Year"])] += 1

# Create data array for heatmap
data = []
first_decade = str(sorted(tally)[0])[:3]
last_decade = str(sorted(tally)[-1])[:3]

# Create axesis data
decades = list(range(int(first_decade), int(last_decade)+1))    # Y axesis
years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]                          # X axesis

# Create array of data
for deca in decades:
    new_decade = []
    for year in years:
        x = int(str(deca)+str(year))
        if x in tally:
            new_decade.append(tally[x])
        else:
            new_decade.append(0)
    data.append(new_decade)

fig, axes = plot.subplots()
im = axes.imshow(data)

axes.set_xticks(range(len(years)))
axes.set_xticklabels(years)

axes.set_yticks(range(len(decades)))
axes.set_yticklabels(decades)

for i in range(len(decades)):
    for j in range(len(years)):
        axes.text(j, i, data[i][j], horizontalAlignment="center", verticalAlignment="center", color="w")

fig.suptitle("Films Watched Heatmap by Release Year")
plot.show()
