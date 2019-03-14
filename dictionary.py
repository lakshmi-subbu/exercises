# program for Dictionaries
playerdict1 = {
   "name":"kartik",
   "numbers":{23,22,47,89,5}
}
playerdict2 = {
   "name":"vishak",
   "numbers":{13,22,47,8,5}
}
lottery_numbers = set()
lottery_numbers.add(13)
lottery_numbers.add(21)
lottery_numbers.add(22)
lottery_numbers.add(5)
lottery_numbers.add(8)
print (lottery_numbers)
participants_list =[playerdict1,playerdict2]
print(type(playerdict1))
print(type(playerdict2))
print ("Congrats "+participants_list[0]["name"]+"!")
print ("You have won")
print(len(lottery_numbers.intersection(participants_list[0]["numbers"])))
print ("Congrats "+participants_list[1]["name"]+"!")
print ("You have won ")
print(len(lottery_numbers.intersection(participants_list[1]["numbers"])))
#for x in participants_list:
#    print(participants_list[x]["name"])
#    print(len(lottery_numbers.intersection(participants_list[0]["numbers"])))
    