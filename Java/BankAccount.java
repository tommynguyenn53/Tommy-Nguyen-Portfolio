public class BankAccount {
    int accountNumber;
    int bsb;
    double balance;
    double interestRate;
    double depositAmount;

    public BankAccount(int accountNumber, int bsb, double balance, double interestRate) {
        this.accountNumber = accountNumber;
        this.bsb = bsb;
        this.balance = balance;
        this.interestRate = interestRate;
        this.depositAmount = 0;
    }


    public double increaseInterestRate() {
        balance += balance *(interestRate / 100);
        return balance;
    }

    public double deposit(double cash) {
        balance += cash;
        depositAmount += cash;
        return balance;
    }

    public double withdraw(double cash) {
        balance -= cash;
        return balance;
    }

    public void applyTransaction(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }

    public double getDepositAmount() {
        return depositAmount;
    }
}