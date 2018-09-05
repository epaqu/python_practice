from calendar import *

start_year = 1901
end_year = 2100

start_month = 1
end_month = 12

def string_to_date(s) :
    tmp_year = 0
    tmp_month = 0
    tmp_day = 0    
    if( len(s) == 10 and s[4] == '.' and s[7] == '.' and s[0:4].isdigit() and s[5:7].isdigit() and s[8:].isdigit() ) :
	tmp_year = int( s[0:4] )
	tmp_month = int( s[5:7] )
	tmp_day = int( s[8:] )    
    return ( tmp_year, tmp_month, tmp_day )

def print_date_and_day( tmp_year, tmp_month, tmp_day ) :
    print '%d.%02d.%02d is %s\n' % ( tmp_year, tmp_month, tmp_day, what_day( date_to_num(tmp_year, tmp_month, tmp_day) ) )
    
def print_two_dates_and_num_of_days( res_year, res_month, res_day, num_of_days, base_year, base_month, base_day ) :
    print '%d.%02d.%02d has been %d days since %d.%02d.%02d\n' % (res_year, res_month, res_day, num_of_days, base_year, base_month, base_day)


######################################################################################################
######################################################################################################
def month_to_num_of_days( tmp_year, tmp_month ) :
    num_of_days = 0
    if isleap(tmp_year) and tmp_month == 2:
	num_of_days = 29
    elif tmp_month == 2:
	num_of_days = 28
    elif tmp_month == 1 or tmp_month == 3 or tmp_month == 5 or tmp_month == 7 or tmp_month == 8 or tmp_month == 10 or tmp_month == 12:
	num_of_days = 31
    else:
	num_of_days = 30
    return num_of_days

def is_valid_date( tmp_year, tmp_month, tmp_day ) :
    check_result = False
    global start_year, end_year, start_month, end_month
    if tmp_year < start_year or tmp_year > end_year or tmp_month < start_month or tmp_month > end_month:
	return check_result
    month_length = month_to_num_of_days(tmp_year, tmp_month)
    if tmp_day < 1 or tmp_day > month_length:
	return check_result
    return True

def what_day(n) :
    res_day = ''
    if n % 7 == 1:
	res_day += "Tuesday"
    elif n % 7 == 2:
	res_day += "Wednesday"
    elif n % 7 == 3:
	res_day += "Thursday"
    elif n % 7 == 4:
	res_day += "Friday"
    elif n % 7 == 5:
	res_day += "Saturday"
    elif n % 7 == 6:
	res_day += "Sunday"
    elif n % 7 == 0:
	res_day += "Monday"
    return res_day

def date_to_num( tmp_year, tmp_month, tmp_day ) :
    num_of_days = 0
    if tmp_year > 1901:
	for i in range (1901, tmp_year):
	    if isleap(i):
		num_of_days += 366
	    else:
		num_of_days += 365
    for j in range (1, tmp_month):
	num_of_days += month_to_num_of_days(tmp_year, j)
    num_of_days += tmp_day
    return num_of_days

def num_to_date(n) :
    tmp_year = 0
    tmp_month = 0
    tmp_day = 0
    tmp_year += 1901
    tmp_month += 1
    while n > 365:
	if isleap(tmp_year):
	    if n > 366:
		tmp_year += 1
		n -= 366
	else:
	    tmp_year += 1
	    n -= 365
    for i in range (1, 13):
	if n > month_to_num_of_days(tmp_year, i):
	    tmp_month += 1
	    n -= month_to_num_of_days(tmp_year, i)
    tmp_day += n
    return ( tmp_year, tmp_month, tmp_day )

def date_after_days(base_year, base_month, base_day, number_of_days ) :
    tmp_year = 0
    tmp_month = 0
    tmp_day = 0
    days_til_base = date_to_num(base_year, base_month, base_day)
    number_of_days += days_til_base - 1
    tmp_year, tmp_month, tmp_day = num_to_date(number_of_days)
    return ( tmp_year, tmp_month, tmp_day )

def num_of_days_between_dates( base_year, base_month, base_day, new_year, new_month, new_day ) :
    num_of_days = 1
    num_of_days += date_to_num(new_year, new_month, new_day)
    num_of_days -= date_to_num(base_year, base_month, base_day)
    if num_of_days < 0:
	num_of_days -= 1
    return num_of_days

######################################################################################################
######################################################################################################


base_year, base_month, base_day = string_to_date( raw_input( 'Enter base date : ' ) )
while (base_year, base_month, base_day) == ( 0, 0, 0 ) :
    print 'Enter date with the format like following : yyyy.mm.dd\n'
    base_year, base_month, base_day = string_to_date( raw_input( 'Enter base date : ' ) )

if is_valid_date( base_year, base_month, base_day ) :
    print_date_and_day( base_year, base_month, base_day )
    choice = raw_input( '1. How many days later?\n2. What date?\n3. Quit\nSelect : ' )
    while ( not choice.isdigit() ) or ( not ( int(choice)==1 or int(choice)==2 or int(choice)==3 ) ) :
	print 'Enter only numbers between 1 and 3!\n'
	choice = raw_input( "1. How many days later?\n2. What date?\n3. Quit\nSelect : " )
    choice = int( choice )
    
    if choice == 1 :
	num_of_days = raw_input( '\nHow many days later do you want to know : ' )
	while ( not num_of_days.isdigit() ) or ( not int(num_of_days) >= 1 ) :
	    print 'Enter only positive numbers!\n'
	    num_of_days = raw_input( 'How many days later do you want to know : ' )
	num_of_days = int( num_of_days )	
	
	res_year, res_month, res_day = date_after_days( base_year, base_month, base_day, num_of_days )
	print_date_and_day( res_year, res_month, res_day )
	print_two_dates_and_num_of_days( res_year, res_month, res_day, num_of_days, base_year, base_month, base_day )
	
    elif choice == 2 :
	new_year, new_month, new_day = string_to_date( raw_input( '\nEnter a date : ' ) )
	while (new_year, new_month, new_day) == ( 0, 0, 0 ) :
	    print 'Enter date with the format like following : yyyy.mm.dd\n'
	    new_year, new_month, new_day = string_to_date( raw_input( '\nEnter a date : ' ) )
	
	if is_valid_date( new_year, new_month, new_day ) :
	    print_date_and_day( new_year, new_month, new_day )
	    num_of_days = num_of_days_between_dates( base_year, base_month, base_day, new_year, new_month, new_day )	    
	    print_two_dates_and_num_of_days( new_year, new_month, new_day, num_of_days, base_year, base_month, base_day )
	else :
	    print 'You can input a date between %d.%02d.01 and %d.%02d.31' % (start_year, start_month, end_year, end_month)

else :
    print 'You can input a date between %d.%02d.01 and %d.%02d.31' % (start_year, start_month, end_year, end_month)