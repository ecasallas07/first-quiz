package org.velezreyes.quiz.question6;


public class VendingMachineImpl implements VendingMachine {

  private int quarters = 0;

    @Override
    public void insertQuarter() {
        quarters++;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        switch (name) {
            case "ScottCola":
                if (quarters >= 3) {
                    quarters -= 3;
                    return new Drink("ScottCola", true);
                } else {
                    throw new NotEnoughMoneyException();
                }
            case "KarenTea":
                if (quarters >= 4) {
                    quarters -= 4;
                    return new Drink("KarenTea", false);
                } else {
                    throw new NotEnoughMoneyException();
                }
            default:
                throw new UnknownDrinkException();
        }
    }

    public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }
}
