# Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
# Copyright (c) 2021 Edgar Barrera

def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
