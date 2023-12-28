print(r'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  _.--.
              _.-'_:-'||
          _.-'_.-::::'||
     _.-:'_.-::::::'  ||
   .'`-.-:::::::'     ||
  /.'`;|:::::::'      ||_
 ||   ||::::::'     _.;._'-._
 ||   ||:::::'  _.-!oo @.!-._'-.
 \'.  ||:::::.-!()oo @!()@.-'_.|
  '.'-;|:.-'.&$@.& ()$%-'o.'\U||
    `>'-.!@%()@'@_%-'_.-o _.|'||
     ||-._'-.@.-'_.-' _.-o  |'||
     ||=[ '-._.-\U/.-'    o |'||
     || '-.]=|| |'|      o  |'||
     ||      || |'|        _| ';
     ||      || |'|    _.-'_.-'
     |'-._   || |'|_.-'_.-'
     '-._'-.|| |' `_.-'
          '-.||_/.-'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----Welcome to Treasure Island-----
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Your mission is to find the treasure and have fun!")

choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "l" for left or "r" for right: \n').lower()

if choice1 == "l":
    choice2 = input(
        'You\'re at a lake with an island in the middle. '
        'Type "w" to wait for a boat or "s" to swim across: \n').lower()
    if choice2 == "w":
        choice3 = input(
            "You arrive at the island unharmed. "
            "There is a house with 3 doors. One red, one yellow and one blue. "
            "Type a door color to enter: \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")
