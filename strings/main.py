# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_1 + ' ' + str(goal_0) + ', ' + scorer_2 + ' ' + str(goal_1)
print(scorers)
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
print(report)

player = 'Frank Rijkaard'
split_name = player.find(' ')
first_name = player[:split_name]
last_name = player[split_name + 1:]
first_letter = player[0]
name_short = f'{first_letter}. {last_name}'
last_name_len = len(last_name)
chant = (f'{first_name}! ') * len(first_name)
chant = chant[0:len(chant)-1]
last_character = chant[-1]
good_chant = last_character != ' '
