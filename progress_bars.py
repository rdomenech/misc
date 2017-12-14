import collections
import sys
import time
from multiprocessing import Process as Task, Queue

BARS = ['=', '^', '#']


def bars(status, bar):
    count = 10
    for i in range(count):
        status.put([bar, (i+1.0)/count])
        time.sleep(0.1)


def print_progress(progress, totals):
    sys.stdout.write('\033[2J\033[H')
    for bar, percent in progress.items():
        bar_display = (bar * int(percent * totals[bar])).ljust(totals[bar])
        percent = int(percent * totals[bar])
        sys.stdout.write("[%s] %s%%\n" % (bar_display, percent))
    sys.stdout.flush()


def main(totals):
    """
    It prints n progress bars given a dictionary with n elements with a bar id
     as a key and an integer between 1 and 100 as a value.

    :param totals: dict of progress bar ids and integer values
    :type totals: dict
    """
    for element in totals.values():
        if element > 100 or element < 1:
            sys.stdout.write('One of the elements is too big or smalll.\n')
            sys.exit()

    status = Queue()
    progress = collections.OrderedDict()
    workers = []

    for bar in BARS:
        child = Task(target=bars, args=(status, bar))
        child.start()
        workers.append(child)
        progress[bar] = 0.0

    while any(i.is_alive() for i in workers):
        time.sleep(0.1)
        while not status.empty():
            bar, percent = status.get()
            progress[bar] = percent
            print_progress(progress, totals)


if __name__ == ('__main__'):
    sys.stdout.write('\n***************************************\n')
    sys.stdout.write('* Welcome to the progress bar display *\n')
    sys.stdout.write('***************************************\n')

    totals = {}
    for element in BARS:

        is_not_number = True
        while is_not_number:
            sys.stdout.write(
                'Type the percentage for bar {}:\n'.format(element))

            try:
                totals[element] = int(sys.stdin.readline().strip())
                is_not_number = False
            except ValueError:
                sys.stdout.write('This number is incorrect.\n')

    main(totals)
    sys.stdout.write('All tasks complete!\n')
