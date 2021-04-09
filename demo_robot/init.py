import csv

def main():
    with open('./memory.csv','w') as memory:
        fieldnames = ['UserName','Age','LikingRestaurant','TimeMikeUserName']
        writer = csv.DictWriter(memory, fieldnames=fieldnames)
        writer.writeheader()
    with open('./ranking.csv','w') as ranking:
        fieldnames = ['RestaurantName','Count','SumAge','AgeAverage']
        writer = csv.DictWriter(ranking, fieldnames=fieldnames)
        writer.writeheader()

if __name__ == '__main__':
    main()