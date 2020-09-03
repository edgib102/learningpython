path = "Enter path here"
testfile = open(path,"r+") 
testfile.truncate()


def writeinput(wr_input):
    testfile.write(wr_input)

while True:
    print("\nDo you want to write to the .txt file?")
    ans = input("y/n: ")

    if ans == "y":

        TextInput = input("\nEnter text to write: ")
        writeinput(TextInput + "\n")
    
    elif ans == "n":

        print("\nQuit?")
        quit_Yn = input("y/n: ")
        if quit_Yn == "y":
            quit()


    

                  

