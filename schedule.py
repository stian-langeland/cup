
class db:
    def __init__(self):
        self.responsibles=[]
        self.teams=[]
        self.clubs=[]

    def add_line(self,line):
        ri = self.create_and_add_responsible(line)
        self.teams.append(team(line[1],ri,None,None))

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

    def __str__(self):
        t = "Teams\n"
        t += "\n".join([str(t) for t in self.teams])
        return t

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
    def __init__(self,name,responsible_id,group_id,club_id):
        self.name = name
        self.responsible_id = responsible_id
        self.group_id = group_id
        self.club_id = club_id

    def __str__(self):
        return self.name

def read_csv(filename):
    skipped_header = False
    registrations = []
    for line in open(filename,"r"):
        if not skipped_header:
            skipped_header = True
        else:
            registrations.append(line.strip().split(";"))
    return registrations

if __name__=="__main__":
    mdb = db()

    registrations = read_csv("registrations.csv")

    for line in registrations:
        mdb.add_line(line)
    print (str(mdb))


