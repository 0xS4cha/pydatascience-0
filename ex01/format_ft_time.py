import datetime as dt
from decimal import Decimal

def main():
    date = dt.datetime.now().timestamp()
    print(f"Seconds since January 1, 1970: {date} or {'%.2E' %Decimal(date)} in scientific notation")
    print(dt.datetime.now().strftime("%b %d %Y"))

if __name__ == "__main__":
    main()
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$