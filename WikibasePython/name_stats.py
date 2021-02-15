import json

def count_matches(matches):
    counts = {}
    people = {}
    for person in matches.keys():
        count = len(matches.get(person))
        if count in counts.keys():
            old = counts.get(count)
            counts[count] = old + 1
            people[count].append(person)
        else:
            counts[count] = 1
            people[count] = [person]

    for i in range(300):
        if i in counts.keys():
            print(str(i) + "\t" + str(counts.get(i)))
        #else: print(str(i) + "\t0")

    return people


def main():
    with open("matches.json") as json_file:
        matches = json.load(json_file)
    people = count_matches(matches)


if __name__ == '__main__':
    main()