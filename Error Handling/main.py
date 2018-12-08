try:
    filename = input('Enter file to read content')
    with open(filename) as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print(filename + ' not found')
