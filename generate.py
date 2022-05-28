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

class NPC():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        hit_die = 0,
        current_hp = 0,
        max_hp = 0,
        inventory = [],
        equipped_items = [],
        spells = [],
        is_alive = True,
        held_dominant_hand = None,
        held_off_hand = None,
        worn_head = None,
        worn_torso = None,
        worn_legs = None,
        worn_feet = None,
        worn_dominant_hand = None,
        worn_off_hand = None,
        conversation_topics = {},
    ):
        self.name = name
        self.description = description
        self.hit_die = hit_die
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.inventory = inventory
        self.equipped_items = equipped_items
        self.spells = spells
        self.is_alive = is_alive
        self.held_dominant_hand = held_dominant_hand
        self.held_off_hand = held_off_hand
        self.worn_head = worn_head
        self.worn_torso = worn_torso
        self.worn_legs = worn_legs
        self.worn_feet = worn_feet
        self.worn_dominant_hand = worn_dominant_hand
        self.worn_off_hand = worn_off_hand
        self.conversation_topics = conversation_topics

class Room():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        accessible_rooms = [],
        item_contents = [],
        NPC_contents = [],
    ):
        self.name = name
        self.description = description
        self.accessible_rooms = accessible_rooms
        self.item_contents = item_contents
        self.NPC_contents = NPC_contents