import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Interaction {
    public interface Interactable {
        public void talkTo(Interactable thing);
        public List<String> responseScript();
        public List<String> contactScript();
    }

    public class Person implements Interactable {
        private String name;
        private List<String> contact;
        private List<String> responses;

        public Person(String name, List<String> contact, List<String> responses) {
            this.name = name;
            this.contact = contact;
            this.responses = responses;
        }

        @Override
        public void talkTo(Interactable thing) {
            List<String> initiation = contactScript();

            for (String init : initiation) {
                System.out.println(name + ": " + init);

                List<String> responses = thing.responseScript();

                if(!responses.isEmpty()) {
                    System.out.println(thing.getClass().getSimpleName() + ": " + responses.get(0));
                }
            }

        }

        @Override
        public List<String> responseScript() {
            return responses;
        }

        @Override
        public List<String> contactScript() {
            List<String> script = new ArrayList<>();
            script.add("How are you?");
            script.add("Fine, see you soon");
            return script;
        }

        public String getName() {
            return name;
        }
    }

    public class Alien implements Interactable {
        private boolean isHostile;
        private List<String> contact;
        private List<String> responses;

        public Alien(boolean isHostile, List<String> contact, List<String> responses) {
            this.isHostile = isHostile;
            this.contact = contact;
            this.responses = responses;
        }

        @Override
        public void talkTo(Interactable thing) {
            List<String> initiation = contactScript();
            for (String init : initiation) {
                System.out.println("Alien: " + init);
                if (isHostile) {
                    System.out.println("Alien: Get away!");
                } else {
                    List<String> responses = responseScript();
                    if (!responses.isEmpty()) {
                        System.out.println(thing.getClass().getSimpleName() + ": " + responses.get(0));
                    }
                }
            }
        }
        @Override
        public List<String> responseScript() {
            return responses;
        }

        @Override
        public List<String> contactScript() {
            List<String> script = new ArrayList<>();
            script.add("What do you want?");
            return script;
        }
    }

    public class Billboard implements Interactable {

        private String content;

        public Billboard(String content) {
            this.content = content;
        }

        @Override
        public void talkTo(Interactable thing) {
            System.out.println("Billboard: " + content);

        }

        @Override
        public List<String> responseScript() {
            return Collections.singletonList(content);
        }

        @Override
        public List<String> contactScript() {
            return Collections.emptyList();
        }
    }


}
