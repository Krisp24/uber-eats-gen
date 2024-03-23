from random import choice, randint, choices

rand_first_names = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
    "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth",
    "Joshua", "George", "Kevin", "Brian", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
    "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon",
    "Frank", "Benjamin", "Gregory", "Samuel", "Raymond", "Patrick", "Alexander", "Jack", "Dennis", "Jerry",
    "Tyler", "Aaron", "Jose", "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary", "Kyle",
    "Walter", "Harold", "Jeremy", "Ethan", "Carl", "Keith", "Roger", "Gerald", "Christian", "Terry",
    "Sean", "Arthur", "Austin", "Noah", "Lawrence", "Jesse", "Joe", "Bryan", "Billy", "Jordan",
    "Albert", "Dylan", "Bruce", "Willie", "Gabriel", "Alan", "Juan", "Logan", "Wayne", "Ralph",
    "Roy", "Eugene", "Randy", "Vincent", "Russell", "Louis", "Philip", "Bobby", "Johnny", "Bradley",
    "Alberto", "Howard", "Leonard", "Elijah", "Curtis", "Victor", "Martin", "Luis", "Theodore", "Trevor",
    "Travis", "Alex", "Oscar", "Earl", "Nathaniel", "Marvin", "Shawn", "Leroy", "Fernando", "Casey",
    "Caleb", "Ronnie", "Tommy", "Derrick", "Jon", "Aiden", "Cory", "Calvin", "Clinton", "Jesus",
    "Cole", "Cameron", "Blake", "Colin", "Geoffrey", "Mitchell", "Carlton", "Marc", "Joel", "Roland",
    "Dustin", "Mitchell", "Byron", "Bernard", "Darren", "Jeremiah", "Alfred", "Joey", "Ricky", "Allan",
    "Jay", "Jonathon", "Edwin", "Brent", "Tony", "Kelly", "Clarence", "Owen", "Derek", "Darrell",
    "Ted", "Vincent", "Sam", "Max", "Everett", "Jordan", "Brendan", "Malcolm", "Tristan", "Seth",
    "Evan", "Gilbert", "Clifford", "Dennis", "Levi", "Dwayne", "Ramon", "Terrance", "Stanley", "Don",
    "Conrad", "Stuart", "Eduardo", "Maxwell", "Damon", "Russell", "Cesar", "Drew", "Kurt", "Cory",
    "Fred", "Lance", "Mathew", "Fredrick", "Tyrone", "Darren", "Preston", "Lorenzo", "Brad", "Antonio",
    "Malachi", "Eli", "Ben", "Oliver", "Jake", "Miles", "Wesley", "Micah", "Leo", "Axel",
    "Jasper", "Emmanuel", "Dean", "Kai", "Bennett", "Jared", "Griffin", "River", "Phoenix", "Nico",
    "Damien", "Julian", "August", "Beckett", "Finn", "Graham", "Arthur", "Theo", "Dexter", "Hugo",
    "Gideon", "Knox", "Kieran", "Luka", "Ronan", "Simon", "Sullivan", "Tobias", "Atticus", "Ezekiel",
    "Cassius", "Felix", "Killian", "Cyrus", "Milo", "Orion", "Titus", "Zane", "Cairo", "Enzo",
    "Caspian", "Lennon", "Romeo", "Canaan", "Hendrix", "Jonas", "Callum", "Leonidas", "Soren", "Alaric",
    "Dorian", "Cohen", "Reign", "Zephyr", "Bodhi", "Atlas", "Maverick", "Kyrie", "Zayn", "Bear",
    "Orlando", "Mekhi", "Axl", "Cyril", "Keanu", "Ocean", "Kaius", "Lorcan", "Arian", "Dimitri",
    "Keegan", "Zaire", "Brecken", "Castiel", "Lucian", "Aries", "Caspian", "Rhys", "Zahir", "Daxton",
    "Landyn", "Khalil", "Dangelo", "Ermias", "Zaiden", "Devon", "Kenzo", "Bishop", "Rohan", "Armando",
    "Wesson", "Kingsley", "Yadiel", "Jaxtyn", "Lian", "Jagger", "Omarion", "Rodrigo", "Ahmad", "Lyle",
    "Forrest", "Aarav", "Asa", "Keaton", "Harry", "Koa", "Yahir", "Marley", "Santos", "Alden",
    "Ameer", "Vivaan", "Bode", "Koda", "Kace", "Vance", "Jabari", "Thaddeus", "Tadeo", "Xander",
    "Maxim", "Cairo", "Nikolai", "Emerald", "Demetrius", "Davian", "Jayceon", "Koen", "Aarush", "Jovanni",
    "Merrick", "Abdullah", "Taison", "Giancarlo", "Jovani", "Yousef", "Musa", "Aayan", "Thatcher", "Shia",
    "Zakai", "Briggs", "Brixton", "Kalani", "Kamari", "Alvaro", "Davion", "Randall", "Benicio", "Aldo",
    "Van", "Harris", "Rodney", "Dayton", "Huxley", "Jet", "Joziah", "Marcelo", "Miller", "Chaim",
    "Crosby",
]


