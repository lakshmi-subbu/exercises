# Program for sets
nearby_people = {'Saurabh', 'Jen', 'Anna'}
print (nearby_people)
print(type(nearby_people))
user_friends = set()
name = input("Enter a friend's name")
user_friends.add(name)
print (user_friends)
print (user_friends.intersection(nearby_people))
