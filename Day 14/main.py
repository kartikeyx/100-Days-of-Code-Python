import random
import game_data
import art

a = random.choice(game_data.data)
b = random.choice(game_data.data)
print(f"Compare A: {game_data.data[a]["name"]}, a {game_data.data[a]["description"]}, from {game_data.data[a]["country"]}")
print(art.vs)
print(f"Against B: {game_data.data[b]["name"]}, a {game_data.data[b]["description"]}, from {game_data.data[b]["country"]}")