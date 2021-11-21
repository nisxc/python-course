MILE_TO_METRE = 1609.344
GALLON_TO_LITRE = 3.785411784


def liters_100km_to_miles_gallon(value):
    return (((100 * 1000)/MILE_TO_METRE)/(value/GALLON_TO_LITRE))


def miles_gallon_to_liters_100km(value):
    return ((100 * 1000) * GALLON_TO_LITRE) / (value * MILE_TO_METRE)


print(liters_100km_to_miles_gallon(3.9))
print(miles_gallon_to_liters_100km(23.5))
