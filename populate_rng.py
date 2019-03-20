import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RNG_project.settings')
import django
django.setup()
from RNG.models import Category, Game, Rating, UserProfile

def populate():
    #creates a list of dictionaries containing games to add into each category
    action=[
        {"name": "Assassin's Creed 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"name": "Grand Theft Auto V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18},
        {"id": "DISH",
        "name": "Dishonored",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    rpg=[
        {"name": "Skyrim",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15},
        {"name": "Mass Effect 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 15},
        {"id": "DAI",
        "name": "Dragon Age: Inquisition",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 18}
    ]
    strategy=[
        {"name": "DOTA 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 16},
        {"name": "Civilization V",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"name": "Spore",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    puzzle=[
        {"name": "Portal 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"name": "The Talos Principle",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"name": "The Witness",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    sports=[
        {"name": "Rocket League",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"name": "Fifa 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"name": "NBA 2K19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3}
    ]
    mmo=[
        {"name": "World Of Warcraft",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"name": "Elder Scrolls Online",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12},
        {"name": "Guild Wars 2",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 12}
    ]
    simulation=[
        {"name": "The Sims 4",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"name": "Kerbal Space Program",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3},
        {"name": "Farming Simulator 19",
        "user_score": 5,
        "num_user_ratings": 5,
        "critic_score": 5,
        "num_critic_ratings": 5,
        "age_rating": 3}
    ]

    # cats={"Action":{"games":action, "reviews":0},
    #     "RPG":{"games":rpg, "reviews":0},
    #     "Strategy":{"games":strategy, "reviews":0},
    #     "Puzzle":{"games":puzzle, "reviews":0},
    #     "Sports":{"games":sports, "reviews":0},
    #     "MMO":{"games":mmo, "reviews":0},
    #     "Simulation":{"games":simulation, "reviews":0},
    # }
    
    # maintained dict structure here in case we want to add supercategories
    cats = {"Action":action,
            "RPG":rpg,
            "Strategy":strategy,
            "Puzzle":puzzle,
            "Sports":sports,
            "MMO":mmo,
            "Simulation":simulation,
    }

    def add_game(cat, name, age_rating):
        # [0] specifies object in the [object, boolean created]
        p = Game.objects.get_or_create(category=cat, name=name, age_rating=age_rating)[0]
        p.save()
        return p

    def add_cat(name):
        c=Category.objects.get_or_create(name=name)[0]
        c.save()
        return c

    # for cat, cat_data in cats.items():
    #     c=add_cat(cat, cats[cat]["views"]["likes"])
    #     for p in cat_data["games"]:
    #         add_game(c,p["name"],p["url"],p["views"])
    
    for name, games in cats.items():
        cat = add_cat(name)
        for game in games:
            add_game(cat, name=game["name"], age_rating=game["age_rating"])
    
    for c in Category.objects.all():
        for p in Game.objects.filter(category=c):
            print("- {0} - {1}".format(str(c),str(p)))


if __name__ == '__main__':
    print("*** Starting RNG population script ***")
    populate()
