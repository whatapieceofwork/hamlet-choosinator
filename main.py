# THE HAMLET CHOOSINATOR
# By Alison Bain
# A program to determine which Hamlet film adaptation the user should watch.
#
# Main program parts:
# - Take Input: take_input(answer_key)
# - Quiz: run_quiz()
# --- """Presents a series of questions, divides points between film categories, scores and returns result."""
# --- Print Choices: print_choices(category1, category2)
# --- Distribute Points: distribute_points(choice, category1, category2)
# --- Ask Question: ask_question(category1, category2)
# --- Results: results()
# - Quick Recommend: run_recommend()
# --- """Returns one of three hard-coded film recommendations."""
# - Library: run_library()
# --- """Presents information on films in library and films excluded from library. Multiple sorting options available for films in library."""
# --- Sort Library: sort_library(sort_order)
# --- Print Categories: print_categories()
#
# Potential future features:
# - Detailed personal recommendation blurbs for each Hamlet object. [DONE]
# - Expanded comparison feature: compare between Hamlets.
# - Additional categories for streaming availability, etc.
# - Additional Hamlets: Kline, Williamson, Terry
# - Advanced quiz with more specific questions: is the Fortinbras subplot included, etc.
# - Hamlet-adjacent recommendations: Rosencrantz and Guildenstern Are Dead, Haider, etc.


# Each new object in the Hamlet class appends itself to Hamlet.list and adds 1 to Hamlet.counter. Hamlet.list is used to iterate through Hamlet objects.
class Hamlet:
    counter = 0
    names = []
    list = []
    
    def __init__(self, name, actor, director, year, length, description, score=0):
        self.name = name
        self.actor = actor
        self.director = director
        self.year = year
        self.length = length
        self.description = description
        self.score = int(score)
        
        Hamlet.counter += 1
        Hamlet.list.append(self)
    
    def report_categories(self):
        self_categories = []
        for category in categories.items():
            if self in category[1][1]:
                self_categories.append(category[1][0])
        self_categories = sorted(self_categories)
        return format_list(self_categories)

    def report(self):
        print(f"Hamlet ({self.year})")
        print(f"Starring: {self.actor}")
        print(f"Directed by: {self.director}")
        print(f"Length: {self.length} minutes")
        print(f"Description: {self.description}")
        print(f"Categories: {self.report_categories()}")

