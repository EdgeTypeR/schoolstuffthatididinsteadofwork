import random
def add_person_to_list():
    people = []
    while True:
        person = input("írd be az ember instáját (vagy írd azt hogy 'vége' ha nincs több): ")
        if person.lower() == 'vége':
            break
        people.append(person)
    return people

def raffle(people):
    if not people:
        print("nincsenek emberek felvéve")
    győztes = random.choice(people)
    print(f"a nyertes: {győztes}")
    return győztes

people_list = add_person_to_list()
raffle(people_list)