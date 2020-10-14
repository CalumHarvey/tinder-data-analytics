#Tinder Analysis - Calum Harvey
import pandas as pd
import json

def swipeRatio(table):

    totalLikes = table["swipes_likes"].sum()
    totalPasses = table["swipes_passes"].sum()
    
    passesPerLike = "{:.2f}".format(totalPasses / totalLikes)
    likesPerLike = totalLikes / totalLikes

    return passesPerLike, likesPerLike

def matchRatio(table):

    totalLikes = table["swipes_likes"].sum()
    totalMatches = table["matches"].sum()
    
    matchesPerLike = "{:.2f}".format(totalLikes / totalMatches)
    matchesPerMatch = totalMatches / totalMatches

    return matchesPerLike, matchesPerMatch

def openFile(name="data.json"):

    #Swiped Data contains data on swipes taken from full json file given
    with open('data.json', "r") as json_file:
        temp = json.load(json_file)

    temp2 = temp["Usage"]

    data = pd.DataFrame(temp2)

    return data

def main():

    data = openFile()

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


if __name__ == "__main__":
    main()
