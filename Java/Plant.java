
public class Plant {
    boolean isAlive;
    int soilMoistureLevel;
    String nickname;
    int height;

    public Plant(boolean isAlive, int soilMoistureLevel, String nickname, int height) {
        this.isAlive = isAlive;
        this.soilMoistureLevel = soilMoistureLevel;
        this.nickname = nickname;
        this.height = height;
    }

    public void setNickname(String name) {
        this.nickname = name;
    }

    public String getNickname() {
        return this.nickname;
    }

    public void water() {
        soilMoistureLevel ++;
    }

    public boolean isDead() {
        return isAlive = true;
    }


}