from tkinter import *
from tkinter.ttk import *
import random

# Variables:
global temp
temp = ""
global temp2
temp2 = []


def begin():
    for widget in root.winfo_children():
        widget.destroy()
    lbl1 = Label(root, text = "What sort of names do you want to generate?").pack(side = TOP)
    btn2 = Button(root, text = "Company names", command = Company).pack(fill=X)
    btn3 = Button(root, text = "Human names", command = Human).pack(fill=X)
    btn4 = Button(root, text = "Robot names", command = Robot).pack(fill=X)
    btn5 = Button(root, text = "Country names", command = Country).pack(fill=X)


def Company():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Company1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Company2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT) 
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Companycalc():
    # TODO: Add more names
    # Setup
    listA = ["United", "Wholesome", "Micro", "Giant"]
    listB = ["Foods", "Industries", "Engineering", "Technology", "Games"]
    listC = ["Ltd.", "Corp.", "Inc.", ""]

    listAlen = len(listA)
    listBlen = len(listB)
    listClen = len(listC)

    for i in range(times):
        # Generation
        tempA = listA[random.randint(0, listAlen-1)]
        tempB = listB[random.randint(0, listBlen-1)]
        tempC = listC[random.randint(0, listClen-1)]

        global temp2
        temp = tempA + " " + tempB + " " + tempC
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Company()
def Company1():
    global temp2
    temp2 = []
    global times
    times = 1
    Companycalc()
def Company2():
    global temp2
    temp2 = []
    global times
    times = 10
    Companycalc()


def Robot():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Robot1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Robot2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT) 
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Robot1():
    global temp2
    temp2 = []
    global times
    times = 1
    Robotcalc()
def Robot2():
    global temp2
    temp2 = []
    global times
    times = 10
    Robotcalc()
def Robotcalc():
    # TODO: Add more names
    # Setup
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = str.upper(alphabet_lower)

    for i in range(times):
        # Generation
        rand = random.randint(0, 2)
        if rand == 0:
            tempA = str(random.randint(1000, 9999))
            tempB = alphabet_lower[random.randint(0, len(alphabet_lower)-1)]
            tempC = str(random.randint(1, 1000))

            temp = tempA + tempB + tempC
        elif rand == 1:
            tempA = alphabet_lower[random.randint(0, len(alphabet_lower)-1)]
            tempB = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempC = str(random.randint(1000, 9999))
            tempD = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempE = str(random.randint(1, 1000))

            temp = tempA + tempB + tempC + tempD + tempE
        elif rand == 2:
            tempA = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempB = str(random.randint(0, 9))
            tempC = alphabet_upper[random.randint(0, len(alphabet_upper)-1)]
            tempD = str(random.randint(0, 9))

            temp = tempA + tempB + tempC + tempD
        else:
            print("error! 108")

        global temp2
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Robot()


def Country():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Country1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Country2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT)  
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Country1():
    global temp2
    temp2 = []
    global times
    times = 1
    Countrycalc()
def Country2():
    global temp2
    temp2 = []
    global times
    times = 10
    Countrycalc()
def Countrycalc():
    # TODO: Add more names
    # Setup
            # If you add more names into listA, put a space infront for asthetics
    listA = [" Great", " United States of", " Monumental", " Allmighty", "", "" , "", "", "", "", "", "", "", "", "", "", "", ""]
    listB = ["Cu", "So", "Swe", "Ethi", "Sau", "Chi", "Indi", "Eng", "Nor", "Bri"]
    listC = ["n", "b", "mali", "ad", "co", "way", "t", "", ""]
    listD = ["annia", "land", "a", "ain", ""]

    listAlen = len(listA)
    listBlen = len(listB)
    listClen = len(listC)
    listDlen = len(listD)
    for i in range(times):
        # Generation
        tempA = listA[random.randint(0, listAlen-1)]
        tempB = listB[random.randint(0, listBlen-1)]
        tempC = listC[random.randint(0, listClen-1)]
        tempD = listD[random.randint(0, listDlen-1)]

        temp = tempA + " " + tempB + tempC + tempD
        global temp2
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Country()


def Human():
    for widget in root.winfo_children():
        widget.destroy()
    btn1 = Button(root, text = "Generate!", command = Human1).pack()
    btn2 = Button(root, text = "Generate 10!", command = Human2).pack()
    txt1 = Text(root, height = 10, wrap = WORD)
    txt1.insert(1.0, temp2)
    txt1.pack()
    txt1.configure(bg=root.cget('bg'), relief=FLAT)  
    btn0 = Button(root, text = "Go back", command = begin).pack(side = BOTTOM)
