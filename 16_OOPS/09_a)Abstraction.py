# ABSTRACTION:
# Hinding Implementation (unnecessary) details and showing necessary information to the user.

from abc import ABC,abstractmethod #(abstract Base Class)

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

# Method Implementation shown below 
class SBI(ATM):
    def withdraw(self):                     # Example 
        server = "SBI Core Banking Server"  # These are details how and what are used inside.
        language = "JAVA B"
        database = "OracleDB"

    print("Cash withdrawn successful.")

    def check_balance(self):
        server = "SBI Core Banking Server"
        language = "JAVA B"
        database = "OracleDB"

    print(f"Current Balance:{100000}")

sbi = SBI()
sbi.withdraw()
sbi.check_balance()