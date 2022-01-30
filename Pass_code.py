import random
import string
def password_decoder(w_name):
    if(w_name.count(" ")==1):
        n_lst1 = w_name.split(" ")
        name=n_lst1[0]
        surname=n_lst1[1]
        n_lst2=[]
        n_lst2.extend(name)
        n_lst2
        n_lst2.extend(surname)
        #print(n_lst2)
        dic = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        n_dic ={}
        dum=[]
        for i in range(0 , len(n_lst1)):
            for j in range(0,len(n_lst1[i])):
                if n_lst1[i][j] in dum:
                    pass
                else:
                    dum.append(n_lst1[i][j])
            if(i==0):
                name=dum.copy()
                dum.clear()
            surname=dum.copy()
        #print("name is: ",name)
        #print("surname is: ",surname)
        for i in range(0,len(name)):
            n_dic[name[i]]=dic[name[i].lower()]
        for i in range(0,len(surname)):
            n_dic[surname[i]]=dic[surname[i].lower()]
        #print(n_dic,len(name),len(surname))
        num =random.randint(0,len(name))
        num2=random.randint(0,len(surname))
        s_code=n_dic[name[num-1]]+n_dic[surname[num2-1]]
        for key,value in dic.items():
            if value==s_code:
                s_key=key
            else:
                s_key=random.choice(string.ascii_letters)
        #print("secreat code: ",s_code)
        #print("secreat key: ",s_key)
        #print("PASSWORD GENERATED IS: ")
        codee=f"{name[num-1]}{str(n_dic[name[num-1]])}{surname[num2-1]}{str(n_dic[surname[num2-1]])}{s_key}{str(s_code)}"
        #print(codee)
        return codee

w_name=input("enter your name and surname with space ")
var=password_decoder(w_name)
print(f"YOUR PASSWORD GENERATED IS : {var}")

