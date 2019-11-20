f = open('LIWC_dic.txt','r')
counter_word = {}
LIWC = f.readlines()
LIWC_dict = {}
for line in LIWC:
    line = line.split(',')
    category = line[0]
    words = line[1].split(' ')
    words[-1] = words[-1][:-1]
    LIWC_dict[category] = words
    for word in words:
        if word.endswith('*'):
            if word not in counter_word.keys():
                counter_word[word] = 1
            else:
                counter_word[word] += 1
        else:
            temp_word = word[:-1]+'*'
            if temp_word in counter_word.keys():
                counter_word[temp_word] += 1
            else:
                if word not in counter_word.keys():
                    counter_word[word] = 1
                else:
                    counter_word[word] += 1
counter_word_tuple = sorted(counter_word.items(),key=lambda x:x[1],reverse=True)
print('{:15}\t{}'.format('word','number_of_word'))
for word,num in counter_word_tuple:
    print('{:15}\t{}'.format(word,num))
    