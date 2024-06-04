PLAYER_NAME_KEY = 'player_name'
TEAM_NAME_KEY = 'team_name'
GOAL_TIME_KEY = 'goal_time'

def read_file(filepath):
    with open(filepath) as file:
        return file.read()

def line_to_goal(line):
    goal_data = line[:-1].split(';')
    goal = dict()
    goal[PLAYER_NAME_KEY] = goal_data[0]
    goal[TEAM_NAME_KEY] = goal_data[1]
    goal[GOAL_TIME_KEY] = int(goal_data[2])

    return goal

def text_to_goals(text):
    return [line_to_goal(line) for line in text.split('\n')]

def find_goals_by_condition(goals, condition):
    return list(filter(condition, goals))

def find_goals_by_value(goals, key, value):
    return find_goals_by_condition(goals, lambda goal: goal[key] == value)

def find_scoring_players_by_team(goals, team_name):
    goals_of_team = find_goals_by_value(goals, TEAM_NAME_KEY, team_name)

    return list(set(goal[PLAYER_NAME_KEY] for goal in goals_of_team))


def main():
    AMOUNT_OF_GOALS_OF_TEAM = '1'
    AMOUNT_OF_GOALS_OF_PLAYER = '2'
    SCORING_PLAYERS_OF_TEAM = '3'
    AMOUNT_OF_GOALS_IN_COMPETITION = '4'
    AMOUNT_OF_GOALS_IN_FIRST_HALF = '5'
    AMOUNT_OF_GOALS_IN_SECOND_HALF = '6'
    AMOUNT_OF_GOALS_IN_EXTRA_TIME = '7'
    EXIT = '8'

    filepath = './goals.txt'
    goals = text_to_goals(read_file(filepath))
    menu_text = '''Please enter your choise(1-8):
    1. Amount of goals scored by a team
    2. Amount of goals scored by a player
    3. All scoring players of a team
    4. Amount of goals scored in the competition
    5. Amount of goals scored during the first half
    6. Amount of goals scored during the second half
    7. Amount of goals scored during extra time
    8. Exit\n'''

    option = input(menu_text)
    while option != EXIT:
        if option == AMOUNT_OF_GOALS_OF_TEAM:
            team_name = input('Enter the name of the team: ')
            print('{} scored {} goals'.format(
                team_name, 
                len(find_goals_by_value(goals, TEAM_NAME_KEY, team_name))
            ))
        elif option == AMOUNT_OF_GOALS_OF_PLAYER:
            player_name = input('Enter the name of the player: ')
            print('{} scored {} goals'.format(
                player_name, 
                len(find_goals_by_value(goals, PLAYER_NAME_KEY, player_name))
            ))
        elif option == SCORING_PLAYERS_OF_TEAM:
            team_name = input('Enter the name of the team: ')
            scoring_players = find_scoring_players_by_team(goals, team_name)
            if len(scoring_players) == 0:
                print('There are no scoring players in {}'.format(team_name))
            else:
                print('Scoring players of {}:\n{}'.format(
                    team_name, 
                    '\n'.join(scoring_players)
                ))
        elif option == AMOUNT_OF_GOALS_IN_COMPETITION:
            print('{} goals were scored during the competition'.format(len(goals)))
        elif option == AMOUNT_OF_GOALS_IN_FIRST_HALF:
            print('{} goals were scored during the first half'.format(
                len(find_goals_by_condition(goals, lambda goal: goal[GOAL_TIME_KEY] <= 45)))
            )
        elif option == AMOUNT_OF_GOALS_IN_SECOND_HALF:
            print('{} goals were scored during the second half'.format(
                len(find_goals_by_condition(
                    goals, 
                    lambda goal: goal[GOAL_TIME_KEY] > 45 and goal[GOAL_TIME_KEY] <= 90)))
            )
        elif option == AMOUNT_OF_GOALS_IN_EXTRA_TIME:
            print('{} goals were scored during extra time'.format(
                len(find_goals_by_condition(goals, lambda goal: goal[GOAL_TIME_KEY] > 90)))
            )
        elif option != EXIT:
            print('Invalid input, please try again.')


        if option != EXIT:
            option = input(menu_text)

main()