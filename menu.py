def menu(options):
    while True:
        user_choice = input(f'Choose from {options}: ').strip()
    
        if user_choice in options:   # did they choose something valid?
            return user_choice

        print(f'{user_choice} is invalid; try again!')

pick = menu(['a', 'b', 'c'])

print(f'You picked {pick}!')
