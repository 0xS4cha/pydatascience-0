import sys

def main():
    try: 
        if len(sys.argv) == 2:
            age = None
            try:
                age = int(sys.argv[1])
            except Exception:
                raise AssertionError("argument is not an integer")
            if age != None and age % 2:
                print("I'm Odd.")
            else:
                print("I'm Even.")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()