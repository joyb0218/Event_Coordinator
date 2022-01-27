# Event_Coordinator
Codecademy's intermediate Python project called Event Coordinator that utilizes generators (yield, send, multiple and pipeline).

Create a Python application using generators to help manage this event.

Task 1: You’ve been provided a guestlist of names and their ages that are within the file guest_list.txt. Within the file script.py, there is a defined function called read_guestlist() that will read in the guestlist file line by line. This function will separate the name and age values and store them into variables named name and age respectively. Modify this function to be a generator function that will yield each read line so that each guest name is yielded each time for the generator. Using a for loop, iterate through the generator object that is retrieved by calling the generator function read_guestlist() and print out the first 10 guests on the guestlist.

Task 2: Add a guest with the information: “Jane,35”. Use one of the three generator methods we have learned to accomplish this (use the send method).

Task 3: Yield the rest of the names on the guestlist file to our generator by adding numerous next() calls on the generator object until a StopIteration exception is reached. This can also be accomplished by using a for loop on the generator object to automatically make the appropriate amount of next() calls (I used a for loop).

Task 4: Define a generator expression that will use the guests dictionary to retrieve a generator of names of all guests over 21 years of age. We should see our newly added guest, Jane on this list.

Task 5: Assign meals to 3 tables with 5 seats at each tables. Create 3 separate generator functions, one for each table, that will yield tuples of (“Food Name”, “Table X”, “Seat Y”) for each of the 5 seats at each table. You may use the following foods for the tables: Chicken, Beef, Fish.

Task 6: Assign a table and seat number with meal selection to each guest. Create another generator function that will take in as input our guests dictionary and the connected generator seating/food selection we created in the previous step. This function should yield a tuple of the guest name and the next value from the connected generator.