# Initializing list of Hamlet objects
branagh = Hamlet("branagh", "Kenneth Branagh", "Kenneth Branagh", 1996, 242, "This four-hour Hamlet is a lavish, bombastic spectacle which uses the combined texts of both the quarto and folio. It's an excellent choice for students who need to watch an uncut version of the play or Shakespeare fans who somehow haven't ever seen Hamlet before.")
essiedu = Hamlet("essiedu", "Paapa Essiedu", "Simon Godwin", 2016, 175, "Filmed live at the Royal Shakespeare Theatre in Stratford-upon-Avon, this film captures an innovative 2016 stage production with an almost all-black cast and an extraordinarily charismatic young Hamlet. Perfect for anyone wanting a modern Hamlet theatre experience that doesn't stray too far from the text.")
gibson = Hamlet("gibson", "Mel Gibson", "Franco Zeffirelli", 1990, 135, "This streamlined blockbuster has an all-star cast, excellent period set design, and beautiful costumes. Mel Gibson is a surprisingly competent Hamlet, and this is a reasonable choice for anyone looking for a highly cinematic but still traditional adaptation.")
hawke = Hamlet("hawke", "Ethan Hawke", "Michael Almereyda", 2000, 217, "In this striking and divisive late-nineties adaptation, Hamlet gives his 'to be or not to be' soliloquy in the Action aisle of a Blockbuster Video Store. Fans of Baz Luhrmann's Romeo + Juliet may enjoy the innovative modern take, and Julia Stiles is one of the best Ophelias on film, but viewers new to Shakespeare (and fun-hating traditionalists) might be better-served elsewhere.")
peake = Hamlet("peake", "Maxine Peake", "Sarah Frankcom", 2015, 184, "Filmed live at the Royal Exchange Theatre in Manchester, this production is mostly noteworthy for having a gender-swapped Horatia and Polonia alongside a female actress playing a still-male Hamlet. Many of the directorial decisions are questionable, and the performance has pacing issues, but viewers who are already familiar with Hamlet may find something new to enjoy here.")
ramsay = Hamlet("ramsay", "Bruce Ramsay", "Bruce Ramsay", 2012, 89, "This intimate, streamlined Hamlet presents the play as a noir-ish family drama taking place over a single day in a claustrophobic, echoing estate. Not ideal for new Shakespeare fans, this is still a good choice for adult viewers who have already watched plenty of traditional Hamlets and want to see what happens when he doesn't get sent to England and is present for Ophelia's mad scene.")
scott = Hamlet("ramsay", "Campbell Scott", "Campbell Scott", 2000, 178, "This tragically underrated production has an excellent cast (including a black Ophelia and family), beautiful Regency-era set design, and a genuinely sympathetic Hamlet. Unusually strong directing means that each character's actions are clearly motivated, and the action is well-paced and easy to follow. My absolute top recommendation for anyone new to Hamlet or looking for a mostly-traditional film adaptation.")
tennant = Hamlet("tennant", "David Tennant", "Gregory Doran", 2009, 180, "This hybrid film was adapted from a live production at the Royal Shakespeare Theatre and maintains a traditionally stage-y feel. Tennant is one of the most compelling and dynamic Hamlets on film, and this is a good choice for viewers who aren't sure they could find Shakespeare interesting.")

# ExcludedHamlet is a mirror class to Hamlet, but tracked separately and not included in the quiz, main library, or recommendations
class ExcludedHamlet:
    counter = 0
    names = []
    list = []
    
    def __init__(self, name, actor, director, year, length, note):
        self.name = name
        self.actor = actor
        self.director = director
        self.year = year
        self.length = length
        self.note = note
        
        ExcludedHamlet.counter += 1
        ExcludedHamlet.list.append(self)
    
    def report(self):
        print(f"Hamlet ({self.year})")
        print(f"Starring: {self.actor}")
        print(f"Directed by: {self.director}")
        print(f"Length: {self.length} minutes")
        print(f"Reason for exclusion: {self.note}")

# ExcludedHamlet objects for the "What's Missing" section of the library
burton = ExcludedHamlet("burton", "Richard Burton", "Bill Colleran and John Gielgud", 1964, 191, "The performances here are excellent, and the minimalist rehearsal-style staging was innovative for the time, but the video quality is wretched and so vertically distorted that everyone looks blurrily four feet tall. You might as well listen to an audio play.")
fodor = ExcludedHamlet("fodor", "Wilson Belchambers", "Alexander Fodor", 2007, 131, "This is a poorly-crafted arthouse film with a few good ideas, including flashbacks to Hamlet's childhood and a female Horatia and Polonia. Unfortunately it's just a genuinely bad movie, and I can't recommend anyone watch it.")
houston = ExcludedHamlet("houston", "William Houston", "Michael Mundell", 2003, 114, "Others might find something to enjoy in this Hamlet, but I've never been able to get past the first few minutes. This low-budget Hamlet seems to have been filmed at a Renaissance Faire, and though the actors are competent, the directing is questionable and there are far better options elsewhere.")
jacobi = ExcludedHamlet("jacobi", "Derek Jacobi", "Rodney Bennett", 1980, 210, "Derek Jacobi is an excellent actor, but he's only seven years younger than his Queen Gertrude and two years OLDER than his King Claudius (Patrick Stewart, who also plays Claudius in the fantastic 2010 film with David Tennant). All of the action seems to take place in a featureless void, and there isn't anything to recommend this Hamlet over any of the more recent adaptations.")
olivier = ExcludedHamlet("olivier", "Laurence Olivier", "Laurence Olivier", 1948, 155, "Look, if you really want to watch Olivier's Hamlet I can't stop you. It's just... so... slow. So, so slow. And stagey. And outdated. And not to my tastes. But go ahead! It's a classic.")

