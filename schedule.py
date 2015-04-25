

class db:
    def __init__(self):
        self.responsibles=[]
        self.teams=[]
        self.clubs=[]

    def add_line(self,line):
        ri = self.create_and_add_responsible(line)
        print str(ri)

    def create_and_add_responsible(self,line):
        r = responsible(line[4],line[5],line[6])
        return self.add_and_return_index(r,self.responsibles)

    def add_and_return_index(self,elem,elem_list):
        try:
            return elem_list.index(elem)
        except ValueError:
            pass
        elem_list.append(elem)
        return len(elem_list)-1

        

class responsible:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone.replace(' ','')

    def __eq__(self,other):
        if self.phone==other.phone:
            if self.name != other.name or self.email != other.email:
                print ("Warning: Same key but info differs:\n" + str(self) + "\n"  + str(other))
            return True
        return False

    def __str__(self):
        return "(" + self.name + "," + self.email + "," + self.phone + ")"







class team:
    def __init__(self,name,group_id,responsible_id):
        pass

if __name__=="__main__":
    mdb = db()

    fid = (('0000000','VUL 1','G06','VUL','stian','sjefen@vul.no','41764253',''),
           ('0000000','VUL 2','G06','VUL','stian','sjefen@vul.no','41764253',''),
           ('0000000','VUL 1','G07','VUL','ole','sjefen2@vul.no','41764252',''),
           ('0000000','VUL 2','G07','VUL','ole','sjefen2@vul.no','41764252',''))
    
    for line in fid:
        mdb.add_line(line)


