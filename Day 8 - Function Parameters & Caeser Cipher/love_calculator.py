def calculate_love_score(name1, name2):
    names = name1.lower() + name2.lower()

    score1 = names.count("t") + names.count("r") + names.count("u") + names.count("e")
    score2 = names.count("l") + names.count("o") + names.count("v") + names.count("e")

    print(f"{score1}{score2}")


calculate_love_score("Jason Fernandez", "Kim Ysabel")