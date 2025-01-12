nights_spend = int(input("Enter for how many nights u want to spend..."))
def hotel_rent(nights_spend):
    return 5000*nights_spend
print(hotel_rent(nights_spend))


car_rent_time = int(input("Enter for how many days u want take the rental car"))
def car_rent(car_rent_time):
    if car_rent_time >= 10:
        return 100*car_rent_time
    elif car_rent_time >= 5:
        return 200*car_rent_time
    else:
        return 500*car_rent_time



print(car_rent(car_rent_time),(hotel_rent(nights_spend)))