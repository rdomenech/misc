import sys
import time


def main(option, percentage):
    inc = 0
    while inc <= percentage:
        progress(inc, option, percentage)
        time.sleep(0.1)
        inc += 1

    sys.stdout.write("\n")


def progress(count, option, percentage):

    filled_len = int(percentage * count / float(percentage))

    percents = round(percentage * count / float(percentage), 1)
    bar = option * filled_len + '-' * (percentage - filled_len)

    sys.stdout.write('[{}] {}% \r'.format(bar, percents))

    sys.stdout.flush()


if __name__ == ('__main__'):

    sys.stdout.write('\n***************************************\n')
    sys.stdout.write('* Welcome to the progress bar display *\n')
    sys.stdout.write('***************************************\n')

    is_wrong_option = True
    while is_wrong_option:
        sys.stdout.write('Choose the kind of progress bar you want to display'
                         ' =, ^ or #:\n')
        option = sys.stdin.readline().strip()

        if option not in ['=', '^', '#']:
            sys.stdout.write("You've chosen an invalid option.\n")
        else:
            is_wrong_option = False

    is_not_number = True
    while is_not_number:
        sys.stdout.write('Type the percentage you want to display:\n')

        try:
            percentage = int(sys.stdin.readline().strip())
            is_not_number = False
        except ValueError:
            sys.stdout.write('This number is incorrect.\n')

    main(option, percentage)
