def me(city):
    if city == "Dushanbe":
        print(city + " population is 1M")
    if city == "Khorog":
        print(city + " population is 300K")
    if city == "Khujand":
        print(city + " population is 600K")
    if city == "":
        print("You didn't write any city name!")

me("Dushanbe")  
me("Khujand")  
me("Khorog")
me("")    