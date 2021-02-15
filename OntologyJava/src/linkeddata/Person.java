package linkeddata;

import java.util.List;
public class Person extends Entity {

    String first;
    String last;
    String middle;
    List<String> roles;
    List<Entity> related;

    public Person(String label, String iri, String first, String last, String middle, List<String> role, List<Entity> related) {
        super(label, iri);
        this.first = first;
        this.last = last;
        this.middle = middle;
        this.roles = role;
        this.related = related;
    }

    public void addRoles(List<String> roles) {
        for (String role : roles) {
            this.roles.add(role);
        }
    }

    public void addRelated(List<Entity> items) {
        for (Entity i : items){
            this.related.add(i);
        }
    }

}