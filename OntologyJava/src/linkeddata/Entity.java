package linkeddata;

import java.util.ArrayList;
import java.util.List;

public abstract class Entity {

    private int id = 0;
    private String label = "";
    private List<String> IRI = new ArrayList<>();

    public Entity(String label, String iri) {
        this.label = label;
        addIRI(iri);
    }

    public int getQID(){
        return id;
    }

    public void setQID(int newId){
        id = newId;
    }

    public String getLabel(){
        return label;
    }

    public void setLabel(String newLabel) {
        label = newLabel;
    }

    public List<String> getIRIs() {
        return IRI;
    }

    public void setIRIs(List<String> newIRIs){
        IRI = newIRIs;
    }

    public void addIRI(String newIRI){
        IRI.add(newIRI);
    }

}
