seconds_year = 365 * 24 * 3600


def change(population, year):
    birth = seconds_year / 7
    death = seconds_year / 13
    immigrant = seconds_year / 45

    for i in range(year):
        population += birth + immigrant - death 
    return population


year_2 = 5
current_people = 312032487
print("After %d years, the population is %d" % (year_2, change(current_people, year_2)))
