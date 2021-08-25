#!/usr/bin/python3

print("""
         .    _.----~~~~~~~7
             /              ~-..-~~--..--.
       .'.'.'                             `.
         .~                                 \
       .'                                    `.
   .   (                                       \
 '.    )                                        `.
   '  (                                           ~-.
       \                                             ~-~~7
        `.       __.._                                  .'
          ~-.--~~     ~--.                             /
                         ;                          .-~
                         (                        .~
                          `.                    .'
                            ;                   ;
                            `.                  `       _
                             )                   )     / )
                            (                 _.-'  .-' .'
                            `.               (      )   /
                              7             _;      < _/
                               \           /         ~
                                \         /
                                 `. __..-'
                                   ~


""")

print ("Welcome to Tresure Continent.")
print ("Your mission is to find the treasrue.")

choice = input ("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if (choice == 'left'):
	choice = input ("You come to lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boot. Type \"swim\" to swim across.\n")
	if (choice == 'wait'):
		choice = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?\n")
		if (choice == 'red'):
			print ("Burned by fire. Game Over!!!")
		elif (choice == 'Blue'):
			print ("Eaten by beats. Game Over!!!")
		elif (choice == 'Yellow'):
			print ("You Win!!!")
		else:
			print("Game Over")
else:
	print("You Fail into a hole. Game Over!!!")

