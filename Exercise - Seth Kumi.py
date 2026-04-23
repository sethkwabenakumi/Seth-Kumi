#*Section 1: Lists (Methods & Slicing)*

#Q1
market_list =["Yam", "Tomato", "Onion"]
market_list.append("Fish")
print(market_list)

#Q2
Given_grades = [80, 90, 70]
Given_grades.insert(1,83)
print(Given_grades)

#Q3
gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
print(gadgets[0:3])

#Q4
list_colors = ["Red", "Blue", "Green"]
list_colors.clear()
print(list_colors)

#Q5
list_votes = ["Yes", "No", "Yes", "Yes", "No"]
list_votes= list_votes.count("Yes")
print(list_votes)

#Q6
list_alphabets = ["a", "b", "c", "d", "e", "f"]
print(list_alphabets[2:5])

#Q7
order_of_students = ["Kofi", "Ama", "Yaw"]
order_of_students.reverse()
print(order_of_students)

#Q8
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)

#Q9
Given_cities = ["Accra", "Kumasi", "Tamale"]
Given_cities.remove(Given_cities[2])
Given_cities.insert(2,"removed_city")
print(Given_cities)

#Q10
list_items = ["Pen", "Ruler", "Eraser"]
index =list_items.index("Ruler")
print(index)

#*Section 2: Tuples & Data Types*

#Q1
#student_info = ("Araba", 20)
#update                              #commented this for the rest of the code to run.
#student_info[1] = 21
#print(student_info) 

#Q2
tup = (1, 2, 3)
tup_list = list(tup)
tup_list.append(4)
tup = tuple(tup_list)
print(tup)

#Q3
Given_data = (10, 20, 10, 30, 10)
Given_data= Given_data.count(10)
print(Given_data)

#Q4
tuples_colors = ("Red", "Blue", "Green")
Blue_index = tuples_colors.index("Blue")
print(Blue_index)

#Q5
tuple_coords = (5.6, -0.1)
lat, lon = tuple_coords
print("Latitude:", lat)
print("Longitude:", lon)

#Q6
nest_list = []
nest_list.append((5, 10))
print(len(nest_list))

#Q7
Given_numbers = (10, 20, 30, 40, 50)
last_two = Given_numbers[-2:]
print(last_two)

#Q8
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list)

#Q9
#my_tup = (4, 8, 2)
#del my_tup                   #commented this for the rest of the code to run.
#print(my_tup)

#10
x = (5)
y = (5,)               
print(type(x))
print(type(y))