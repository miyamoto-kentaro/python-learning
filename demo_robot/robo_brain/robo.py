import csv
import datetime


class Robo(object):
    def __init__(self):
        self.what_your_name()
        self.how_old_are_you()
        self.what_do_you_like_kind_of_restaurant()

    def what_your_name(self):
        print('Hi','What your name?')
        self.username = input('your name:')
        print('Nice to meet you {name}.'.format(name=self.username))

    def how_old_are_you(self):
        print('How old are you?')
        self.userage = input('your age:')
        print('Ok {age} years old'.format(age=self.userage))

    def what_do_you_like_kind_of_restaurant(self):
        print('what_do_you_like_kind_of_restaurant')
        self.restaurantname = input('restaurant:').capitalize()
        print('Thank you {}.'.format(self.username),'Have a good day.')

    def recommend_some_restaurant(self):
        print('#######')
    
    def __del__(self):
        with open('./memory.csv','a') as memory:
            writer = csv.writer(memory)
            writer.writerow([self.username,self.userage,self.restaurantname,datetime.datetime.now()])

        with open('./memory.csv','r') as memory:
            data = csv.DictReader(memory)
        
        with open('./ranking.csv','w') as ranking:
            fieldnames = ['RestaurantName','Count','SumAge','AgeAverage']
            writer = csv.DictWriter(ranking, fieldnames=fieldnames)
            writer.writeheader()
            


if __name__ == "__main__":
    robo = Robo()