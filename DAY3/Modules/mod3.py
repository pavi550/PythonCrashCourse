# displayMsg prints a message to the name being passed.

def displayMsg(name):
    print("Inside Display Message")
    print("Hi "+name)

# if main function we write the code that is to be executed by the program itself as owner
# and not visible to the other modules/program
def main():   # main function -
    if __name__ == '__main__':
        print("This is the mod1 program")
        print(__name__)
        displayMsg('Gautam')

        def hello():
            print("method from main program..")

        hello()
main()