def Human1():
    global temp2
    temp2 = []
    global times
    times = 1
    Humancalc()
def Human2():
    global temp2
    temp2 = []
    global times
    times = 10
    Humancalc()
def Humancalc():
    # Setup
    listA = [
        "Jacob","Emily",
    "Michael","Madison",
    "Joshua","Hannah",
    "Matthew","Emma",
    "Andrew","Ashley",
    "Christopher","Alexis",
    "Joseph","Samantha",
    "Nicholas","Sarah",
    "Daniel","Abigail",
    "William","Olivia",
    "Ethan","Elizabeth",
    "Anthony","Alyssa",
    "Ryan","Jessica",
    "Tyler","Grace",
    "David","Lauren",
    "John","Taylor",
    "Alexander"	"Kayla",
    "James","Brianna",
    "Zachary","Isabella",
    "Brandon","Anna",
    "Jonathan","Victoria",
    "Dylan","Sydney",
    "Justin","Megan",
    "Christian","Rachel",
    "Samuel","Jasmine",
    "Benjamin","Natalie",
    "Austin","Sophia",
    "Nathan","Chloe",
    "Noah","Morgan",
    "Jose","Hailey",
    "Logan","Jennifer",
    "Robert","Destiny",
    "Kevin","Julia",
    "Thomas","Kaitlyn",
    "Gabriel","Haley",
    "Caleb","Katherine",
    "Jordan","Nicole",
    "Hunter","Alexandra",
    "Cameron","Savannah",
    "Kyle","Maria",
    "Jason","Amanda",
    "Elijah","Mackenzie",
    "Aaron","Stephanie",
    "Jack","Allison",
    "Connor","Mia",
    "Isaiah","Brooke",
    "Luke","Jordan",
    "Isaac","Jenna",
    "Evan","Rebecca",
    "Eric","Mary",
    "Brian","Makayla",
    "Angel","Faith",
    "Juan","Andrea",
    "Adam","Katelyn",
    "Jackson","Paige",
    "Mason","Madeline",
    "Luis","Gabrielle",
    "Charles","Michelle",
    "Sean","Kaylee",
    "Aidan","Sara",
    "Gavin","Kimberly",
    "Alex","Amber",
    "Nathaniel","Trinity",
    "Bryan","Zoe",
    "Carlos","Caroline",
    "Steven","Sierra",
    "Ian","Ava",
    "Hayden","Breanna",
    "Diego","Melanie",
    "Carson","Mariah",
    "Colin","Jade",
    "Riley","Katie",
    "Wyatt","Briana",
    "Kenneth","Arianna",
    "Carter","Diana",
    "Tanner","Evelyn",
    "Aiden","Kathryn",
    "Dakota","Laura",
    "Tristan","Alexandria",
    "Marcus","Sofia",
    "Jorge","Amy",
    "Stephen","Gabriela",
    "Henry","Caitlin",
    "Dalton","Kelsey",
    "Paul","Isabelle",
    "Spencer","Angel",
    "Liam","Madelyn",
    "Vincent","Avery",
    "Kaleb","Lindsey",
    "Edward","Kelly",
    "Oscar","Margaret",
    "Joel","Cheyenne",
    "Eduardo","Sabrina",
    "Landon","Mikayla",
    "Brendan","Adriana",
    "Parker","Alicia",
    "Colton","Cassandra",
    "Maxwell","Daniela",
    "Jeffrey","Cassidy",
    "Grant","Jillian",
    "Alexis","Kennedy",
    "George","Brittany",
    "Ivan","Miranda",
    "Collin","Tiffany",
    "Shane","Ana",
    "Peter","Lydia",
    "Brayden","Erica",
    "Ashton","Mya",
    "Nicolas","Brooklyn",
    "Derek","Amelia",
    "Ricardo","Alexia",
    "Jalen","Daisy",
    "Travis","Mckenzie",
    "Francisco","Caitlyn",
    "Alan","Skylar",
    "Caden","Summer",
    "Gage","Angelica",
    "Omar","Crystal",
    "Cristian","Sophie",
    "Preston","Karen",
    "Bradley","Gracie",
    "Shawn","Ashlyn",
    "Brady","Kiara",
    "Devon","Erika",
    "Fernando","Hope",
    "Colby","Gianna",
    "Erik","Bianca",
    "Javier","Heather",
    "Kaden","Veronica",
    "Josiah","Valerie",
    "Andres","Chelsea",
    "Max","Natalia",
    "Cesar","Kylee",
    "Manuel","Karina",
    "Gregory","Alondra",
    "Levi","Naomi",
    "Mario","Jordyn",
    "Johnathan","Jamie",
    "Edgar","Meghan",
    "Conner","Peyton",
    "Mitchell","Abby",
    "Clayton","Payton",
    "Nolan","Juliana",
    "Micah","Kendall",
    "Damian","Bethany",
    "Raymond","Carly",
    "Braden","Cynthia",
    "Jonah","Kate",
    "Taylor","Hayley",
    "Cooper","Delaney",
    "Trenton","Kristen",
    "Wesley","Jasmin",
    "Corey","Monica",
    "Edwin","Karla",
    "Dustin","Alejandra",
    "Dillon","Mckenna",
    "Scott","Shannon",
    "Erick","Maggie",
    "Peyton","Rylee",
    "Emmanuel","Kyla",
    "Marco","Nevaeh",
    "Sergio","Valeria",
    "Dawson","Hanna",
    "Martin","Brenda",
    "Hector","Julianna",
    "Giovanni","Diamond",
    "Roberto","Michaela",
    "Donovan","Reagan",
    "Eli","Aubrey",
    "Brett","Esmeralda",
    "Alec","Makenzie",
    "Jakob","Giselle",
    "Abraham","Jazmin",
    "Harrison","Rebekah",
    "Andre","Ariel",
    "Andy","Ruby",
    "Malik","Desiree",
    "Drew","Lizbeth",
    "Ruben","Charlotte",
    "Ty","Sadie",
    "Damien","Kaitlin",
    "Jaylen","Adrianna",
    "Cade","Kyra",
    "Pedro","Jayla",
    "Calvin","Genesis",
    "Elias","Alana",
    "Josue","Addison",
    "Leonardo","Mallory",
    "Frank","Britney",
    "Malachi","Nadia",
    "Phillip","Amaya",
    "Ronald","Kara",
    "Chandler","Elena",
    "Trey","Julie",
    "Bryson","Camryn",
    "Gerardo","Lindsay",
    "Skyler","Kendra",
    "Chance","Macy",
    "Rafael","Aliyah",
    "Trent","Claudia",
    "Casey","Alison",
    "Zane","Ellie",
    "Griffin","Elise",
    "Avery","Holly",
    "Dominick","Eva",
    "Derrick","Selena",
    "Miles","Joanna",
    "Raul","Jazmine",
    "Johnny","Raven",
    "Israel","Savanna",
    "Armando","Nina",
    "Darius","Haylee",
    "Troy","Makenna",
    "Enrique","Mariana",
    "Donald","Fatima",
    "Keith","Allyson",
    "Marcos","Asia",
    "Payton","Guadalupe",
    "Allen","Katelynn",
    "Simon","Cameron",
    "Dante","Nancy",
    "Jaime","Serena",
    "Zackary","Layla",
    "Julio","Vivian",
    "Brock","Lucy",
    "Kobe","April",
    "Brenden","Liliana",
    "Keegan","Kathleen",
    "Drake","Camille",
    "Lance","Brittney",
    "Oliver","Josephine",
    "Kameron","Katrina",
    "Jonathon","Carmen",
    "Mathew","Cierra",
    "Brody","Kailey",
    "Alberto","Sandra",
    "Gustavo","Carolina",
    "Philip","Celeste",
    "Jace","Cindy",
    "Jimmy","Tatiana",
    "Fabian","Kristina",
    "Dennis","Jaden",
    "Jerry","Kirsten",
    "Marc","Cecilia",
    "Cory","Zoey",
    "Brennan","Skyler",
    "Ayden","Patricia",
    "Louis","Serenity",
    "Angelo","Casey",
    "Camden","Yesenia",
    "Corbin","Tessa",
    "Saul","Wendy",
    "Danny","Kira",
    "Kyler","Anastasia",
    "Roman","Rachael",
    "Curtis","Miriam",
    "Tucker","Heaven",
    "Myles","Christine",
    "Bailey","Bridget",
    "Chad","Tara",
    "Tony","Priscilla",
    "Arturo","Alaina",
    "Pablo","Tori",
    "Damon","Kassandra",
    "Randy","Alissa",
    "Lane","Natasha",
    "Gary","Madeleine",
    "Braxton","Mercedes",
    "Douglas","Josie",
    "Kai","Lauryn",
    "Albert","Esther",
    "Grayson","Jayden",
    "Larry","Lilly",
    "Nickolas","Dakota",
    "Emanuel","Paris",
    "Quinn","Kayleigh",
    "Lorenzo","Clara",
    "Darren","Sidney",
    "Alfredo","Kiana",
    "Theodore","Nayeli",
    "Bryant","Shayla",
    "Tyson","Brenna",
    "Axel","Paola",
    "Zion","Alexus",
    "Leo","Marisa",
    "Joe","Melody",
    "Lukas","Imani",
    "Santiago","Denise",
    "Tristen","Nia",
    "Emilio","Emilee",
    "Jaxon","Ciara",
    "Kristopher","Logan",
    "Ramon","Rose",
    "Ismael","Ashanti",
    "Ricky","Meredith",
    "Russell","Annie",
    "Arthur","Ashlee",
    "Zachery","Bryanna",
    "Moises","Callie",
    "Salvador","Kamryn",
    "Jay","Eleanor",
    "Carl","Anne",
    "Ernesto","Heidi",
    "Quentin","Ashlynn",
    "Jayson","Ashleigh",
    "Walter","Annabelle",
    "Ezekiel","Ruth",
    "Micheal","Clarissa",
    "Esteban","Daniella",
    "Dallas","Julissa",
    "Nikolas","Dominique",
    "Lawrence","Laila",
    "Morgan","Annika",
    "Marvin","Allie",
    "Tommy","Dana",
    "Maximilian","Kassidy",
    "Mateo","Lisa",
    "Deandre","Eliza",
    "Marshall","Harley",
    "Abel","Rosa",
    "Isiah","Whitney",
    "Ali","Helen",
    "Brent","Hallie",
    "Jaiden","Cristina",
    "Camron","Shania",
    "Braeden","Anahi",
    "Reece","Kaylie",
    "Maurice","Marina",
    "Jeffery","Talia",
    "Terry","Kristin",
    "Cayden","Jadyn",
    "Amir","Carolyn",
    "Keaton","Alayna",
    "Branden","Deanna",
    "Jarrett","Georgia",
    "Eddie","India",
    "Dean","Yasmin",
    "Mauricio","Tabitha",
    "Orlando","Elisabeth",
    "Rodney","Fiona",
    "Davis","Piper",
    "Jon","Tiana",
    "Justice","Ivy",
    "Xander","Aniya",
    "Brayan","Halle",
    "Rodrigo","Raquel",
    "Jamal","Teresa",
    "Hugo","Hailee",
    "Kody","Madalyn",
    "Felix","Emely",
    "Kade","Jayda",
    "Shaun","Eden",
    "Roger","Linda",
    "Chris","Jenny",
    "Conor","Jaqueline",
    "Skylar","Krystal",
    "Reese","Lesly",
    "Trevon","Iris",
    "Craig","Virginia",
    "Maximus","Lexi",
    "Zachariah","Gillian",
    "Weston","Gloria",
    "Javon","Tatum",
    "Adan","Marisol",
    "Brendon","Perla",
    "Kelvin","Sasha",
    "Charlie","Monique",
    "Walker","Baylee",
    "Melvin","Kiley",
    "Bobby","Kaitlynn",
    "Graham","Aurora",
    "Guillermo","Eliana",
    "Quinton","Angie",
    "Landen","Camila",
    "Tyrese","Nora",
    "Julius","Lacey",
    "Billy","Katlyn",
    "Zackery","Bella",
    "Demetrius","Haleigh",
    "Issac","Leilani",
    "Holden","Alivia",
    "Ezra","Francesca",
    "Jaylon","Tamia",
    "Desmond","Destinee",
    "Frederick","Renee",
    "Nelson","Ashton",
    "Tate","Noelle",
    "Khalil","Paulina",
    "Dorian","Deja",
    "Rene","Aniyah",
    "Jessie","Phoebe",
    "Zander","Regan",
    "Aden","Alisha",
    "Johnathon","Viviana",
    "Jaylin","Ayanna",
    "Gerald","Sage",
    "Felipe","Gina",
    "Reginald","Madisyn",
    "Elliot","Carla",
    "Roy","Leila",
    "Ahmad","Alina",
    "Steve","Reese",
    "Kolby","Alice",
    "Malcolm","Kaleigh",
    "Jadon","Genevieve",
    ]
    # too many names? i think not!
    for i in range(times):
        # Generation
        temp = listA[random.randint(0, len(listA))]
        global temp2
        temp2.append(temp)
    temp2 = "\n".join(temp2)
    Human()

root = Toplevel()
root.geometry("400x300")
root.title("NameGenerator")
btn1 = Button(root, text = "Generate me some names!", command = begin)
btn1.pack()
root.mainloop()