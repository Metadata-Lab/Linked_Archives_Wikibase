package linkeddata;

public class Event extends Entity {

    String date;
    String title;

    public Event(String label, String iri, String date, String title) {
        super(label, iri);
        this.date = date;
        this.title = title;
    }

}