# Dictionary of categories holding category name and fitting Hamlet films
categories = {
    "innovative": ["innovative", [essiedu, hawke, peake, tennant, ramsay]],
    "traditional": ["traditional", [branagh, gibson, scott]],
    "cinematic": ["cinematic", [branagh, gibson, hawke, ramsay, scott]],
    "stagelike": ["stagelike", [essiedu, peake, tennant]],
    "political": ["political", [branagh, essiedu, scott, tennant]],
    "intimate": ["intimate", [hawke, gibson, peake, ramsay]],
    "long": ["long", [branagh, hawke]],
    "medium-length": ["medium-length", [essiedu, peake, scott, tennant]],
    "short": ["short", [gibson, ramsay]],
    "modern": ["modern", [essiedu, hawke, peake, ramsay, tennant]],
    "period": ["period", [branagh, gibson, scott]]
}

# List of preferred categories to be populated with user's quiz answers
answer_list = []

# - BEGIN MISC TOOLS - #
def take_input(answer_key):
    """Prompt user for selection choice and validate. If choice matches answer key, return choice"""
    while True:
        choice = str(input(" > "))
        if len(choice) > 0 and choice.lower() in answer_key:
            break
        else:
            print("Please enter a valid selection.")
    return choice.lower()

def format_list(item_list):
    """Formats list into "a, b, and c" style string"""
    if len(item_list) == 0:
        return "none"
    elif len(item_list) == 1:
        return item_list[0]
    elif len(item_list) == 2:
        return f"{item_list[0]} and {item_list[1]}"
    else:
        # Join all items except the last one with a comma between them
        # Add the last element, separated by ", and" and a final "."
        out = ", ".join(item_list[:-1])
        return "{}, and {}".format(out, item_list[-1])

def print_header(header):
    """Prints header text with decorative underline of equal length"""
    print(header)
    print("-" * len(header))

def recommend(winner):
    """Prints recommended Hamlet"""
    print(f"You should watch Hamlet ({winner.year}), starring {winner.actor}!")
    print(f"Directed by {winner.director}, this Hamlet is {winner.report_categories()}.")
# - END MISC TOOLS - #

# - BEGIN QUIZ FUNCTIONS - #
def reset():
    """Resets the score counter for all Hamlets to 0"""
    for hamlet in Hamlet.list:
        hamlet.score = 0

def add_bias():
    """Adds initial bias based on creator preference"""
    tennant.score += 1
    scott.score += 1
    essiedu.score += 1
    gibson.score -= 1
    peake.score -= 1

def print_choices(category1, category2):
    """Print options for user, filling in the names of the categories"""
    print()
    print(f"{category1[0].title()} or {category2[0].title()}:")
    print(f"[A] I would strongly prefer the film be {category1[0]}.")
    print(f"[B] I would prefer the film be {category1[0]}.")
    print(f"[C] Either {category1[0]} or {category2[0]} is fine.")
    print(f"[D] I would prefer the film be {category2[0]}.")
    print(f"[E] I would strongly prefer the film be {category2[0]}.")

def distribute_points(choice, category1, category2):
    """Take two category arguments; assign points to the appropriate Hamlet scores based on weight of answer choice, append chosen category name to answer_list"""
    # Strongly Prefer gives 2 points to the chosen category and eliminates 1 point from its opposite category
    # Prefer gives 1 point to the chosen category
    if choice == "a":
        print(f"You chose: strongly prefer {category1[0]}.")
        answer_list.append(category1[0])
        for hamlet in category1[1]:           
            hamlet.score += 2
        for hamlet in category2[1]:
            hamlet.score -= 1
    elif choice == "b":
        print(f"You chose: prefer {category1[0]}.")
        answer_list.append(category1[0])
        for hamlet in category1[1]:           
            hamlet.score += 1
    elif choice == "c":
        print(f"You chose: no preference.")
    elif choice == "d":
        print(f"You chose: prefer {category2[0]}.")
        answer_list.append(category2[0])
        for hamlet in category2[1]:
            hamlet.score += 1
    elif choice == "e":
        print(f"You chose: strongly prefer {category2[0]}.")
        answer_list.append(category2[0])
        for hamlet in category2[1]:
            hamlet.score += 2
        for hamlet in category1[1]:
            hamlet.score -= 1

