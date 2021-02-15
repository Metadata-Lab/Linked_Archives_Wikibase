package linkeddata;

import java.util.ArrayList;
import java.util.List;

public class Collection extends Entity {

    private List<String> subjects = new ArrayList<>();
    private String date;
    private String description;
    private String identifier;
    private List<String> types = new ArrayList<>();
    private String title;


    public Collection(String label, String iri, List<String> subjects, String date, String desc, String id,
                      List<String> types, String title) {
        super(label, iri);
        this.subjects = subjects;
        this.date = date;
        this.description = desc;
        this.identifier = id;
        this.types = types;
        this.title = title;
    }

}

