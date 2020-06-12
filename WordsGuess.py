# coding=UTF-8
import random # Används när programmet ska hämta ett ord.
import io # Io modulen används eftersom vi använder oss av en fil som innehåller speciella tecken
class SystemGuess:

    subsets_2 = ["0,1", "0,2", "0,3", "0,4", "1,2", "1,3", "1,4", "2,3", "2,4", "3,4"]
    subsets_3 = ["0,1,2", "0,1,3", "0,1,4", "0,2,3", "0,2,4", "0,3,4", "1,2,3", "1,2,4", "1,3,4", "2,3,4"]
    subsets_4 = ["0,1,2,3", "0,1,2,4", "0,1,3,4", "0,2,3,4", "1,2,3,4"]

    def __init__(self):
        print("Startar spelet")

    """
    
     Den här metoden använder sig av indexuppsättningen som finns ovan och använder sig av funktionen som finns nedan
     som t.ex. antal gissade ord, lista av alla orden och en tom lista på alla ord som behöver fyllas med dem
     filtrerade orden.
     
     Om vi t.ex. använder ordet "HALLÅ" och bokstäverna 'A' och 'L' är korrekt positionerade så kommer den att 
     tillämpa index_list 1,2 i listan på ord som har samma bokstäver på samma position och om det finns liknande ord
     så kommer den slumpmässigt gå igenom listan på ord som uppfyller kriterierna enligt index.
     
     Den här metoden sparar ord som är på rätt plats.

    """
    # Sparar och jämför bokstäver som finns på 'rätt plats'.
    def fill_list_with_exact_indexes(self, index_list, input_list, output_list, word):
        if len(index_list) == 2:
            x = int(index_list[0])
            y = int(index_list[1])
            a = word[x]
            b = word[y]
            for line in input_list:
                if line[x] == a and line[y] == b:
                    if line != word:
                        output_list.append(line)
        elif len(index_list) == 3:
            x = int(index_list[0])
            y = int(index_list[1])
            z = int(index_list[2])
            a = word[x]
            b = word[y]
            c = word[z]
            for line in input_list:
                if line[x] == a and line[y] == b and line[z] == c:
                    if line != word:
                        output_list.append(line)
        elif len(index_list) == 4:
            x = int(index_list[0])
            y = int(index_list[1])
            z = int(index_list[2])
            o = int(index_list[3])
            a = word[x]
            b = word[y]
            c = word[z]
            d = word[o]
            for line in input_list:
                if line[x] == a and line[y] == b and line[z] == c and line[o] == d:
                    if line != word:
                        output_list.append(line)

    """
    Den här metoden fungerar som ovan men används när datorn vet att vi har skrivit in rätt bokstäver som
    inte är i rätt position.
    
    Om värdet 0,4 (första och sista bokstaven) tillämpas för indexlistan för ordet 'HALLÅ' så kommer den att leta efter 
    ord genom input_list som innehåller bokstäverna 'H' och 'Å'.

    """
    # Sparar och jämför bokstäver som inte är på rätt plats
    def fill_list_which_contains_chars(self, index_list, input_list, output_list, word):
        if len(index_list) == 2:
            x = int(index_list[0])
            y = int(index_list[1])
            a = word[x]
            b = word[y]
            for line in input_list:
                if line.__contains__(a) and line.__contains__(b):
                    if line != word:
                        output_list.append(line)
        elif len(index_list) == 3:
            x = int(index_list[0])
            y = int(index_list[1])
            z = int(index_list[2])
            a = word[x]
            b = word[y]
            c = word[z]
            for line in input_list:
                if line.__contains__(a) and line.__contains__(b) and line.__contains__(c):
                    if line != word:
                        output_list.append(line)
        elif len(index_list) == 4:
            x = int(index_list[0])
            y = int(index_list[1])
            z = int(index_list[2])
            o = int(index_list[3])
            a = word[x]
            b = word[y]
            c = word[z]
            d = word[o]
            for line in input_list:
                if line.__contains__(a) and line.__contains__(b) and line.__contains__(c) and line.__contains__(d):
                    if line != word:
                        output_list.append(line)

    """
    
    Den här metoden använder sig av attributerna words_list, word_guessed och antal bokstäver på rätt plats och ger ett värde
    som argument och hämtar en lista på ord som innehåller dem bokstäverna.
    
    T.ex. om datorn gissade på ordet 'GRODA' och användaren gav input att den innehåller 2 bokstäver som inte är på
    rätt plats så kommer size få värdet 2 och den kommer att hämta ett nytt ord från listan som innehåller en
    kombination av bokstäverna som finns inkluderat för ordet 'GRODA'.
    
    Alltså kommer den att använda sig av subset_2 och tillämpa dessa värden med hjälp av indexering
    när den försöker komma på rätta ordet.
    
    """

    def get_contains(self, input_list, word, size):
        output_list = []
        if size == 1:
            for line in input_list:
                if line.__contains__(word[0]) or line.__contains__(word[1]) or line.__contains__(word[2]) or \
                        line.__contains__(word[3]) or line.__contains__(word[4]):
                    if line != word:
                        output_list.append(line)
        elif size == 2:
            for subset in self.subsets_2:
                list_of_indexes = subset.split(",")
                self.fill_list_which_contains_chars(list_of_indexes,input_list,output_list,word)
        elif size == 3:
            for subset in self.subsets_3:
                list_of_indexes = subset.split(",")
                self.fill_list_which_contains_chars(list_of_indexes, input_list, output_list, word)
        elif size == 4 :
            for subset in self.subsets_4:
                list_of_indexes = subset.split(",")
                self.fill_list_which_contains_chars(list_of_indexes, input_list, output_list, word)
        return output_list

    """
    Samma som ovan men den frågar efter ord där den vet exakt vart vissa bokstäver måste befinna sig.
    """
    # En loop som programmet använder för att begränsa sökningen genom att använda index.
    # 0 resultat innebär att den ska slumpmässigt välja ett nytt ord från word-listan.
    # Line är användarens gissning och word är programmens hemliga ord
    def get_exact_located(self, input_list, word, size):
        output_list = []
        if size == 1:
            for line in input_list:
                if line != word:
                    if line[0] == word[0]:
                        output_list.append(line)
                    elif line[1] == word[1]:
                        output_list.append(line)
                    elif line[2] == word[2]:
                        output_list.append(line)
                    elif line[3] == word[3]:
                        output_list.append(line)
                    elif line[4] == word[4]:
                        output_list.append(line)
        elif size == 2:
            for subset in self.subsets_2:
                list_of_indexes = subset.split(",")
                self.fill_list_with_exact_indexes(list_of_indexes,input_list,output_list,word)
        elif size == 3:
            for subset in self.subsets_3:
                list_of_indexes = subset.split(",")
                self.fill_list_with_exact_indexes(list_of_indexes, input_list, output_list, word)
        elif size == 4:
            for subset in self.subsets_4:
                list_of_indexes = subset.split(",")
                self.fill_list_with_exact_indexes(list_of_indexes, input_list, output_list, word)
        return output_list

    """
    Programmet hämtar slumpmässigt ett ord och ger det värdet till användaren
    """
    def get_random_word(self, input_list):
        return random.choice(input_list)

    """Loop som frågar hur många bokstäver som är på rätt plats och hur många bokstäver som är rätt i ett ord och 
    återvänder med ett värde"""
    def hows_my_guess(self, input, mysecret):
        correct_positioned = 0
        contains = 0
        for i in range(5):
            for j in range(5):
                if input[i] == mysecret[j]:
                    if i == j:
                        correct_positioned += 1
                    else:
                        contains += 1
        return correct_positioned, contains

    def user_vs_program(self, words_list):
        list_of_words = words_list
        guess_count = 0
        while True:
            if len(list_of_words) > 0:
                guess_count += 1
                word_guessed = guess.get_random_word(list_of_words)
                print(f"Word i guessed is : {word_guessed}")
                is_correct = input("Is that correct word : yes/no : ")
                if is_correct == "yes":
                    print(f"I won with total guesses : {guess_count}")
                    break
                else:
                    exact = int(input("How many characters are in correct position: "))
                    contains = int(input("How many correct characters are present but not in correct position: "))
                    if exact == 0 and contains == 0:
                        continue
                    else:
                        # Programmet letar efter ord baserat på tidigare gissningar och användarens input.
                        if exact > 0 and contains > 0:
                            list_contains = guess.get_contains(list_of_words, word_guessed, contains)
                            list_exact = guess.get_exact_located(list_of_words, word_guessed, exact)
                            list_contains_as_set = set(list_contains)
                            list_exact_as_set = set(list_exact)
                            result_common_set = list_contains_as_set.intersection(list_exact_as_set)
                            list_of_words = list(result_common_set)
                        elif exact > 0 and contains == 0:
                            list_exact = guess.get_exact_located(list_of_words, word_guessed, exact)
                            list_exact_as_set = set(list_exact)
                            list_of_words = list(list_exact_as_set)
                        elif exact == 0 and contains > 0:
                            list_contains = guess.get_contains(list_of_words, word_guessed, contains)
                            list_contains_as_set = set(list_contains)
                            list_of_words = list(list_contains_as_set)
                do_quit = input("Do you want to quit : yes/no : ")
                if do_quit == "yes":
                    break
            else:
                print("i am out of guesses")
                break
            print(len(list_of_words))

    """
    Program Vs User betyder att programmet ska försöka gissa på ordet och användaren ska ge ledtrådar till programmet
    genom att ge ett värde baserat på frågeställningar.
    """
    def programVsUser(self, words_list):
        list_of_words = words_list
        count_guess = 0
        secret_word = self.get_random_word(list_of_words)
        while True:
            count_guess += 1
            word_guessed = input("Enter the word you guessed : ")
            if len(word_guessed) != 5:
                # En parameter som gör att användaren måste gissa ett nytt ord om ordet inte innehåller 5 bokstäver.
                continue
            if word_guessed == secret_word:
                print(f"you won with {count_guess} guesses")
            else:
                corr_pos, contains = self.hows_my_guess(word_guessed, secret_word)
                if corr_pos > 0:
                    print(f"{corr_pos} : characters are in correct position in my chosen secret word")
                if contains > 0:
                    print(f"{contains} : characters are in there in my chosen secret word but not in correct position")
                if corr_pos == 0 and contains == 0:
                    print("The secret word doesn't contain any of the guessed word character")
            do_quit = input("Do you want to quit : yes/no : ")
            if do_quit == "yes":
                break
    """
    För att öppna och läsa filen som innehåller alla ord så använder jag path
    """
    def read_file(self, path):
        path = io.open(path, mode="r", encoding="utf-8")
        list_of_words = []
        lines = path.readlines()
        for line in lines:
            line = line[0:5]
            if len(line) == 5:
                list_of_words.append(line)
        return list_of_words

if __name__ == "__main__":
    guess = SystemGuess()
    list_of_words = guess.read_file("C:\\Users\\Unver\\Desktop\\words.txt")
    # Koden ovan hämtar orden från den path som jag har angett, i detta fall words.txt

    print('''
    Choose a game mode : Program Vs User or User Vs Program
    1. Program vs User : The program will choose a word and the user will guess
    2. User vs Program : The user will choose a word and the program will guess
    ''')
    mode = int(input("Which game mode would you like to play ?  1 or 2  "))
    if mode == 1:
        guess.programVsUser(list_of_words)
    elif mode == 2:
        guess.user_vs_program(list_of_words)
    else:
        print("invalid input")