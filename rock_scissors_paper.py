import random

def human_vs_computer(player_choice=None):

	choices = ['rock', 'scissors', 'paper']

	computer = random.choice(choices)

	print("Computer's choice was", computer)

	if comparison(player_choice, computer) == 1:
		print('You wins')
	elif comparison(player_choice, computer) == 2:
		print('You loses')
	else:
		print('Draw')


def comparison(player_1_choice=None, player_2_choice=None):
	hands = {player_1_choice: 1, player_2_choice: 2}

	if player_1_choice != player_2_choice:
		if [player_1_choice, player_2_choice] in [['rock', 'scissors'], ['scissors', 'rock']]:
			return hands['rock']
		elif [player_1_choice, player_2_choice] in [['scissors', 'paper'], ['paper', 'scissors']]:
			return hands['scissors']
		elif [player_1_choice, player_2_choice] in [['rock', 'paper'], ['paper', 'rock']]:
			return hands['paper']
	else:
		return 0


def solve():
	input_shortcuts =  {
		'rock': ['r', 'rock', 'R', 'ROCK', 'Rock', ],
		'scissors': ['s', 'scissors', 'S', 'SCISSORS', 'Scissors', ],
		'paper': ['p', 'paper', 'P', 'PAPER', 'Paper', ],
	}

	while True: 
		input_choice = input('Pick your choice rock/scissors/paper (r/s/p)?')

		for choice, shortcuts in input_shortcuts.items():
			if input_choice in shortcuts:
				player_choice = choice
				break
			else:
				player_choice = ''

		if player_choice:
			human_vs_computer(player_choice)

			keep_playing = input('\n Continue to play? Yes/No (y/n)')

			if keep_playing in ['y', 'yes', 'Y', 'YES', 'Yes']:
				continue
			else:
				print('Game Over')
				break
		else:
			continue


def main():
	try:
		solve()
	except KeyboardInterrupt:
		print('Process Killed')


if __name__ == '__main__':
	main()