rand_last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
    "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
    "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
    "Harrison", "Fernandez", "McDonald", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen",
    "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter",
    "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks",
    "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox",
    "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens",
    "Soto", "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins",
    "Arnold", "Pierce", "Vazquez", "Hansen", "Peters", "Santos", "Hart", "Bradley", "Knight", "Elliott",
    "Cunningham", "Duncan", "Armstrong", "Hudson", "Carroll", "Lane", "Riley", "Andrews", "Alvarado", "Ray",
    "Delgado", "Berry", "Perkins", "Hoffman", "Johnston", "Matthews", "Pena", "Richards", "Contreras", "Willis",
    "Carpenter", "Lawrence", "Sandoval", "Guerrero", "George", "Chapman", "Rios", "Estrada", "Ortega", "Watkins",
    "Greene", "Nunez", "Wheeler", "Valdez", "Harper", "Burke", "Larson", "Santiago", "Maldonado", "Morrison",
    "Franklin", "Carlson", "Austin", "Dominguez", "Carr", "Lawson", "Jacobs", "Obrien", "Lynch", "Singh",
    "Vega", "Bishop", "Montgomery", "Oliver", "Jensen", "Harvey", "Williamson", "Gilbert", "Dean", "Sims",
    "Espinoza", "Howell", "Li", "Wong", "Reid", "Hanson", "Le", "McCoy", "Garrett", "Burton",
    "Fuller", "Wang", "Weber", "Welch", "Rojas", "Lucas", "Marquez", "Fields", "Park", "Yang",
    "Little", "Banks", "Padilla", "Day", "Walsh", "Bowman", "Schultz", "Luna", "Fowler", "Mejia",
    "Davidson", "Acosta", "Brewer", "May", "Holland", "Juarez", "Newman", "Pearson", "Curtis", "Cortez",
    "Douglas", "Schneider", "Joseph", "Barrett", "Navarro", "Figueroa", "Keller", "Avila", "Wade", "Molina",
    "Stanley", "Hopkins", "Campos", "Barnett", "Bates", "Chambers", "Caldwell", "Beck", "Lambert", "Miranda",
    "Byrd", "Craig", "Ayala", "Lowe", "Frazier", "Powers", "Neal", "Leonard", "Gregory", "Carrillo",
    "Sutton", "Fleming", "Rhodes", "Shelton", "Schwartz", "Norris", "Jennings", "Watts", "Duran", "Walters",
    "Cohen", "Mills", "Nicholson", "Gates", "Lloyd", "Manning", "Stanley", "Bryant", "Harvey", "Kim",
    "Lucas", "Li", "Gates",
]

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def first_name_gen():
    return choice(rand_first_names)

def last_name_gen():
    return choice(rand_last_names)

def rand_email_gen(fname, lname, domain):
    rand_email = f"{fname}{lname}{"".join(choices(alphabet, k=10))}{randint(0, 100)}{domain}"
    return rand_email