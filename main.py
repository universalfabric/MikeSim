"""
This is my main file for a mess around project.

Should be very simple.

Objective is to use code knowledge to date outside of the regular class structure.

Ideas:

1. Simple combat, 1 v 1
    Create player object and monster object.
    determine a turn system.
    give player and monster attributes, armor class, weapons, etc.
    implement in a progressive way, adding complexity along the way.

"""
# Code below is from a GPT3 result pulled on 20 Jan 24.  Unrelated to the comment above...prompt was:
'''
Prompt: Show me python code that could be used to generate a non-player character for the Traveller role playing game

GPT Answer:
Creating a non-player character (NPC) for a role-playing game like Traveller involves defining characteristics such as skills, attributes, and possibly a background story. Here's a simple example of Python code that generates a Traveller RPG-style NPC:
'''
 
import random

class TravellerNPC:
    def __init__(self):
        self.name = self.generate_name()
        self.age = random.randint(18, 50)
        self.attributes = self.generate_attributes()
        self.skills = self.generate_skills()
        self.background = self.generate_background()

    def generate_name(self):
        # Add logic to generate a name (you can use lists of names, etc.)
        return "NPC_Name"

    def generate_attributes(self):
        # Attributes could include Strength, Dexterity, Intelligence, etc.
        attributes = {
            'Strength': random.randint(1, 6),
            'Dexterity': random.randint(1, 6),
            'Endurance': random.randint(1, 6),
            'Intelligence': random.randint(1, 6),
            'Education': random.randint(1, 6),
            'Social': random.randint(1, 6)
        }
        return attributes

    def generate_skills(self):
        # Skills could include various abilities or proficiencies
        skills = {
            'Pilot': random.randint(0, 3),
            'Gun Combat': random.randint(0, 3),
            'Engineering': random.randint(0, 3),
            'Medic': random.randint(0, 3),
            'Leadership': random.randint(0, 3)
        }
        return skills

    def generate_background(self):
        # Add logic to generate a background story
        return "This NPC has a mysterious past."

    def display_npc(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Attributes:")
        for attribute, value in self.attributes.items():
            print(f"  {attribute}: {value}")
        print("Skills:")
        for skill, value in self.skills.items():
            print(f"  {skill}: {value}")
        print(f"Background: {self.background}")

# Example usage
npc = TravellerNPC()
npc.display_npc()
