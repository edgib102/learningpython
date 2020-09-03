import random
a_list = set()

while True:
    rand_int = random.randint(1, 10)
    a_list.add(rand_int)
    print (a_list)
#orginises a set?? idk why but i think i undersatnd them now maybe (then again i dont know why it orginises but whatever)

    
    


#As with tuples, sets are faster than lists (in certain conditons)

#See https://stackoverflow.com/questions/2831212/python-sets-vs-lists, but a tldr below

#Lists are slightly faster than sets when you just want to iterate over the values.
#Sets, however, are significantly faster than lists if you want to check if an item is contained within it.

#Quoted from the stackoverflow link