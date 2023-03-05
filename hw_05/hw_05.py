import datetime
import requests
import re
from soccer_data_api import SoccerDataAPI
from os import system, name


class File():

    def write_data(self, text):
        """ write data to file """
        try:
            with open('news_feed.txt', mode='a', encoding='utf-8') as feed_file:
                feed_file.write(text)

        except IOError:
            print('Could not open file.')


class News(File):

    def __init__(self):
        # call class methods during object creation
        self.set_text()
        self.set_date_time()
        self.set_city()

    def set_text(self):
        # set text for News
        while_condition = True

        while(while_condition):
            self.__main_text = input('Write the text for news: ')

            if not self.__main_text:
                print('You entered an empty string, try again:')
                continue

            while_condition = False

    def set_date_time(self):
        # set current date for object
        now = datetime.datetime.now()
        self.__date_time = now.strftime("%m/%d/%Y %H.%M")

    def set_city(self):
        while_condition = True

        while(while_condition):
            self.__city = input('Write the city name: ')

            if not self.__city:
                print('You entered an empty string, try again:')
                continue

            # make responce with city name, to get info about intered city
            responce = requests.request(
                'GET', f"https://www.geonames.org/advanced-search.html?q={self.__city}&country=&featureClass=P&continentCode=", timeout=5)

            # patterns that are searched in responce
            patterns_city = ['/city_name.html', '>city_name<', '/city_name">']

            # if info about city wasn't found, user will be informed
            for count, pattern in enumerate(patterns_city, start=1):

                # change 'city_name' with entered value by user
                pattern = re.sub('city_name', self.__city, pattern)

                match_pattern = re.search(
                    pattern, responce.text, re.IGNORECASE)

                if match_pattern is not None:
                    while_condition = False
                    break

                if count == len(patterns_city):
                    print("Entered city wasn't find.")

    def get_news(self):
        return f'''News -------------------------\n{self.__main_text}\n{self.__city}, {self.__date_time}\n------------------------------\n\n'''


class Ad(File):

    def __init__(self):
        self.set_text()
        self.set_date()

    def set_text(self):
        while_condition = True

        while(while_condition):
            self.__main_text = input('Write the text for ad: ')

            if not self.__main_text:
                print('You entered an empty string, try again:')
                continue

            while_condition = False

    def set_date(self):
        while_condition = True

        while(while_condition):

            self.__until_date = input(
                'Enter the expiration date, example: 03/30/2023 : ')

            date_format = '%m/%d/%Y'

            # verify, that user entered correct date format or date > current date
            try:
                date_object = datetime.datetime.strptime(
                    self.__until_date, date_format)
            except ValueError:
                print('Incorrect date format was entered, try again: ')
                continue
            else:
                difference_date = date_object - datetime.datetime.today()
                self.__days_left = difference_date.days

                if self.__days_left <= 0:
                    print(
                        'The difference between the expiration date and current date should be at least 1 day.')
                    continue

            while_condition = False

    def get_ad(self):
        return f'''Private Ad -------------------\n{self.__main_text}\nActual until: {self.__until_date}, {self.__days_left} days left\n------------------------------\n\n'''


class LaLiga(File):
    
    def __init__(self):
        
        # create soccer object with API, to get info about spain football clubs
        soccer_data = SoccerDataAPI()
        
        # get list of dicttionaries with clubs info
        self.__liga_list = soccer_data.la_liga()

        # call method to enter club name
        self.set_club_name()

    def set_club_name(self):
        while_condition = True

        while(while_condition):
            self.__club_name = input(
                'Write the club name from Spain ligue, for example (Barcelona, Elche, Real Madrid): ').upper()

            if not self.__club_name:
                print('You entered an empty string, try again:')
                continue
            
            # get info about entered club by user
            team = [team for team in self.__liga_list if team['team'].upper() == self.__club_name]

            # verify that user club was found in self.__liga_list
            if len(team) == 0:
                print('Club was not find, try again: ')
                continue

            self.__team_info = team[0]
            while_condition = False

    def get_club_results(self):
        return f"La Liga result ---------------\nClub name: {self.__team_info['team']}\n{self.__team_info['pos']} position in championat with {self.__team_info['points']} points\n------------------------------\n\n"


class Menu():

    def run_menu(self):
        while_condition = True

        while(while_condition):

            chosen_number = input(
                'Choose the number of operation:\n1 - Add news\n2 - Add Ad\n3 - Add LaLiga club result\n4 - Exit\n:')

            if chosen_number not in ['1', '2', '3', '4']:
                system('cls')
                print('Choose the right number of operation, try again.')
                continue

            match chosen_number:
                case '1':
                    news_object = News()
                    news_object.write_data(news_object.get_news())
                    print('News was added.\n')

                case '2':
                    ad_object = Ad()
                    ad_object.write_data(ad_object.get_ad())
                    print('Ad was added.\n')

                case '3':
                    liga_object = LaLiga()
                    liga_object.write_data(liga_object.get_club_results())
                    print('Club result was added.\n')

                case '4':
                    break


def main():
    menu = Menu()
    menu.run_menu()


if __name__ == "__main__":
    main()