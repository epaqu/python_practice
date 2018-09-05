from cs1graphics import *
import math

f = open("./character.csv","r")

##########################################################
#implement Person class
class Person():
    def __init__(self,s_id,name,e_i,s_n):
        self.s_id = s_id
        self.name = name
        self.E_I = e_i
        self.S_N = s_n
        
    def calDist(self,other):
        return abs(self.E_I - other.E_I) + abs(self.S_N - other.S_N)
##########################################################
        
people = []
f.readline()
##########################################################
ei = 0
sn = 0
for individual in f:
    person = individual.strip().split(",")
    for i in range (3, 23):
        if i%2 == 1:
            ei += int(person[i])
        else:
            sn += int(person[i])
    people.append(Person(person[1], person[2], ei, sn))
    ei = 0
    sn = 0
#fill the list 'people' with Person instances. You should also aggregate each characteristic values(E_I and S_N). By skipping the foremost three information(time, ID, and name), the information at odd number is according to E_I(extroverts or introverts), the even number according to S_N(sensing or intuition). 
##########################################################

canvas = Canvas(450,450)
canvas.setTitle("The Colour of Our Section")
offset = 25
for i in range(11):
    pt = Path(Point(0,offset+i*40))
    pt.addPoint(Point(450,offset+i*40))
    pt.setDepth(100)
    pt.setBorderColor((200,200,200))
    canvas.add(pt)
    pt2 = Path(Point(offset+i*40,0))
    pt2.addPoint(Point(offset+i*40,450))
    pt2.setDepth(100)
    pt2.setBorderColor((200,200,200))
    canvas.add(pt2)

# get information from people
people_list = []
people_count = []
for i in range(len(people)):
    person = people[i]
    print person.name, person.E_I, person.S_N
    if not (person.E_I,person.S_N) in people_list:
        people_list.append((person.E_I,person.S_N))
        people_count.append(1)
    else:
        for j in range(len(people_list)):
            if (person.E_I,person.S_N) == people_list[j]:
                people_count[j]+=1

for j in range(len(people_list)):
    circle = Circle(people_count[j]*4+2,Point(people_list[j][0]*40+offset,people_list[j][1]*40+offset))
    circle.setFillColor((255-people_count[j]*10,255-people_list[j][0]*20,255-people_list[j][1]*20))
    pt.setDepth(100-(50-people_count[j]))
    canvas.add(circle)
    
e = Text("E",20,Point(15,225))
canvas.add(e)
i = Text("I",20,Point(450-15,225))
canvas.add(i)
s = Text("S",20,Point(225,17))
canvas.add(s)
n = Text("N",20,Point(225,450-15))
canvas.add(n)

#get the student ID of mine
s_id = input("Give me your student ID : ")
my_friends = []
me = None
for person in people:
    if s_id == int(person.s_id):
        me = person
        print me.name
        
##########################################################
#get the nearest neighborhoods using the calDist function
people_except_me = []
for person in people:
    if person != me:
        people_except_me.append(person)
BF = people_except_me[0]
for person in people_except_me:
    if me.calDist(person) < me.calDist(BF):
        BF == person
for person in people_except_me:
    if me.calDist(BF) == me.calDist(person):
        my_friends.append(person)
##########################################################

#print out my best friends!
print "My best friend!"
for person in my_friends:
    print person.name,me.calDist(person)