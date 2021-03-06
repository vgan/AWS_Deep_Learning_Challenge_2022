import random
def generateText():
    style = random.choice([
        "a charcoal drawing",
        "a line drawing",
        "a vintage black velvet painting",
        "a vintage oil painting",
        "a watercolor painting",
        "Abstract",
        "Anime",
        "Art Deco",
        "Art Nouveau",
        "Aztec",
        "Constructivism",
        "Cubism",
        "Clay Animation",
        "Clay Animation",
        "Clay Animation",
        "Clay Animation",
        "Dadaism",
        "Dali",
        "Expressionism",
        "Geometric",
        "Gothic",
        "H.R. Giger",
        "Hieronymus Bosch",
        "Impressionism",
        "Matisse",
        "Mayan",
        "Michelangelo",
        "minimalist",
        "Moebius",
        "Moebius",
        "Moebius",
        "Moebius",
        "Moebius",
        "Monet",
        "Picasso",
        "Pop Art",
        "Realism",
        "Retro-Futurism",
        "Roger Dean",
        "Social Realism",
        "Socialist Realism",
        "Still Life",
        "Surrealist",
        "Symbolism",
        "Ukiyo-E",
        "Van Gogh",
        "vaporwave",
        "1970s airbrushed space",
        "1980s airbrushed knight",
        "plants in a greenhouse",
        "1970s fantasy airbrushed",
        "1960s modernist church interior",
        "1960s brutalist church interior",
        "1960s brutalist corridor",
        "1960s brutalist hotel",
        "1960s brutalist hotel |plants"
        ])

    subject = random.choice([
        "a bear",
        "a blacksmith",
        "a cat",
        "a clown",
        "a cow",
        "a cowboy",
        "a crow",
        "a dragon",
        "a frog",
        "a ghost",
        "a hammer",
        "a hamster",
        "a little girl",
        "a magician",
        "a man",
        "a mindmill",
        "a moose",
        "a mouse",
        "a Muppet",
        "a parade",
        "a robot",
        "a shiba inu",
        "a space station",
        "a squirrel",
        "a sword",
        "a tardigrade",
        "a treasure chest",
        "a vacuum cleaner"
        "a volcano",
        "a Wienermobile",
        "a wizard",
        "album cover",
        "an alien",
        "an elf",
        "angels",
        "bank robbers",
        "bees",
        "beetles",
        "bones",
        "bookshelves",
        "bridges",
        "buddah",
        "camels",
        "carnivorous plants",
        "cats",
        "cavemen",
        "chupacabra",
        "circuitry",
        "clocks",
        "coffins",
        "deep sea fish",
        "demons",
        "detectives ",
        "dogs",
        "dumptrucks",
        "elves",
        "elvis",
        "fancy jewelry",
        "ferns",
        "ghosts",
        "giraffes",
        "goblins",
        "god",
        "godzilla",
        "hackers",
        "handcuffs",
        "jellyfish",
        "lizard men",
        "lobsters",
        "luigi",
        "mad scientists",
        "mariachis",
        "monsters",
        "muffins",
        "mutants",
        "nuclear explosion",
        "pancakes",
        "Pyramids",
        "raccoons",
        "satan",
        "scarabs",
        "scorpions",
        "sea shells",
        "sharks",
        "shiva",
        "skiers",
        "skunks",
        "smartphones",
        "snakes"
        "Snoopy",
        "super mario",
        "sushi",
        "tacos",
        "teenagers",
        "tentacles",
        "the devil",
        "the pope",
        "tigers",
        "time travelers",
        "tombstones",
        "tractors",
        "trains",
        "Transformers",
        "turkeys",
        "UFO abduction",
        "UFOs",
        "umbrellas",
        "yggdrasil world tree"
        ])

    modifier = random.choice([
        "|abandoned",
        "|after the rain",
        "|autumn",
        "|black and white",
        "|blue tint",
        "|crystal matrix",
        "|dark",
        "|dim",
        "|doom",
        "|dry",
        "|earth tones",
        "|faded",
        "|fall",
        "|foggy",
        "|futuristic",
        "|glowing",
        "|green tint",
        "|heavy rain",
        "|high contrast",
        "|illuminated",
        "|morning",
        "|neon",
        "|neon glowing",
        "|night",
        "|pastels",
        "|rainbow",
        "|rainbow doom",
        "|shining",
        "|shiny",
        "|spooky",
        "|stained glass",
        "|sunrise",
        "|sunset",
        "|wet",
        "|winter",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""])

    scene = random.choice([
        "at a concert",
        "at a dinner party",
        "at a dive bar",
        "at a grassy field",
        "at a pachinko parlor",
        "at a pool party",
        "at the circus",
        "at the gates of heaven",
        "at the gates of hell",
        "at the gates of valhalla",
        "at the great pyramids",
        "at the mall",
        "by a creek",
        "in a barn",
        "hubble HD wallpaper",
        "in a black hole",
        "in a castle",
        "in a cavern",
        "in a datacenter",
        "in a desert",
        "in a diner",
        "in a factory",
        "in a gothic cathedral",
        "in a graveyard",
        "in a hidden tunnel",
        "in a jungle",
        "in a medieval castle",
        "in a post-apocalyptic city",
        "in a secret passage",
        "in a swamp",
        "in an arcade",
        "in ancient Egypt",
        "in ancient Greece",
        "in ancient rome",
        "in Athens",
        "in Bangkok",
        "in Belgrade",
        "in Bishkek",
        "in Bombay",
        "in Bucharest",
        "in Buenos Aires",
        "in Caracas",
        "in Ethiopia",
        "in Havana",
        "in Helsinki",
        "in Hollywood",
        "in Istanbul",
        "in Krakow",
        "in Kyiv",
        "in Las Vegas",
        "in Medellin",
        "in Mexico City",
        "in Minsk",
        "in Montevideo",
        "in Odessa",
        "in Paris",
        "in Prague",
        "in Saigon",
        "in Samara Russia",
        "in Sao Paolo",
        "in Shanghai",
        "in Siberia",
        "in Sintra",
        "in Skopje",
        "in soviet russia",
        "in space",
        "in Taipei",
        "in Tallinn",
        "in Tashkent",
        "in Tbilisi",
        "in the city",
        "in the countryside",
        "in the metro",
        "in the mountains",
        "in the ocean",
        "in Tokyo",
        "in Ulaanbaatar",
        "inside a machine",
        "lakeside resort",
        "on a battleship",
        "on a cloud",
        "on a cruiseship",
        "on a farm",
        "on a pier",
        "on a ship",
        "on a train",
        "on a tropical island",
        "on an island",
        "on Mars",
        "on the beach",
        "on the Moon"
        ])
    place = random.choice([
        "a barn",
        "a black hole",
        "a castle",
        "a cavern",
        "a datacenter",
        "a desert",
        "a diner",
        "a dinner party",
        "a factory",
        "a Galaxy",
        "a gothic cathedral",
        "a grassy field",
        "a graveyard",
        "a hidden tunnel",
        "a jungle",
        "a medieval castle",
        "a pachinko parlor",
        "a pool party",
        "a post-apocalyptic city",
        "a secret passage",
        "a swamp",
        "an arcade",
        "ancient Egypt",
        "ancient Greece",
        "ancient rome",
        "Athens",
        "banff national park",
        "Bangkok",
        "Belgrade",
        "Bishkek",
        "Bombay",
        "Bucharest",
        "Buenos Aires",
        "by a creek",
        "Caracas",
        "Constructivist Architecture",
        "cycberspace",
        "Ethiopia",
        "glacier national park",
        "Havana",
        "Helsinki",
        "Hollywood",
        "in the ocean",
        "inside a machine",
        "Istanbul",
        "Kowloon City",
        "Krakow",
        "Kyiv",
        "lakeside resort",
        "Las Vegas",
        "Medellin",
        "Metabolist Architecture",
        "Mexico City",
        "Minsk",
        "Modernist Architecture",
        "Montevideo",
        "Odessa",
        "on a battleship",
        "on a cloud",
        "on a cruiseship",
        "on a farm",
        "on a pier",
        "on a ship",
        "on a train",
        "on a tropical island",
        "on an island",
        "on Mars",
        "on stage at a concert",
        "on the beach",
        "on the Moon",
        "Organic Brutalist Architecture",
        "Paris",
        "Postmodernist Architecture",
        "Prague",
        "Saigon",
        "Samara Russia",
        "Sao Paolo",
        "Shanghai",
        "Siberia",
        "Sintra",
        "Skopje",
        "soviet russia",
        "Taipei",
        "Tallinn",
        "Tangier",
        "Tashkent",
        "Tbilisi",
        "the circus",
        "the city",
        "the countryside",
        "the gates of heaven",
        "the gates of hell",
        "the gates of valhalla",
        "the great pyramids",
        "the Interzone",
        "the mall",
        "the metro",
        "the mountains",
        "the north pole",
        "Tokyo",
        "Ulaanbaatar",
        "yosemite national park",
        "zion national park"
        ])

    preset_scene = random.choice([
        "1960s brutalist church interior",
        "1960s brutalist corridor",
        "1960s brutalist hotel",
        "1960s brutalist hotel |plants",
        "1960s modernist church interior",
        "1970s airbrushed tiger",
        "1970s dragon airbrushed",
        "1980s airbrushed fantasy movie poster",
        "1980s airbrushed galaxy",
        "1980s airbrushed knight",
        "1980s airbrushed space",
        "1980s shakeys pizza restaurant",
        "1990s taco bell dining area",
        "a space garden",
        "a surfer on a wave airbrushed",
        "album cover airbrushed",
        "black metal album cover |evil",
        "Electron Microscope dust mites",
        "Electron Microscope spores",
        "Electron Microscope tardigrade",
        "Electron Microscope virus",
        "plants in a greenhouse at sunset",
        "unusual roadside attraction|japan|weird",
        "unusual roadside attraction|route 66",
        "unusual roadside attraction|weird",
        "very long motel hallway"
        ])
    # define prompt templates    
    sub_scene_style_mod = [subject,scene,"in the style of",style,modifier]
    sub_scene_style = [subject,scene,"in the style of",style]
    place_style_mod =[place,"in the style of",style,modifier]
    place_style = [place,"in the style of",style]
    preset = [preset_scene]

    template = random.choice([preset,sub_scene_style_mod,sub_scene_style,place_style_mod,place_style])

    text = template
    return text
