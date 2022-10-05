from datetime import date

def main():
    # Step 1: Panic!
    print(thirteenth(1, 1985))
    # Step 4: Profit!

def thirteenth(month, year):
    # Step 2: Remember Python has datetime objects
    return str(date(year,month,13).strftime("%A")=='Friday')
    # Step 3: Remind self to always check the documentation

if __name__ == "__main__":
    main()

