public class Pet {
    String name;
    String[] nicknames;
    int age;
    String type;
    boolean isHouseTrained;

    public Pet(String name, int age, String type, boolean isHouseTrained) {
        this.name = name;
        this.age = age;
        this.type = type;
        this.isHouseTrained = isHouseTrained;

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public boolean isHouseTrained() {
        return isHouseTrained;
    }

    public void setHouseTrained(boolean houseTrained) {
        isHouseTrained = houseTrained;
    }

    public static void main (String[] args) {
        Pet pet1 = new Pet("Kayla", 8, "Staffy", true);
    }
}
