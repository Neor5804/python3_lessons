def create_record(name, phone, address):
    """Create record"""
    record = {
        'name' : name,
        'phone' : phone,
        'address' : address
    }
    return record

user1 = create_record("Vadim", "+375291923129", "Minsk")
user2 = create_record("Vasia", "+375200482304", "Brest")

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrashdaetsja medalyu " + medal)


give_award("Za Berlin", "vasia", "petya")
give_award("Za London", "petya")