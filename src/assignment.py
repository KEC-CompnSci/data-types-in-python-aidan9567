# Create the requested sentence by converting and combining these variables
# You may not add any additional string or numeric literals
# You can only use these variables, type conversion, and string concatenation

num_str_1 = "42"
num_str_2 = "13"
num_str_3 = "7"
word_1 = " robots "
word_2 = "built "
word_3 = "today"
word_4 = "were "


num_int_1 = int(num_str_1)
num_int_2 = int(num_str_2)

word_str_1 = str(num_int_1 + num_int_2)

word_str_2 = str(word_1 + word_4 + word_2 + word_3)
sentence =(word_str_1 + word_str_2)
print (sentence)