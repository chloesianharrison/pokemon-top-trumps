import requests
import random
def play_pokemon():
        my_id = random.randint(1, 1001)
        url = f"https://pokeapi.co/api/v2/pokemon/{my_id}"
        response = requests.get(url)
        data = response.json()
        return {
            'name': data['name'],
            'id': data['id'],
            'height': data['height'],
            'weight': data['weight'],
            'base_experience': data['base_experience'],
        }

user_pokemon = play_pokemon()
computer_pokemon = play_pokemon()

def your_pokemon():
    print(f"Your pokemon is: {user_pokemon['name']}")
    print(f"id: {user_pokemon['id']}")
    print(f"height: {user_pokemon['height']}")
    print(f"weight: {user_pokemon['weight']}")
    print(f"base_experience: {user_pokemon['base_experience']}")


your_pokemon()

user_choice = input("Which stat would you like to choose? Enter id/weight/height/base_experience: ").lower()

print(f"Opponent's pokemon is {computer_pokemon['name']}")

if user_choice == "id":
        print(f"Your id is {user_pokemon['id']}")
        print(f"Opponent's id is {computer_pokemon['id']}")
elif user_choice == "height":
        print(f"Your height is {user_pokemon['height']}")
        print(f"Opponent's height is {computer_pokemon['height']}")
elif user_choice == "weight":
        print(f"Your weight is {user_pokemon['weight']}")
        print(f"Opponent's weight is {computer_pokemon['weight']}")
elif user_choice == "base_experience":
        print(f"Your XP is {user_pokemon['base_experience']}")
        print(f"Opponent's XP is {computer_pokemon['base_experience']}")
else:
        print("Invalid choice, choose another pokemon.")
        play_pokemon()

my_result = user_pokemon[user_choice]
computer_result = computer_pokemon[user_choice]

if my_result > computer_result:
        print("You win!")
elif computer_result > my_result:
        print("Bad luck, you lose")
else:
        print("Draw")

play_pokemon()