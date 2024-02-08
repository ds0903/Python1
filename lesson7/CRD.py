# CRUD (Create Read Update Delete) operations

# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]

def player_update(players: list[dict]):
    fin_num=input('enter player number ')
    for player in players:
        if player['number'] == int(fin_num):
            new_number = input('Enter the new number for the player: ')
            new_name = input('Enter the new name for the player: ')
            new_age = input('Enter the new age for the player: ')
            player['name'] = (new_name)
            player['age'] = (new_age)
            player['number'] = (new_number)
            print(f"Player {fin_num} updated with new number {new_number} name {new_name} and new age {new_age}")
            main()
    else:
        print(f"No player found with number {fin_num}")


# Application source code
def repr_players(players: list[dict]):
    for player in players:
        print(f"\t[Player {player['number']}]: {player['name']},{player['age']}")


def player_add(name: str, age: int, number: int) -> dict:
    player: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    

    if not any (p ['number'] == number for p in team): 
        team.append(player)
        return player
    else:
        raise 'this player alredy in team!'


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            del player


def main():
    operations = ("add", "del", "repr", "exit", "up")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "up":
            player_update(team)

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input("Enter new player information[name,age,number]: ")
            # Input: 'Clark,19,22'
            user_items: list[str] = user_data.split(",")
            # Result: ['Clark', '19', '22']
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
        else:
            raise NotImplementedError


#if __name__ == "__main__":
main()
