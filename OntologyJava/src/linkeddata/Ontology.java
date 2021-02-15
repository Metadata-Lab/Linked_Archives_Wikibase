package linkeddata;

import java.util.Map;
import java.util.HashMap;

public class Ontology {

    private Map<String, BibSeries> bibSeries;
    private Map<String, Collection> collections;
    private Map<String, Event> events;
    private Map<String, Item> items;
    private Map<String, Name> names;
    private Map<String, Person> people;
    private Map<String, Place> places;
    private Map<String, Series> series;
    private Map<String, Subject> subjects;

    public Ontology(){
        bibSeries = new HashMap<>();
        collections = new HashMap<>();
        events = new HashMap<>();
        items = new HashMap<>();
        names = new HashMap<>();
        people = new HashMap<>();
        places = new HashMap<>();
        series = new HashMap<>();
        subjects = new HashMap<>();
    }

    public void addObject(String label, BibSeries obj) { bibSeries.put(label, obj); }
    public void addObject(String label, Collection obj) { collections.put(label, obj); }
    public void addObject(String label, Event obj) { events.put(label, obj); }
    public void addObject(String label, Item obj) { items.put(label, obj); }
    public void addObject(String label, Name obj) { names.put(label, obj); }
    public void addObject(String label, Person obj) { people.put(label, obj); }
    public void addObject(String label, Place obj) { places.put(label, obj); }
    public void addObject(String label, Series obj) { series.put(label, obj); }
    public void addObject(String label, Subject obj) { subjects.put(label, obj); }

    public BibSeries getBibSeries(String label) { return bibSeries.get(label); }
    public Collection getCollection(String label) { return collections.get(label); }
    public Event getEvent(String label) { return events.get(label); }

    public Name getName(String label) { return names.get(label); }
    public Person getPerson(String label) { return people.get(label); }
    public Place getPlace(String label) { return places.get(label); }
    public Series getSeries(String label) { return series.get(label); }


    public boolean personExists(String label) { return (people.keySet().contains(label)); }
    public boolean subjectExists(String label) { return (subjects.keySet().contains(label)); }

    public Map<String, Subject> getSubjects() {
        return subjects;
    }

    public Map<String, Item> getItems() {
        return items;
    }

    public Item getItem(String label) {
        if (items.get(label) != null) return items.get(label);
        else {
            for (String s : items.keySet()) {
                if (s.contains(label)) return items.get(s);
                else if (s.contains(label.replace("\"", "\'"))) return items.get(s);
            }
            return null;
        }
    }

    public Subject getSubject(String label) {
        return subjects.get(label);
    }

}
