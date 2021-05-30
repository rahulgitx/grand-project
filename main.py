def main():
    x='start'
    while x=='start':
        import os
        from Bigdatafolder import Bigdata

        #clearing screen
        if os.name=='nt':
            os.system("cls")
        else:
            os.system('clear')


        print("\n\n\n\n\n")
        print("Welcome To The Future".center(180))
        print()
        print("Which of the following services do you want to work one:\n\n\n".center(180))
        print("MENU".center(180))
        print("\t\t\t\t\t\t\t\t\t\t1. Bigdata (Hadoop)")
        print("\t\t\t\t\t\t\t\t\t\t2. Ansible")
        print("\t\t\t\t\t\t\t\t\t\t3. Cloud ")
        print("\t\t\t\t\t\t\t\t\t\t4. Docker")
        print("\t\t\t\t\t\t\t\t\t\t5. Kubernetes ")
        print("\t\t\t\t\t\t\t\t\t\t6. Jenkins")
        print()
        print()

        x=input("\t\t\t\t\t\t\t\t\tChoose any of the above number : ")
        while x=='1':
            x=Bigdata.frontpage()
            print('done')
        if x=='2':
            print('This section is under maintenance please come back another time : '.center(180), x)
            x='start'
            input()
        if x !='1' and x !='2' and x != 'start':
            print('\t\t\t\t\t\t\t\tPlease give an appropriate input(press enter to try again)')
            x='start'
            input()

main()

