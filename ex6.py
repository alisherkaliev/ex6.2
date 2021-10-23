"""1"""
def convert_distance(miles):
  km = miles * 1.6  # approximately 1.6 km in 1 mile
  return km
miles = (55)
km = convert_distance(miles)
print("The distance in kilometers is: " + str(km))
print("The round-trip in kilometers is: " + str(km * 2))

"""2"""
def right_align(hello):
    print(' ' * (70 - len(hello)) + hello)
right_align('Hello')
