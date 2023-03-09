import datetime
import requests
import re
from soccer_data_api import SoccerDataAPI
from os import system, name
from constants import NEWS_TEXT, AD_TEXT, CLUB_TEXT


class File:

    def write_data(self, text):
        """ write data to file """
        try:
            with open('news_feed.txt', mode='a', encoding='utf-8') as feed_file:
                feed_file.write(text)
        except IOError:
            print('Could not open file.')

    def get_text(self, input_description):
        while True:
            input_text = input(input_description)
            if input_text:
                return input_text
            else:
                print('You entered an empty string, try again:')


class News(File):

    def __init__(self):
        self.main_text, self.date_time, self.city = None, None, None
        
        # call class methods during object creation
        self.main_text = self.get_text('Write the text for news: ')
        self.set_date_time()
        self.set_city()
        
    def set_date_time(self):
        # set current date for object
        now = datetime.datetime.now()
        self.date_time = now.strftime("%m/%d/%Y %H.%M")

    def city_verification(self, city_name):
        verification_result = True
        
        # make responce with city name, to get info about intered city
        responce = requests.request(
            'GET', f"https://www.geonames.org/advanced-search.html?q={city_name}&country=&featureClass=P&continentCode=", timeout=5)
        
        # patterns that are searched in responce
        patterns_city = ['/city_name.html', '>city_name<', '/city_name">']
        
        for count, pattern in enumerate(patterns_city, start=1):

            # change 'city_name' with entered value by user
            pattern = re.sub('city_name', self.city, pattern)

            match_pattern = re.search(pattern, responce.text, re.IGNORECASE)

            if match_pattern is not None:
                break

            if count == len(patterns_city):
                print("Entered city wasn't find.")
                verification_result = False
        
        return verification_result

    def set_city(self):
        while True:
            self.city = self.get_text('Write the city name: ')
            
            if self.city_verification(self.city):
                break
            else: continue

    def get_news(self):
        news_text = NEWS_TEXT.format(main_text=self.main_text, city=self.city, date_time=self.date_time)
        return news_text
        

class Ad(File):

    def __init__(self):
        self.main_text, self.until_date, self.days_left = None, None, None
        self.main_text = self.get_text('Write the text for ad: ')
        self.set_date()

    def date_verification(self, until_date):
        verification_result = True
        date_format = '%m/%d/%Y'

        # verify, that user entered correct date format or date > current date
        try:
            date_object = datetime.datetime.strptime(until_date, date_format)
        except ValueError:
            print('Incorrect date format was entered, try again: ')
            verification_result = False
        else:
            difference_date = date_object - datetime.datetime.today()
            self.days_left = difference_date.days

            if self.days_left <= 0:
                print('The difference between the expiration date and current date should be at least 1 day.')
                verification_result = False
        
        return verification_result
        

    def set_date(self):
        while True:
            self.until_date = input('Enter the expiration date, example: 03/30/2023 : ')
            if self.date_verification(self.until_date):
                break
            else:
                continue

    def get_ad(self):
        ad_text = AD_TEXT.format(main_text=self.main_text, until_date=self.until_date, days_left=self.days_left)
        return ad_text

        
class LaLiga(File):
    
    def __init__(self):
        self.club_name, self.team_info = None, None

        # create soccer object with API, to get info about spain football clubs
        soccer_data = SoccerDataAPI()
        
        # get list of dicttionaries with clubs info
        self.liga_list = soccer_data.la_liga()

        # call method to enter club name
        self.set_club_name()

    def club_verification(self, club_name):
        # get info about entered club by user
        team = [team for team in self.liga_list if team['team'].upper() == club_name]

        # verify that user club was found in self.liga_list
        if len(team) == 0:
            print('Club was not find, try again: ')
            return False
        else:
            return team[0]

    def set_club_name(self):
        while True:
            self.club_name = self.get_text('Write the club name from Spain ligue, for example (Barcelona, Elche, Real Madrid): ').upper()
            verification_result = self.club_verification(self.club_name)
            
            if verification_result is False:
                continue
            else:
                self.team_info = verification_result
                break

    def get_club_results(self):
        club_text = CLUB_TEXT.format(team=self.team_info['team'], position=self.team_info['pos'], poits=self.team_info['points'])
        return club_text
        

class Menu:

    def run_menu(self):
        while True:
            chosen_number = input(
                'Choose the number of operation:\n1 - Add news\n2 - Add Ad\n3 - Add LaLiga club result\n4 - Exit\n:')

            if chosen_number not in ['1', '2', '3', '4']:
                system('cls')
                print('Choose the right number of operation, try again.')
                continue

            match chosen_number:
                case '1':
                    news_object = News()
                    news_text = news_object.get_news()
                    news_object.write_data(news_text)
                    print('News was added.\n')
                
                case '2':
                    ad_object = Ad()
                    ad_text = ad_object.get_ad()
                    ad_object.write_data(ad_text)
                    print('Ad was added.\n')
                
                case '3':
                    liga_object = LaLiga()
                    liga_text = liga_object.get_club_results()
                    liga_object.write_data(liga_text)
                    print('Club result was added.\n')
                
                case '4':
                    break


def main():
    menu = Menu()
    menu.run_menu()


if __name__ == "__main__":
    main()