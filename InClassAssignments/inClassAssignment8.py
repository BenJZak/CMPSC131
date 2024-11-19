# List Comprehension

list_of_squares = [i**2 for i in range(11)]
print(list_of_squares)

yes_no_list = ['yes' if i%3==0 else 'no' for i in range(11)]
print(yes_no_list)

list_of_tuples = [(i, i**2) for i in range(6)]
print(list_of_tuples)

# Dictionary Comprehension

dic_alpha = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
}
alpha = ['a', 'b', 'c', 'd', 'e']
inverted_dic_alpha = {v: k for k, v in dic_alpha.items()}
yes_no_dic = {i:'yes' if i%3==0 else 'no' for i in range(1, 11)}
print(yes_no_dic)

# Combining Both

combined = {k:[i for i in range(11) if i%k==0] for k in range(1, 6)}
print(combined)