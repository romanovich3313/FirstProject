base_rate = 40
price_per_km = 10
total_trip = 0
path = 0

def trip_price(path):



    def totaltrip():   
        global total_trip
        int(total_trip) 
        total_trip +=1
        return total_trip
    
    total = totaltrip()
    price = (path*price_per_km) + base_rate
    return f"price taxi{price} total trip: {total}"

print(trip_price(100))
print(trip_price(50))
print(trip_price(10))
