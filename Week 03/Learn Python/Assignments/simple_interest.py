if __name__ == "__main__":
    amount = int(input("Enter Amount: "))
    interest_rate = int(input("Enter Interest Rate: "))
    duration = int(input("Enter duration(in years): "))
    simple_interest = (amount*duration*interest_rate)/100
    print(f"Simple interest is {simple_interest}")
