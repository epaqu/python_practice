# Description for ¡®has_duplicates¡¯ function
# Take a list and return True if there is any element that appears more than
# once; otherwise return False.
def has_duplicates( a_list ) :
    result_val = False
    for i in range( len(a_list) ) :
        if a_list[i] in (a_list[i+1:]) :
            result_val = True
            break
    return result_val
# Description for ¡®remove_duplicates¡¯ function
# Take a list and return a new list with only the unique elements from the
# original.
def remove_duplicates( a_list ) :
    result_list = []
    for i in range (len(a_list)):
        if not a_list[i] in result_list:
            result_list.append(a_list[i])
    return result_list

test_list = [ 'deltas', 'lasted', 'salted', 'lasted', 'salted' ]
if has_duplicates( test_list ) :
    print remove_duplicates( test_list )