class ATM:
    def __init__(self, pin: str, balance: float = 1000.0):
        self.pin = pin
        self.balance = balance
        self.is_authenticated = False

    def authenticate(self, max_attempts: int = 3) -> bool:
        attempts = 0
        while attempts < max_attempts:
            entered_pin = input("Enter your 4-digit PIN: ").strip()
            if entered_pin == self.pin:
                print("\nPIN accepted. Welcome!\n")
                self.is_authenticated = True
                return True
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
            else:
                print("\nToo many incorrect attempts. Your card is locked.")
        return False

    def check_balance(self) -> None:
        print(f"\nCurrent Balance: R{self.balance:,.2f}")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("\nDeposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"\nDeposited R{amount:,.2f}. New Balance: R{self.balance:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("\nWithdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("\nInsufficient funds.")
        else:
            self.balance -= amount
            print(f"\nPlease take your cash: R{amount:,.2f}")
            print(f"Remaining Balance: R{self.balance:,.2f}")

    def run(self) -> None:
        if not self.authenticate():
            return

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self._handle_amount_action("deposit")
            elif choice == "3":
                self._handle_amount_action("withdraw")
            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("\nInvalid selection. Please choose 1, 2, 3, or 4.")

    def _handle_amount_action(self, action: str) -> None:
        raw_amount = input(f"Enter amount to {action}: R").strip()
        try:
            amount = float(raw_amount)
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")
            return

        if action == "deposit":
            self.deposit(amount)
        elif action == "withdraw":
            self.withdraw(amount)


if __name__ == "__main__":
    atm = ATM(pin="1612", balance=10000000.00)
    atm.run()