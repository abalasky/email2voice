
from text2speech import run

def main():

    with open("email_clean.txt") as file:
        data = file.read().replace('\n', '')

    with open('validate.txt', 'w+') as file:
        file.write(data)
        file.close()

    data_limit = data[0:5000]
    run(data_limit)


if __name__ == "__main__":
    main()
