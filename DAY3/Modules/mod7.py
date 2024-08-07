# displayMsg prints a message to the name being passed.
import mod6
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
        import mod6    #inside if block
        print("Just imported Mod3 in main function...")
        print("Calling function from mod3")
        mod6.Mod()
        print("Back from mod3 to main function")
    print("Calling Mod function from main function block")
    mod6.Mod()
main()
print("Calling the mod3 from default main...")
mod6.Mod()
