
from text2speech import run

def main():

    with open("fortune.txt") as file:
        data = file.read().replace('\n', '')

    print(type(data))
    print(data)
    run(data)

if __name__ == "__main__":
    main()