def ask_question(category1, category2):
    """Prints choices based on categories, gets user choice, distributes points"""
    print_choices(category1, category2)
    choice = take_input(["a", "b", "c", "d", "e", "list_points", "score", "results", "q", "quit"])
    if choice == "list_points":
        list_points()
    elif choice == "score":
        score()
    elif choice == "results":
        results()
    elif choice == "q" or choice == "quit":
        quit = True
        return quit
    else:
        distribute_points(choice, category1, category2)

def list_points():
    """Iterate alphabetically through all Hamlet objects, printing name and score. Used for debugging, can be called during quiz by entering 'list_points'"""
    sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.name)
    print(sorted_hamlets)
    for hamlet in sorted_hamlets:
        print(f"{hamlet.name.title()}: {hamlet.score}")
    return sorted_hamlets

def score():
    """Sorts the Hamlet films by current score, prints results and returns sorted list. Can be called during quiz by entering 'score'"""
    sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.score, reverse=True)
    for hamlet in sorted_hamlets:
        print(f"{hamlet.name.title()}: {hamlet.score}")
    print()
    return sorted_hamlets

def compare_categories(answer_list, winner):
    """Compares preferred categories chosen by the user with the winning film categories"""
    winner_categories = winner.report_categories()
    shared_categories = []
    for category in answer_list:
        if category in winner_categories and category not in shared_categories:
            shared_categories.append(category)
    shared_categories = sorted(shared_categories)
    return format_list(shared_categories)

def results():
    """Retrieves current score, declares winner based on score list. Can be called during quiz by entering 'results'"""
    print()
    final_score = score()
    winner = final_score[0]
    runner_up = final_score[1]
    shared_categories = compare_categories(answer_list, winner)
    shared_categories2 = compare_categories(answer_list, runner_up)
    if winner.score == runner_up.score:
        print("It was a tie!")
        print()
        recommend(winner)
        print(f"The categories matching your preferences are: {shared_categories}.")
        print()
        recommend(runner_up)
        print(f"The categories matching your preferences are: {shared_categories2}.")
    else:
        recommend(winner)
        print(f"The categories matching your preferences are: {shared_categories}.")
# - END QUIZ FUNCTIONS - #

# - BEGIN PRINT LIBRARY FUNCTIONS - #
def sort_library(sort_option):
    """Returns sorted list of Hamlet objects. Default sort is year, [a]ctor and [d]irector options use last name"""
    if sort_option == "a":
        sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.actor.split(" ", 1)[1])
    elif sort_option == "d":
        sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.director.split(" ", 1)[1])
        print(sorted_hamlets)
    elif sort_option == "l":
        sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.length)
    else:
        sorted_hamlets = sorted(Hamlet.list, key=lambda hamlet: hamlet.year)
    return sorted_hamlets

def print_categories():
    """Print category titles and brief list of films associated with that category"""
    for category in categories.items():
        print(f"{category[0].title()}:")
        for hamlet in category[1][1]:
            print(f"Hamlet ({hamlet.year}), starring {hamlet.actor}")
        print()    
# - END PRINT LIBRARY FUNCTIONS - #

