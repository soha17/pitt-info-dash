from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup

def announcements():
    html = urlopen('https://www.visitpittsburgh.com/events-festivals/')

    bsyc = BeautifulSoup(html.read(), "lxml")


    # get a list of all table tags
    # events_list = bsyc.findAll('div', {"class": "card__body text-center"})
    events_list = bsyc.findAll('h4', {"class": "card__title"})
    dates_list = bsyc.findAll('div', {"class": "cal-date__container"})
    # how many are there?
    # print('there are', len(events_list), 'tables', events_list)

    # print(events_list)
    # print('there are', len(dates_list), 'tables', dates_list)

    events_titles = []
    for val in events_list:
        events_titles.append(str((val.find('a').contents[0])))

    all_years = []
    all_months = []
    all_days = []
    for val in dates_list:
        curr = val.find_all('span')
        all_years.append(curr[0].text)
        all_days.append(curr[1].text)
        all_months.append(curr[2].text)

    print('----------------------------------------------------------------------------------------')
    for event, month, day, year in zip(events_titles, all_months, all_days, all_years):
        print(event, 'on', month, day, year)