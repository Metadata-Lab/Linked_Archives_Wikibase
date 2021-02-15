package linkeddata;

import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Parser {

    String file;
    Ontology ontology;

    List<String> bibLines = new ArrayList<>();
    List<String> collectLines = new ArrayList<>();
    List<String> eventLines = new ArrayList<>();
    List<String> itemLines = new ArrayList<>();
    List<String> nameLines = new ArrayList<>();
    List<String> personLines = new ArrayList<>();
    List<String> placeLines = new ArrayList<>();
    List<String> seriesLines = new ArrayList<>();
    List<String> subjectLines = new ArrayList<>();

    Map<String, List<String>> categories =  new HashMap<>();

    public Parser(String file){
        this.file = file;
        ontology = new Ontology();

        categories.put("/subject", subjectLines);
        categories.put("227.", itemLines); //belfer
        categories.put("140.", itemLines); //becker
        categories.put("185.", itemLines); //koppel
        categories.put("/person", personLines);
        categories.put("/names", nameLines);
        categories.put("/countries", placeLines);
        categories.put("/event", eventLines);
        categories.put("/series", seriesLines);
        categories.put("/collection", collectLines);
        categories.put("/bib_series", bibLines);
    }

    public void readFile(){
        try {
            BufferedReader reader = new BufferedReader(new FileReader(this.file));
            String string;
            while ((string = reader.readLine()) != null) {
                int pipe = string.indexOf('|');
                String splice = string.substring(0, pipe);

                //unique cases
                if (splice.contains("/person/Eisenmann Charles")) {
                    subjectLines.add(string);
                    continue;
                } else if (splice.contains("/object")) {
                    continue;
                }

                for (String s : categories.keySet()) {
                    if (splice.contains(s)) {
                        categories.get(s).add(string);
                    }
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error: file not found.");
        } catch (IOException e) {
            System.out.println("Could not read file.");
        }
    }

    public void parseAll(){
        readFile();
        parseSubjects();
        parsePlaces();
        parseEvents();
        parseNames();
        parseBibSeries();
        parseCollections();
        parseSeries();
        parseItems();
        parsePeople();
    }

    /*
     Property           Index
     "IRI"              0
     "hasAppearance"    1
     "hasBib_series"    2
     "hasComposer"      3
     "hasHost"          4
     "hasHumanSubject"  5
     "hasInterviewee"   6
     "hasObject"        7
     "hasPerformer"     8
     "hasPhotographer"  9
     "hasReporter"      10
     "hasSubject"       11
     "is_part_of"       12
     "is_related_to"    13
     "is_created_by"    14
     "firstname"        15
     "lastname"         16
     "middleinitial"    17
     "role"             18
     "coverage"         19
     "date"             20
     "description"      21
     "identifier"       22
     "publisher"        23
     "rights"           24
     "subject"          25
     "title"            26
     "title_alt"        27
     "type"             28
     "type/mediaType"   29
     "mediaType"        30
     "comment"          31
     "label"            32
     */

    String removeExtraQuotes(String str) {
        while (str.charAt(0) == '\'' || str.charAt(0) == '\"') {
            str = str.substring(1);
            if (str.length() == 0) return str;
        }
        while (str.charAt(str.length()-1) == '\'' || str.charAt(str.length()-1) == '\"') {
            str = str.substring(0, str.length()-1);
            if (str.length() == 0) return str;
        }
        if (str.contains("the Newest \"Drug War")) str += "\"";
        else if (str.contains("the Newest \'Drug War")) str += "\'";
        return str.strip();
    }

    List<String> divideEntries(String str){
        String[] list = str.split("\t");
        List<String> items = new ArrayList<>();
        for (int i = 0; i < list.length; i++) {
            String item = list[i];
            if (item.contains("Unknown")) continue;
            items.add(removeExtraQuotes(item));

        }
        return items;
    }

    public void parseBibSeries(){
        for (String line : bibLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            BibSeries bib = new BibSeries(label, split[0]);
            ontology.addObject(label, bib);
        }
    }

    public void parseCollections(){
        for (String line : collectLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            List<String> subjects = divideEntries(split[25]);
            List<String> types = divideEntries(split[28]);
            Collection coll = new Collection(label, split[0], subjects, split[20],
                    removeExtraQuotes(split[21]), removeExtraQuotes(split[22]), types,
                    removeExtraQuotes(split[26]));
            ontology.addObject(label, coll);
        }
    }

    public void parseEvents(){
        for (String line : eventLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            Event event = new Event(label, split[0], split[20], split[26].substring(1, split[26].length()-1));
            ontology.addObject(label, event);
        }
    }

    public void parseItems(){
        for (String line : itemLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            Item item = new Item(label, split[0], ontology.getCollection(removeExtraQuotes(split[12])),
                    removeExtraQuotes(split[19]), removeExtraQuotes(split[20]), removeExtraQuotes(split[21]),
                    removeExtraQuotes(split[22]), removeExtraQuotes(split[24]),
                    ontology.getSubject(removeExtraQuotes(split[25])), removeExtraQuotes(split[26]),
                    removeExtraQuotes(split[28]), removeExtraQuotes(split[30]));
            ontology.addObject(label, item);
        }
    }

    public void parseNames(){
        for (String line : nameLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            Name name = new Name(label, split[0], split[18], removeExtraQuotes(split[26]));
            ontology.addObject(label, name);
        }
    }

    String personLabel(String[] personLine) {
        String first = removeExtraQuotes(personLine[15]);
        String last = removeExtraQuotes(personLine[16]);
        String middle = removeExtraQuotes(personLine[17]);

        String label = first + " " + middle + " " + last;
        label = label.replace("  ", " ").strip();
        return label;
    }

    List<Entity> extractEntities(List<String> itemStrs) {
        List<Entity> entities = new ArrayList<>();
        for (String label : itemStrs) {
            Entity toAdd;
            if (ontology.subjectExists(label)) toAdd = ontology.getSubject(label);
            else toAdd = ontology.getItem(label);
            entities.add(toAdd);
        }
        return entities;
    }

    public void parsePeople(){
        for (String line : personLines) {
            String[] split = line.split("\\|");
            String label = personLabel(split);
            List<String> roles = divideEntries(split[18]);
            List<String> relStr = divideEntries(split[13]);
            List<Entity> entities = extractEntities(relStr);
            if (ontology.personExists(label)) {
                Person person = ontology.getPerson(label);
                person.addIRI(split[0]);
                person.addRoles(roles);
                person.addRelated(entities);
            } else {
                Person person = new Person(label, split[0], removeExtraQuotes(split[15]), removeExtraQuotes(split[16]),
                        removeExtraQuotes(split[17]), roles, entities);
                ontology.addObject(label, person);
            }
        }
    }

    public void parsePlaces(){
        for (String line : placeLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            Place place = new Place(label, split[0]);
            ontology.addObject(label, place);
        }
    }

    public void parseSeries(){
        for (String line : seriesLines) {
            String[] split = line.split("\\|");
            String label = removeExtraQuotes(split[32]);
            Series series = new Series(label, split[0], ontology.getCollection(split[12]));
            ontology.addObject(label, series);
        }
    }

    public void parseSubjects(){
        for (String line : subjectLines) {
            String[] split = line.split("\\|");
            String label = split[0].substring(split[0].lastIndexOf("/")+1);
            if (ontology.subjectExists(label)) {
                Subject subject = ontology.getSubject(label);
                subject.addIRI(split[0]);
            } else {
                Subject subject = new Subject(label, split[0]);
                ontology.addObject(label, subject);
            }
        }
    }
}
