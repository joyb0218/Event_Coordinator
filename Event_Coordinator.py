guests = {}

def read_guestlist(file_name):
  text_file = open("guest_list.txt",'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    #Task 1A
    yield guests

g = read_guestlist('guest_list.txt')
for guests in g:
  first_ten = (name for name in guests.keys())
  over_21 = (key for key, value in guests.items() if value >= 21)

# Task 1B
# for i in range(10):
#   print(next(first_ten))

# Task 4 - all guests over 21
# for names in over_21:
#   print(names)

# Task 2
def add_name(name):
    with open("guest_list.txt", "+r") as file:
        for line in file:
            if name in line:
                break
        else:
            if name is not None:
                g.send(file.write('\n' + str(name)))

new_guest = add_name("Jane,35")
# Task 3 - to all names, even new name added -
# for names in guests.keys():
#   print(names)

# Task 5
def chicken_table():
    first_set = [name for name in guests.keys()]
    for name, seat in zip(first_set[0:5], range(1, 6)):
        yield name, ("Chicken", "Table 1", seat)

def beef_table():
    second_set = [name for name in guests.keys()]
    for name, seat in zip(second_set[6:11], range(1, 6)):
        yield name, ("Beef", "Table 2", seat)

def fish_table():
    last_set = [name for name in guests.keys()]
    for name, seat in zip(last_set[12:], range(1, 6)):
        yield name, ("Fish", "Table 3", seat)

def seating_arrangement_gen():
    yield from chicken_table()
    yield from beef_table()
    yield from fish_table()

# Task 6
# seating_generator = seating_arrangement_gen()
# for seats in seating_generator:
#   print(seats)