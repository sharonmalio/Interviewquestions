
def longest(string_list):
    count = 0
    for i in string_list:
        if len(i)>count:
            count = len(i)
            word = i
    print word
longest(['sharon', 'rocky', '123456789', 'marthaka'])

# def longest1(string_list):
#     string_max = max(string_list, key=len)
#     return string_max
# longest1(['sharon', 'rocky', '123456789', 'marthaka'])