# - BEGIN TOP-LEVEL PROGRAM FUNCTIONS - #
def run_quiz():
    """Run the quiz program, checking for a quit argument after each question"""
    while True:
        print_header("Hamlet Choosinator Quiz")
        print("Please select the choice that fits best, or type 'quit' at any time to exit.")
        print()
        reset()
        add_bias()
        check_quit = False

        while True:
            check_quit = ask_question(categories["cinematic"], categories["stagelike"])
            if check_quit == True:
                break
            check_quit = ask_question(categories["innovative"], categories["traditional"])
            if check_quit == True:
                break
            check_quit = ask_question(categories["modern"], categories["period"])
            if check_quit == True:
                break
            check_quit = ask_question(categories["long"], categories["short"])
            if check_quit == True:
                break
            check_quit = ask_question(categories["intimate"], categories["political"])
            if check_quit == True:
                break
            break
        
        if check_quit == True:
            break

        print()
        print_header("Hamlet Choosinator Quiz Results")
        results()
        print()
        print("For more information on the films, check out the film library in the main menu.")
        print()
        print("Would you like to play again? [Y]es or [N]o")
        play_again = take_input(["y", "n", "quit"])
        if play_again == "n" or play_again == "quit":
            print("Thanks for playing!")
            break

def run_recommend():
    """Return a quick Hamlet recommendation in one of three categories"""
    print_header("Hamlet Choosinator Quick Recommendations")
    print("Choose a quick recommendation category: ")
    print() 
    print("[T] Traditional, classic Hamlet (Best for Hamlet beginners)")
    print("[M] Mostly traditional Hamlet (Best for intermediate Hamlet viewers)")
    print("[W] Wildcard, innovative Hamlet (Best for those very familiar with Hamlet)")
    print("[Q] Quit")
    recommend_choice = take_input(["t", "m", "w", "q", "quit"])
    if recommend_choice == "t":
        recommend(scott)
        print(f"{scott.description}")
    elif recommend_choice == "m":
        recommend(tennant)
        print(f"{tennant.description}")
    elif recommend_choice == "w":
        recommend(hawke)
        print(f"{hawke.description}")
    elif recommend_choice == "q" or "quit":
        pass

def run_library():
    """Prints a report of Hamlet objects"""
    print_header("Hamlet Choosinator Library")
    print(f"There are {Hamlet.counter} Hamlets in the Choosinator library: ")
    print()
    for hamlet in Hamlet.list:
        hamlet.report()
        print()

    while True: 
        print("Options: ")
        print("[A] Sort by Actor")
        print("[D] Sort by Director")
        print("[L] Sort by Length")
        print("[Y] Sort by Year")
        print("[C] View Film Categories")
        print("[W] What's Missing?")
        print("[Q] Quit")
        sort_option = take_input(["a", "d", "l", "y", "c", "w", "q", "quit"])
        if sort_option == "q" or sort_option == "quit":
            break
        elif sort_option == "c":
            print_header("Hamlet Choosinator Film Categories")
            print()
            print_categories()
        elif sort_option == "w":
            print_header("Hamlet Films Rudely Excluded From the Hamlet Choosinator")
            print()
            sorted_excluded = sorted(ExcludedHamlet.list, key=lambda hamlet: hamlet.year)
            for hamlet in sorted_excluded:
                hamlet.report()
                print()
        else:
            sorted_hamlets = sort_library(sort_option)
            for hamlet in sorted_hamlets:
                hamlet.report()
                print()
# - END TOP-LEVEL PROGRAM FUNCTIONS - #

# - BEGIN PROGRAM - # 
print("Welcome to the Hamlet Choosinator!")
print()
print("This program will help you determine the best Hamlet film adaptation based on your preferences.")

while True:
    print()
    print_header("Hamlet Choosinator")
    print("Choose an option: ")
    print("[T] Take the quiz")
    print("[R] Quick recommendation")
    print("[L] Library of film options")
    print("[Q] Quit")
    print()
    program_choice = take_input(["t", "r", "l", "e", "q", "quit"])
    if program_choice == "t":
        run_quiz()
    elif program_choice == "r":
        run_recommend()
    elif program_choice == "l":
        run_library()
    elif program_choice == "q" or program_choice == "quit":
        print("Goodbye!")
        break
# - END PROGRAM - #