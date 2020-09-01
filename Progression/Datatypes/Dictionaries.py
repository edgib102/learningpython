a_dict = {
    "name": "John",
    "age": 48,
    "hobbies": "drinking",
    "state": "enraged & depressed due to marital disputes"
}

if "drinking" in a_dict.values():
    a_dict["smoking"] = "suspected to be smoking, finacial situation needs to be observed"

for x, y in a_dict.items():
    print(x + ": " + str(y) + "\n")

#does not say this in the .readme becuase i didn't want to mess up formatting
#but I didn't know this before making this script