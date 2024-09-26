public class Water {
    public abstract class Vessel {
        double litres;
        private double maxLitres;

        public Vessel(double maxLitres) {
            this.maxLitres = maxLitres;
            this.litres = 0;
        }

        public double pour(Vessel v, double amount) {
            if (v == null) {
                if (litres >= amount) {
                    litres -= amount;
                    System.out.println(amount + " litres of liquid wasted");
                } else {
                    System.out.println("Not enough liquid to waste.");
                }
            } else {
                if (litres >= amount) {
                    double actualPour = Math.min(amount, v.maxLitres - v.litres);
                    litres -= actualPour;
                    v.litres += actualPour;
                    System.out.println("Poured " + actualPour + " litres into the vessel.");
                } else{
                    System.out.println("Not enough liquid to pour.");
                }
            }
            return litres;
        }

        public void fill(double amount) {
            if (litres + amount <= maxLitres) {
                litres += amount;
                System.out.println("Filled " + amount + " litres.");
            } else {
                litres = maxLitres;
                System.out.println("Filled vessel to its maximum capacity of " + maxLitres + " litres.");
            }
        }

        public double getLitres() {
            return litres;
        }

        public double getCapacity() {
            return maxLitres;
        }
    }

    public class PlasticCup extends Vessel {

        public PlasticCup(double maxLitres) {
            super(maxLitres);
        }

        @Override
        public double pour(Vessel v, double amount) {
            return super.pour(v, amount);
        }

        @Override
        public void fill(double amount) {
            super.fill(amount);
        }
    }

    public class FilteredJug extends Vessel {
        private int numberOfUses;

        public FilteredJug(double maxLitres, int numberOfUses) {
            super(maxLitres);
            this.numberOfUses = numberOfUses;
        }

        @Override
        public double pour(Vessel v, double amount) {
            return super.pour(v, amount);
        }

        @Override
        public void fill(double amount) {
            if (numberOfUses > 0) {
                super.fill(amount);
                numberOfUses--;

            } else {
                System.out.println("This jug cannot be filled anymore!");
            }
        }

        public void changeFilter() {
            if (numberOfUses > 0) {
                System.out.println("This jug can be filled with any other sources!");
            }
            if (numberOfUses > 30) {
                System.out.println("This jug cannot be filled up any more!");
            }
        }
    }

    public class WineGlass extends Vessel {

        boolean isBroken;

        public WineGlass(double maxLitres, boolean isBroken) {
            super(maxLitres);
            this.isBroken = isBroken;
        }

        @Override
        public double pour(Vessel v, double amount) {
            if (isBroken) {
                System.out.println("Cannot pour into a broken wine glass.");
            }
            return super.pour(v, amount);
        }

        @Override
        public void fill(double amount) {
            super.fill(amount);
        }

        public void smash() {
            isBroken = true;
            System.out.println("The wine glass is now broken.");
        }
    }
}
