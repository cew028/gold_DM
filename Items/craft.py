class Item():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        damage_die = 0,
        armor_bonus = 0,
        effect = "No effect",
        two_handed = False,
        holdable_dominant_hand = False,
        holdable_off_hand = False,
        wearable_head = False,
        wearable_torso = False,
        wearable_legs = False,
        wearable_feet = False,
        wearable_dominant_hand = False,
        wearable_off_hand = False,
        equipped = False,
    ):
        self.name = name
        self.description = description
        self.damage_die = damage_die
        self.armor_bonus = armor_bonus
        self.effect = effect
        self.two_handed = two_handed
        self.holdable_dominant_hand = holdable_dominant_hand
        self.holdable_off_hand = holdable_off_hand
        self.wearable_head = wearable_head
        self.wearable_torso = wearable_torso
        self.wearable_legs = wearable_legs
        self.wearable_feet = wearable_feet
        self.wearable_dominant_hand = wearable_dominant_hand
        self.wearable_off_hand = wearable_off_hand
        self.equipped = equipped