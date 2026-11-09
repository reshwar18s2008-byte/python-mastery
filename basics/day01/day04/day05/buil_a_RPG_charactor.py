def create_character(name, strength, intelligence, charisma):

    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats
    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) and not isinstance(stat, bool) for stat in stats):
        return "All stats should be integers"

    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Create character stats
    def create_bar(abbreviation, value):
        return abbreviation + " " + "●" * value + "c" * (10 - value)

    return (
        name + "\n" +
        create_bar("STR", strength) + "\n" +
        create_bar("INT", intelligence) + "\n" +
        create_bar("CHA", charisma)
    )


# Test
print(create_character("ren", 4, 2, 1))