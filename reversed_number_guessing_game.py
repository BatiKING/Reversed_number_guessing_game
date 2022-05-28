def game_loop():
    """Main game loop where user will provide hints to the CPU"""
    print("Think of a number in range 0-1000 and I will guess it in 10 tries max")
    min_num = 0
    max_num = 1001
    player_hint = ''
    guess_count = 1
    while player_hint != 'correct':
        guess = calc_guess(min_num, max_num)
        print(f"My guess is: {guess}")
        player_hint = input("Tell me if the number was 'too big', 'too small' or 'correct': ")
        if player_hint == 'correct':
            print(f"I win! I guessed it in {guess_count} tries.")
        elif player_hint == 'too big':
            guess_count += 1
            max_num = guess
            continue
        elif player_hint == 'too small':
            guess_count += 1
            min_num = guess
            continue
        else:
            print("Don't cheat!")


def calc_guess(min_arg, max_arg):
    """Calculating next CPU guess"""
    return int((max_arg - min_arg) / 2) + min_arg


game_loop()
