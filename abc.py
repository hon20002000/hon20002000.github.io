#method_1
# =============================================================================
# path ='abc.csv'
# file = open(path, 'r')    #open的默認條件是'r', 'r'可寫也可不寫  
# contents = file.readlines()
# 
# for content in contents[1:]:
#     student = content.split(',')[0]
#     score = content.split(',')[1]
#     print("{}: {}".format(student, score), end='')
# =============================================================================

dict_a = {}
dict_a['user_1'] = 'sam'
dict_a['user_2'] = 'mary'
dict_a['user_3'] = 'hon20002000'
dict_b = {}
dict_b['house_1'] = 3000
dict_b['house_2'] = 5000
dict_b['house_3'] = 7000
print("dict_a:", dict_a)
print("dict_b:", dict_b)