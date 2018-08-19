import time
import sys
from collections import namedtuple

Choice = namedtuple('Choice', ('text', 'ref'))
Entry = namedtuple('Entry', ('prompt', 'choices'))


def print_at_speed(text, speed=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()


def process_option(line):
    text, ref = line.split('::')
    return Choice(text=text.strip(), ref=ref.strip())


def update_entries(line, entries):
    ref, prompt = line.split('::')
    entries[ref] = Entry(prompt=prompt.strip(), choices=[])
    return ref


def parse(lines):
    entry = None
    entries = dict()
    for line in lines:
        if line[0] == '#':
            continue

        if not entry:
            entry = update_entries(line, entries)
        elif line == '\n':
            entry = None
        else:
            entries[entry].choices.append(process_option(line))
    return entries


def get_input(entry, prompt='Enter a choice: '):
    raw = input(prompt)
    try:
        return entry.choices[int(raw) - 1].ref
    except IndexError:
        print_at_speed('Please enter a number from %d to %d' %
                       (1, len(entry.choices)), 0.05)
        return get_input(prompt, entry)


def exec_entry(entry):
    print_at_speed(entry.prompt)

    if not entry.choices:
        return None

    for i, choice in enumerate(entry.choices, 1):
        print_at_speed('%d. %s' % (i, choice.text))

    return get_input(entry)


def play(filename, entry_key='start', end_key='end'):
    with open(filename) as f:
        lines = f.readlines()

    entries = parse(lines)
    while entry_key:
        entry_key = exec_entry(entries[entry_key])
        print()
    exec_entry(entries[end_key])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <filename>'.format(sys.argv[0]))
        sys.exit(1)

    play(sys.argv[1])
