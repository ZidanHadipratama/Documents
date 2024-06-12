from flask import Flask, Response
import random

app = Flask(__name__)

def leet_transform(word):
    replacements = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'), ('t', '7'), ('s', '5'), ('g', '6')]
    chosen_replacements = random.sample(replacements, 3)
    for old, new in chosen_replacements:
        word = word.replace(old, new).replace(old.upper(), new)
    return word

def generate_nickname():
    adjectives = [
        "Crazy", "Mystic", "Silent", "Ancient", "Ghost", "Rogue", "Sly", "Swift", "Cyber", "Shadow",
        "Fierce", "Brave", "Dark", "Electric", "Wild", "Vicious", "Savage", "Fearless", "Noble", "Arcane",
        "Cryptic", "Lethal", "Mighty", "Vigilant", "Eternal", "Infernal", "Galactic", "Astral", "Spectral",
        "Stealthy", "Wicked", "Enigmatic", "Daring", "Merciless", "Grim", "Majestic", "Phantom", "Elusive", "Ferocious"
    ]
    nouns = [
        "Hacker", "Coder", "Pirate", "Ninja", "Agent", "Phantom", "Wizard", "Knight", "Guru", "Sniper",
        "Samurai", "Mercenary", "Vanguard", "Warden", "Assassin", "Hunter", "Guardian", "Sentinel", "Ranger", "Warrior",
        "Seeker", "Champion", "Conqueror", "Defender", "Destroyer", "Invader", "Marauder", "Raider", "Vanquisher", "Warlord",
        "Sorcerer", "Mage", "Shaman", "Druid", "Paladin", "Necromancer", "Berserker", "Monk", "Priest", "Rogue"
    ]
    return leet_transform(random.choice(adjectives) + random.choice(nouns))

@app.route('/getnicknames', methods=['GET'])
def get_nicknames():
    nicknames = [generate_nickname() for _ in range(200)]
    return Response('\n'.join(nicknames), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=False)
