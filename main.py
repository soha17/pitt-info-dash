import covid
import announcements

choice = '1'
while(choice != 'END'):
    print('----------------------------------------------------------------------------------------')
    print("- To exit the program, enter 'END'")
    print("- To see current event announcements in Pittsburgh, enter 'A'")
    print("- To see current COVID-19 information in Allegheny County, please enter 'C'")
    print("- If you want to see the references used for each part of the program, please enter 'REF'")
    choice = input("Enter your choice: ")
    if choice == 'C':
        covid.covidCheck()
    elif choice == 'A':
        announcements.announcements()
    elif choice == 'END':
        print('Goodbye!')
    elif choice == 'REF':
        print("COVID-19 References: https://covidactnow.org/?s=32892108")
        print("Pittsburgh Event Announcements: https://www.visitpittsburgh.com/events-festivals/")
    else:
        print('Please enter a valid choice')