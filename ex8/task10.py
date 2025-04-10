import json

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def search_player(data, name):
    for player in data:
        if player['name'] == name:
            print(format_player_info(player))
            return
    print("Player not found.")

def list_teams(data):
    teams = sorted(list(set(player['team'] for player in data)))
    for team in teams:
        print(team)

def list_countries(data):

    countries = sorted(list(set(player['nationality'] for player in data)))
    for country in countries:
        print(country)

def list_players_in_team(data, team):

    players = sorted(
        [player for player in data if player['team'] == team],
        key=lambda p: (p['goals'] + p['assists']),
        reverse=True
    )
    for player in players:
        print(format_player_info(player))

def list_players_from_country(data, country):
    players = sorted(
        [player for player in data if player['nationality'] == country],
        key=lambda p: (p['goals'] + p['assists']),
        reverse=True
    )
    for player in players:
        print(format_player_info(player))

def list_most_points(data, n):
    players = sorted(
        data,
        key=lambda p: (p['goals'] + p['assists'], p['goals']),
        reverse=True
    )[:n]
    for player in players:
        print(format_player_info(player))

def list_most_goals(data, n):

    players = sorted(
        data,
        key=lambda p: (p['goals'], -p['games']),
        reverse=True
    )[:n]
    for player in players:
        print(format_player_info(player))

def format_player_info(player):
    """
    Formats player information into a consistent string.

    Args:
        player (dict): A dictionary containing player information.

    Returns:
        str: A formatted string with player details.
    """
    name = player['name']
    team = player['team']
    goals = player['goals']
    assists = player['assists']
    points = goals + assists
    return f"{name:<20} {team:>3} {goals:>2}+{assists:>2}={points:>3}"

def main():
    """
    Main function to run the hockey statistics application.ẽ
    """

    filename = input("file name: ")  # Prompt for filename
    try:
        data = load_data(filename)
        print(f"read the data of {len(data)} players")  # Indicate data load success
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'")
        return

    while True:
        print("\ncommands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

        command = input("command: ")

        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            search_player(data, name)
        elif command == "2":
            list_teams(data)
        elif command == "3":
            list_countries(data)
        elif command == "4":
            team = input("team: ")
            list_players_in_team(data, team)
        elif command == "5":
            country = input("country: ")
            list_players_from_country(data, country)
        elif command == "6":
            try:
                n = int(input("how many: "))
                list_most_points(data, n)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "7":
            try:
                n = int(input("how many: "))
                list_most_goals(data, n)
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()