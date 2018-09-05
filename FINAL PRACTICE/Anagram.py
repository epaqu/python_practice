# Description for ¡®is_anagram¡¯ function
# Return True if two words for a ¡°anagram pair¡±; otherwise return False.
def is_anagram(str1, str2) :
    list1 = list(str1)
    list1.sort()
    list2 = list(str2)
    list2.sort()
    return list1 == list2

def get_anagram_indices_of_a_word( a, b ) :
    index_list = []
    for i in range( len(b) ) :
        if is_anagram( a, b[i] ) :
            index_list.append(i)
    index_list.reverse()
    return index_list

def pop_words( a, b ) :
    sub_list = []
    for i in a :
        sub_list.append( b.pop(i) )
    return sub_list

def compare(list1, list2) :
    return cmp(list2, list1)

word_list = [ 'deltas', 'lasted', 'enlist', 'staled', 'generating',
'slated', 'silent', 'listen', 'greatening' ]

result_list = []

while len(word_list) > 0 :
    anagram_list = [ word_list.pop(0) ]
    index_list = get_anagram_indices_of_a_word(anagram_list[0], word_list)
    anagram_list += pop_words(index_list, word_list)
    result_list.append( anagram_list )

print word_list, result_list
result_list.sort(compare)
print result_list
result_list.sort(compare)
print result_list