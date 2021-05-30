



def frontpage():
    #clearing screen
    import os
    from Bigdatafolder import hdfs
    if os.name=='nt':
        os.system("cls")
    else:
        os.system('clear')

    print("\n\n\n\n\n")
    print("Welcome To The Bigdata (Hadoop)".center(180))
    print()
    print("Which of the following things do you want me to do  :\n\n\n".center(180))
    print("MENU".center(180))
    print("\t\t\t\t\t\t\t\t\t1. Launch an HDFS cluster")
    print("\t\t\t\t\t\t\t\t\t2. Launch an Map-Reduce Cluster")
    print("\t\t\t\t\t\t\t\t\t3. Launch a complete HDFS + Map-Reduce cluster ")
    print()
    print()
    x=input('\t\t\t\t\t\t\t\tEnter any of the number of press b to go back : ')
    if x == '1':
        hdfs.hdfsfront()

    return 'start'
   

#main.main()
