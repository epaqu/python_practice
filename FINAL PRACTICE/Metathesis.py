def is_metathesis( str1, str2 ) :
    result_val = False
    if len(str1) == len(str2) :
        list1 = list(str1)
        list2 = list(str2)
        temp = ""
        for i in range (len(str1)):
            for j in range (len(str1)):
                temp = list1[j]
                list1[j] = list1[i]
                list1[i] = temp
                if list1 == list2:
                    result_val = True
                list1 = list(str1)
    return result_val
print is_metathesis( 'converse', 'coversen' )
print is_metathesis( 'converse', 'conserve' )
print is_metathesis( 'converse', 'conserves' )
print is_metathesis( 'conserves', 'converse' )
print is_metathesis( "conberse", "conserve" )
