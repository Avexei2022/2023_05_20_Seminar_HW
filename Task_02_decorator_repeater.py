def repeater(greeting):
    def our_repeater(func):
        def decorator():
            count = func()
            for i in range(1, count + 1):
                print(f'{greeting} - {i}!')
        return decorator
    return our_repeater


@repeater('Ты лучший')
def get_num_to_repeat():
    return int(input('Сколько тебе лет?\n'))


get_num_to_repeat()
