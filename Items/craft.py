class Item():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        damage_die = 0,
        armor_bonus = 0,
        effect = "No effect",
        wieldable = False,
        wearable_on_head = False,
        wearable_on_torso = False,
        wearable_on_legs = False,
        wearable_on_feet = False,
        wearable_on_hands = False,
    ):
        self.name = name
        self.description = description
        self.damage_die = damage_die
        self.armor_bonus = armor_bonus
        self.effect = effect
        self.wieldable = wieldable
        self.wearable_on_head = wearable_on_head
        self.wearable_on_torso = wearable_on_torso
        self.wearable_on_legs = wearable_on_legs
        self.wearable_on_feet = wearable_on_feet
        self.wearable_on_hands = wearable_on_hands