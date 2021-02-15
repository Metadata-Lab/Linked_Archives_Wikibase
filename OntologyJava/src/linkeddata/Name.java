package linkeddata;

public class Name extends Entity {

    String title;
    String role;

    public Name(String label, String iri, String title, String role) {
        super(label, iri);
        this.title = title;
        this.role = role;
    }

}
