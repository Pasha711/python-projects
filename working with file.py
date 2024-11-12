import os

# Input file name and existing check
file_exists = False
while not file_exists:
    file_path = input('Enter file name > ')
    if os.path.isfile(file_path):
        file_exists = True
    else:
        print('Enter correct filename!')
print('File ' + file_path + ' exists!')

# Input open mode - text or binary
mode = 'n'
while mode not in ['b', 't']:
    mode = input('Enter mode to read file(t or b) >')

try:
    # If text open mode
    if mode == 't':
        with open(file_path, "rt") as file:
            print('Open file in TEXT mode...')
            print('Lines in file:', file.read().count('\n') + 1)
    # If binary open mode
    else:
        i = 0
        with open(file_path, "rb") as file:
            print('Open file in BINARY mode...')
            for line in file:
                i += 1
            print('Lines in file:', i + 1)

except IOError as e:
    print('Error opening file', file_path)
    print(e)

file.close()
