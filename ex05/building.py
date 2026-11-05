import sys
import string

def main():
    try:
        if len(sys.argv) != 2:
            return
        text = sys.argv[1]
        print(f"The text contains {len(text)} characters:")
        print(f"{sum(c.isupper() for c in text)} upper letters")
        print(f"{sum(c.islower() for c in text)} lower letters")
        print(f"{sum(c in string.punctuation for c in text)} punctuation marks")
        print(f"{sum(c.isspace() for c in text)} spaces")
        print(f"{sum(c.isdigit() for c in text)} digits")
    except AssertionError as e:
        print(e)
if __name__ == "__main__":
    main()