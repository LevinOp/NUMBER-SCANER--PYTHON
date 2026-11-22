print("====NUMBER SCANER====")
while True:

    print("1. see how many numbers are even")
    print("2. see how many numbers are odd")
    print("3. see how many prime numbers")
    print("4. see how many numbers are divisable by 5")
    print('5.Exit')

    option=int(input('select an option: '))

    if option == 1:
        num_1=int(input('Enter a number: '))
        num_2=int(input('Enter the limit: '))

        even=0

        for i in range(1,num_2+1):
            if i % 2==0:
                print(i)
                even+=1
        print(f'There are {even} even numbers')

    elif option==2:
        num_1=int(input('Enter a number: '))
        num_2=int(input('Enter the limit: '))

        odd=0

        for i in range(1,num_2+1):
            if i % 2==1:
                print(i)
                odd+=1
        print(f"There are {odd} odd numbers")

    elif option ==3:
        num_1=int(input('Enter a number: '))
        num_2=int(input('Enter the limit: '))

        prime=0
        
        for i in range(1, num_2 + 1):

            count = 0

            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1

            if count == 2:
                print(i)
                prime += 1

        print(f"These are {prime} prime numbers")

    elif option ==4:
        num_1=int(input('Enter a number: '))
        num_2=int(input('Enter the limit: '))

        div=0

        for i in range(num_1,num_2+1):
            if i%5 == 0:
                print(i)
                div+=1
        print(f'There are {div} numbers which are divisable by 5')
    elif option==5:
        break