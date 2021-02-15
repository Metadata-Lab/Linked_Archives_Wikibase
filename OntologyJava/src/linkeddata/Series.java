package linkeddata;

public class Series extends Entity {

    private Collection isPartOf;

    public Series(String label, String iri, Collection isPartOf) {
        super(label, iri);
        this.isPartOf = isPartOf;
    }

}
