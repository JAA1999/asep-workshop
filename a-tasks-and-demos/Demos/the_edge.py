# This is not a good example (more appropriate for a statically typed language)
class EightLetterWord:
    word = ['','','','','','','','']

    def __init__(self, word) -> None:
        for i in range(len(word)):
            self.word[i] = word[i]


def get_username():
    user_input = input('Enter first name: ')
    name = EightLetterWord(user_input)
    return name


def check_user(username):
    if username == 'Dave':
        print('Logged in :D')
    else:
        print(f'{username} is not the right name')


def main():
    try:
        user = get_username()
        check_user(''.join(user.word).strip())
    except Exception:
        print('Oh no something went wrong')


main()