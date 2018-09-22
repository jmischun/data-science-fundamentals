import csv, sys, webbrowser
import collections as coll



# set user for recommendations
jonathan = '1465258'

# find all listings Jonathan has stayed at
# find all other listings that the other guests of the same listing as Jonathan have stayed at
#   1. find every other guest who stayed at the listings Jonathan stayed at
#   2. for those fellow travelers find the other listings


# find listings for user
def find_listings(records, user_id):
    listings = {record[0] for record in records if record[3] == user_id}
    return listings

# find fellow travelers
def find_travelers(records, listings):
    fellow_travelers = {record[3] for record in records if record[0] in listings}
    return fellow_travelers

# find triangles user is part of
def count_triangles(records, fellow_travelers):
    triangles = [record[0] for record in records if record[3] in fellow_travelers]
    return coll.Counter(triangles)

def recommend_listings(counts, user_listings, num=10):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)
    
    return counts.most_common(num)
    

# the code below only runs if the file is run on the command line,
# not if the modules are imported into another python session
if __name__ == '__main__':
    filename, user_id = sys.argv[1:]

    # open and parse CSV file
    csvfile = open(filename, newline='')
    reader = csv.reader(csvfile)
    headers = next(reader)
    records = list(reader)
    csvfile.close()

    user_listing = find_listings(records, user_id)
    user_fellows = find_travelers(records, user_listing)
    counts = count_triangles(records, user_fellows)
    recommendations = recommend_listings(counts, user_listing)

    # present the results!
    for rec in recommend_listings:
        webbrowser.open('http://airbnb.com/rooms/' + rec[0]) 

    print(recommendations)