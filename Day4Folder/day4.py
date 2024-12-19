# counter = 0
# while counter < 10:
#     print (counter)
#     counter = counter + 1

# counter = 5
# while counter < 33:
#     print (counter)
#     counter = counter + 1

# counter = 50
# while counter > 1:
#     print (counter)
#     counter = counter - 1

corr_ans = ("It has no guts to do it")
per_ans = ("random")
counter = 0
per_ans = input("Why does the skeleton not want to cross the road?")
while corr_ans != per_ans:
    print ("SKILL ISSUE!")
    per_ans = input("Why does the skeleton not want to cross the road?")
    print ("Hint 1, What does the skeleton not have?")
    counter + 1
    if counter == 2:
        print ("SKILL ISSUE!")
        per_ans = input("Why does the skeleton not want to cross the road?")
        print ("Hint 2, It is at the lower part of the body.")
        if counter == 3:
            print ("SKILL ISSUE!")
            per_ans = input("Why does the skeleton not want to cross the road?")
            print ("Hint 3, It is about courage.")
            if counter == 4:
                print ("The answer is that it has no guts to do it.")