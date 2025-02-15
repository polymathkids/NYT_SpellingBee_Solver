
class WordMakerAI():

    def __init__(self, words_file: str, verbose=False):
        # This initializer should read in the words into any data structures you see fit
        # The input format is a file of words separated by newlines

        self.current_words = set() # initialize dictionary of current words active in the game
        with open(words_file) as file_obj:
            for line in file_obj:
                # whatif not all in lowercase as in sample dict.: (added .lower)
                # whatif more than one word in a line: added .split(" ")[0]
                word = line.strip().lower().split(" ")[0]
                if len(word) > 3: # whatif input file has empty line: skip it. Valid words are 3 letters or longer
                    self.current_words.add(word) # add word to current words set as well


def scramble(key_letter, game_letters):
    wm = WordMakerAI("dictionary.txt")

    search_letters = game_letters + key_letter
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Build a set of letters to remove
    remove_these = {letter for letter in alphabet if letter not in search_letters}

    # Now remove words that contain *any* letter in remove_these
    keep_these = {
        word for word in wm.current_words
        # isdisjoint: Returns True if the set has no elements in common with other.
        # Sets are disjoint if and only if their intersection is the empty set.
        if remove_these.isdisjoint(word)  # word contains only letters in "letters"
           and key_letter in word  # word must contain 'e'
           and len(word) > 3
    }


    print(sorted(keep_these))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the NYT Spelling Bee Solver!")
    print("Enter the key letter and the letters on the board:")
    key_letter = input("Key letter: ").lower()
    game_letters = input("Game letters: ").lower()
    if len(key_letter) != 1 or not key_letter.isalpha():
        print("Invalid key letter. Please enter a single letter.")
        exit(1)
    if len(game_letters) != 6 or not game_letters.isalpha():
        print("Invalid game letters. Please enter 6 letters.")
        exit(1)
    # future update might be to only provide hints instead of full list of words
    print("I found the following words for you to try:")
    scramble(key_letter, game_letters)

