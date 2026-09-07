def divide_numbers(a: str, b: str) -> None:
    try:
        int1=int(a)
        int2=int(b)
        res=int1/int2
        print(res)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occurred:",error)

        



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
