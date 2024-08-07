class Not_Allowed(Exception):
      def __init__(self,data):
            self.data = data


try:
      num1 = int(input("Enter the value for age"))
      if (num1 < 20 or num1 > 30):
            raise Not_Allowed("Age is not valid..")
      else:
            print("You are welcome to Python")


except ZeroDivisionError as e:
      print("The number cannot be divided..: \n",e)
except Not_Allowed as e:
      print("Exception :",e)
else:
      print("Try completed successfully...")
finally:
      print("Inside finally block")

