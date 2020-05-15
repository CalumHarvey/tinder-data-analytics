import pandas as pd
import json

def swipeRatio(table):

    totalLikes = table["swipes_likes"].sum()
    totalPasses = table["swipes_passes"].sum()
    
    passesPerLike = totalPasses / totalLikes
    likesPerLike = totalLikes / totalLikes

    return passesPerLike, likesPerLike

def matchRatio(table):

    totalLikes = table["swipes_likes"].sum()
    totalMatches = table["matches"].sum()
    
    matchesPerLike = totalLikes / totalMatches
    matchesPerMatch = totalMatches / totalMatches

    return matchesPerLike, matchesPerMatch


with open('test.json') as f:
   temp = json.load(f)

data = pd.DataFrame(temp)

data.index.name = "Date"

data["total_swipes"] = data["swipes_likes"] + data["swipes_passes"]

totalLikes = data["swipes_likes"].sum()
totalPasses = data["swipes_passes"].sum()

swipesRatio = swipeRatio(data)
matchesRatio = matchRatio(data)


print("\nData from: ", data.index[0], " - ", data.index[-1])
print("\nLike to swipe ratio: ", swipesRatio[1], " : ", swipesRatio[0])
print("Matches to like ratio: ", matchesRatio[1], " : ", matchesRatio[0])
print("Total likes: ", data["swipes_likes"].sum())
print("Total passes: ", data["swipes_passes"].sum())
print("Total swipes: ", data["total_swipes"].sum())

print("\n\n\n\n\n\n\n\n\n\n\n Most Attractive Man on Tinder")

#print(data)
