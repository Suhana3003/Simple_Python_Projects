import random

def madlib1():
    print("THE WINDOW") 
    gender = input("Choose man or woman: " ).lower()
    pronoun = input("His/Her: ").lower()
    pronoun2 = input("He/She: ").lower()
    name = input("Enter a name: ").title()
    verb = input("Enter a verb: ").lower()

    print("On a windy winter morning, a "+gender+" looked out of the window.The only thing "+pronoun2+" saw, a garden. A smile spread across "+pronoun+" face as she spotted "+name+", "+pronoun+" daughter, in the middle of the garden enjoying the weather. It started drizzling. "+name+" started "+verb+" joyfully."+pronoun2+" tried to wave to "+pronoun+" daughter, but "+pronoun+" elbow was stuck, "+pronoun+" arm hurt, "+pronoun+" smile turned upside down. Reality came crashing down as the drizzle turned into a storm. "+name+"'s murdered corpse consumed "+pronoun+" mind.On a windy winter morning, a "+gender+" looked out of the window of "+pronoun+" jail cell.")

def madlib2():
    print("IDENTITY CRISIS")
    name = input("Enter a male name: ").title()
    name2 = input("Enter a new male name: ").title()
    place = input("Enter the name of a place: ").title()
    print("The country was on fire. Communal riots had paralyzed most of the state. "+name+", with the help of a friend, got a fake identity card--his new "+name2+" was Rakesh--and booked a ticket to "+place+". The ticket checker on the train asked for his identification--"+name+" nervously showed the one he had recently procured. He seemed satisfied and "+name+" heaved a sigh of relief.At "+place+" there was none to fear. 'Assalamu alaikum,' said "+name+" to ward off a group of enraged people. The angriest of them, with bloodshot eyes, approached "+name+" and asked for his identity card.")

m = random.randint(1,2)
if m == 1:
    madlib1()
elif m == 2:
    madlib2()
