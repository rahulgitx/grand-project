def hdfsfront():
    #clearing screen
    import os
    import Bigdatafolder.hdfs 
    if os.name=='nt':
        os.system("cls")
    else:
        os.system('clear')

    print("\n\n\n\n\n")
    print("Welcome To The HDFS cluster creation page".center(180))
    print()
    print("Please enter the following information about your hdfs cluster : \n\n\n".center(180))
    getip()


def getip():                    # get the no of slave nodes and their IPs
    mn=input('\t\t\t\t\t\t\t\tEnter the IP of master node : ')
    sn=input("\t\t\t\t\t\t\t\t* How many slave nodes do you want to create ? ")
    sns=[]
    print(int(sn))
    for i in range(int(sn)):
        print('\t\t\t\t\t\t\t\tEnter the IP address of slave node', i+1, ' : ', end='')
        x=input()
        sns.append(x)
    print()
    print('\t\t\t\t\t\t\t\tIP of master node : ', mn)
    for i in range(len(sns)):
        print('\t\t\t\t\t\t\t\tIP of Slave node', i, ':', sns[i])
    choice=input("\t\t\t\t\t\t\t\tDo you want to continue (Press y/n) or go back (Press b)")   
    if choice=='y':
        print('\t\t\t\t\t\t\t\tContinuing...')
    input()