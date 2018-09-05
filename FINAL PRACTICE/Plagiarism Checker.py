def catch_plagiarism(filename1, filename2):
    f1 = open(filename1,"r")
    f2 = open(filename2,"r")
    result = open("./result.txt", "w")
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 == "" or line2 == "":
            break
        #if the line includes only "\n", fetch the next line
        while len(line1) == 1:
            line1 = f1.readline()
        while len(line2) == 1:
            line2 = f2.readline()
            #comparison between two lines
        if line1.strip() == line2.strip():
            print line1.strip()
        else:
            line1_list = line1.split("=")
            line2_list = line2.split("=")
            for i in range(len(line1_list)):
                if line1_list[i].strip() != line2_list[i].strip():
                    result.write("1. py: %s\n" %(line1_list[i]))
                    result.write("2. py: %s\n" %(line2_list[i]))                            
        if line1 == "" or line2 == "":
            break
        #end of while-loop
    print "completed!"
    f1.close()
    f2.close()
    result.close()

catch_plagiarism("./20100020.py.txt","./20101120.py.txt")