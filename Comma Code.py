

#function takes in a list of strings
#function joins list strings seperating strings with a comma ','
#for the last string in the list, the function will append 'and' BEFORE the string and append it to the join
#function prints the final joined string

def string_joiner(a_list):
    joined_list = ''
    for item in a_list:

        if item == a_list[-1]:
            joined_list += 'and ' + item
            print(joined_list)
        else:
            joined_list += item + ', '
            print(joined_list)

    return joined_list


spam= ['apples', 'bananas', 'tofu', 'cats']

print(string_joiner(spam))