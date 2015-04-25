def count_frequency(list) :
    list_set = set(list)
    dictionary = {}
    for element in list_set :
        count = 0
        for ele in list :
            if (element == ele) :
                count += 1
        dictionary[element] = count
    return dictionary
print(count_frequency(["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]))