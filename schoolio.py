# I'm using CORGIS!
import school_scores
list_of_record = school_scores.get_all()

for row in list_of_record:
    print(row["State"]["Name"], row["Year"], row["Total"]["Math"])
