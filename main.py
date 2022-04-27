import covid


choice = input("To see current events and COVID-19 information in Pittsburgh, please enter 'C': ")
if choice == 'C':
    covid.covidCheck()