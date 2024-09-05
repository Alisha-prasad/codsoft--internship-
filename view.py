import sys
import csv

def add(i):
    with open ('data.csv','a+',newline='') as file:
        writer= csv.writer(file)
        writer.writerow(i)


add(['alisha', 'data@gmail.com','234567','q-2ess'])
add(['demo','derfd@gmil.com','1234','wetbdi2'])

def view():
    data=[]
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

view()

def remove(i):

    def save(j):
        with open('data.csv','w' ,newline='') as file:
            writer =csv.writer(file)
            writer.writerows(j)

    new_list=[]
    phonenumber=i

    with open('data.csv' ,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

        for element in row:
            if element == phonenumber:
                new_list.remove(row)
    
    save(new_list)

#remove(123465)
#view()

def update(i):

    def update_newlist(j):
        with open('data.csv','w',newline='') as file:
            writer =csv.writer(file)
            writer.writerows(j)
 
    new_list=[]
    phonenumber=i[0]
    #['34564','demo','f','34564','derfd@gmil.com']


    with open('data.csv','r') as file:
        reader =csv.reader(file)
        for row in reader:
            new_list.append(row)

        for element in row:
            if element == phonenumber:
                name=i[1]
                Email=i[2]
                phonenumber=i[3]
                Address=i[4]

                data =[name ,email,phonenumber,Address]
                index=new_list.index(row)
                new_list[index]=data

    update_newlist(new_list)
    

#sample=['123','girlcoder','f','123','girlcoder@gmail.com']
#update(sample)

def search(i):
    data=[]
    phonenumber=i

    with open('data.csv','r') as file:
        reader =csv.reader(file)
        for row in reader:
            for element in row:
                if element==phonenumber:
                    data.append(row)

    print(data) 
    return data

search('123')


            








    
    
        

        
