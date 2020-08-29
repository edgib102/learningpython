print("type word to stutter:")
def stutter(word):
    cutword = word[0:2]
    print(cutword)
    result = cutword + "... " + cutword + "... " + word + "?"
    print(result)
    return(result)


stutter(input())
    


#Start of the easy challenges
#Goal is to make a string to stutter like this: "in... in... incredible?" (any word)
#Challenge from https://edabit.com/challenge/gt9LLufDCMHKMioh2