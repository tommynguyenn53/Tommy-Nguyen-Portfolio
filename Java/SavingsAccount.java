public class SavingsAccount extends BankAccount{

    private double bonusInterestRate;

    public SavingsAccount(int accountNumber, int bsb, double balance, double interestRate) {
        super(accountNumber, bsb, balance, interestRate);
        this.bonusInterestRate = bonusInterestRate;
    }

    public void applyBonusInterest(double depositAmount) {
        if (getDepositAmount() > 200) {
            double bonus = balance * (bonusInterestRate / 100);
            balance += bonus;
        }
    }



}
