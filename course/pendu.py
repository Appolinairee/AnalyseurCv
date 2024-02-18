import random

def get_character():
    while True:
        l = input("\n\nDevinez une lettre : ").upper()
        if l.isalpha() and len(l) == 1:
            return l
        else:
            print("Veuillez entrer une seule lettre.")


def initialize_word(filename):
    try:
        with open(filename, "r") as file:
            words = [line.strip().upper() for line in file.readlines()]
        return random.choice(words)
    except FileNotFoundError:
        print("Erreur lors de l'ouverture du fichier des mots secrets.")
        raise



def play_game(word):
    hidden_word = '*' * len(word)
    coup = 0

    while coup < len(word) + 6:
        temp = sum(1 for char in hidden_word if char != '*')

        if temp == len(hidden_word):
            break

        print(f"Nombre de coup restant: {len(word) + 6 - coup}\n{hidden_word}\n")

        l = get_character()

        for i, char in enumerate(word):
            if l == char:
                hidden_word = hidden_word[:i] + l + hidden_word[i + 1:]

        coup += 1

    if temp == len(word):
        print(f"\nMot secret: {hidden_word}\nBravo! Mot secret devine en {coup} coups!\n")
    else:
        print(f"\nOoops! Vous n'avez pas devine le mot secret! \nMot secret: {word}")



if __name__ == "__main__":
    try:
        print("\n____Bienvenue dans le Pendu !____")
        secret_word = initialize_word("./secretsWords.txt")

        print(f"\nMot secret de {len(secret_word)} lettres\n")
        play_game(secret_word)
    except Exception as e:
        print(f"Erreur inattendue: {e}")