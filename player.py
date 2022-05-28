import dice
import draw
import prompt

gold_to_reach_level = {
    # next level : cost to get there
    2 : 500,
    3 : 1000,
    4 : 2000,
    5 : 4000,
    6 : 8000,
    7 : 16000,
    8 : 32000,
    9 : 64000,
    10 : 128000,
}

class Player():
    def __init__(
        self,
        name = "Unnamed",
        character_class = "None",
        die = 0,
        max_weapon_die = 0,
        max_armor = "None",
        max_shield = "None",
        level = -1,
        AV_by_level = [],
        CHA = 0,
        CON = 0,
        DEX = 0,
        INT = 0,
        STR = 0,
        WIS = 0,
        current_hp = 0,
        max_hp = 0,
        gold_on_person = 0,
        gold_stored_away = 0,
        gold_spent_this_level = 0,
        gold_to_next_level = 0,
        inventory = [],
        equipped_items = [],
        spells = [],
        spellcasting_stat = "None",
        spell_list = "None",
        abilities = [],
        are_alive = True,
        location = None,
        held_dominant_hand = None,
        held_off_hand = None,
        worn_head = None,
        worn_torso = None,
        worn_legs = None,
        worn_feet = None,
        worn_dominant_hand = None,
        worn_off_hand = None,
    ):
        self.name = name
        self.character_class = character_class
        self.die = die
        self.max_weapon_die = max_weapon_die
        self.max_armor = max_armor
        self.max_shield = max_shield
        self.level = level
        self.AV_by_level = AV_by_level
        self.CHA = CHA
        self.CON = CON
        self.DEX = DEX
        self.INT = INT
        self.STR = STR
        self.WIS = WIS
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.gold_on_person = gold_on_person
        self.gold_stored_away = gold_stored_away
        self.gold_spent_this_level = gold_spent_this_level
        self.gold_to_next_level = gold_to_next_level
        self.inventory = inventory
        self.equipped_items = equipped_items
        self.spells = spells
        self.spellcasting_stat = spellcasting_stat
        self.spell_list = spell_list
        self.abilities = abilities
        self.are_alive = are_alive
        self.location = location
        self.held_dominant_hand = held_dominant_hand
        self.held_off_hand = held_off_hand
        self.worn_head = worn_head
        self.worn_torso = worn_torso
        self.worn_legs = worn_legs
        self.worn_feet = worn_feet
        self.worn_dominant_hand = worn_dominant_hand
        self.worn_off_hand = worn_off_hand
    
    def AC(self) -> int:
        armor_and_shield_score = 0
        for item in filter(None, self.equipped_items):    
            armor_and_shield_score += item.armor_bonus
        return self.DEX + armor_and_shield_score
    
    def AV(self) -> int:
        return self.AV_by_level[self.level-1]
    
    def calculate_highest_stat(self) -> list:
        highest_stat = []
        highest_value = max(self.CHA, self.CON, self. DEX, self.INT, self.STR, self.WIS)
        if highest_value == self.CHA:
            highest_stat.append("Charisma")
        if highest_value == self.CON:
            highest_stat.append("Constituion")
        if highest_value == self.DEX:
            highest_stat.append("Dexterity")
        if highest_value == self.INT:
            highest_stat.append("Intelligence")
        if highest_value == self.STR:
            highest_stat.append("Strength")
        if highest_value == self.WIS:
            highest_stat.append("Wisdom")
        match len(highest_stat):
            case 1:
                return highest_stat[0]
            case 2:
                return highest_stat[0] + " and " + highest_stat[1]
            case 3:
                return highest_stat[0] + ", " + highest_stat[1] + ", and " + highest_stat[2]
            case 4:
                return highest_stat[0] + ", " + highest_stat[1] + ", " + highest_stat[2] + ", and " + highest_stat[3]
            case 5:
                return highest_stat[0] + ", " + highest_stat[1] + ", " + highest_stat[2] + ", " + highest_stat[3] + ", and " + highest_stat[4]
            case 6:
                return "everything"
    
    def calculate_level_up_gold(self) -> int:
        return gold_to_reach_level[self.level+1]
        
    def character_sheet(self):
        return draw.frame(
            100, 
            [
                f"{self.name}: ({self.character_class} {self.level})",
                f"CHA {self.CHA}, CON {self.CON}, DEX {self.DEX}, INT {self.INT}, STR {self.STR}, WIS {self.WIS}",
                f"{self.current_hp}/{self.max_hp} HP, {self.AC()} AC, {self.AV()} AV",
                f"{self.gold_spent_this_level} gold spent this level, {self.gold_on_person} gold on person",
                f"EQUIPMENT: ({len(self.inventory)}/{self.STR})",
                f"{', '.join([item.name for item in self.inventory])}",
                "ABILITIES:",
                "* " + "\n* ".join(self.abilities),
                "SPELLS:",
                "* " + "\n* ".join(self.spells),
            ]
        )
    
    def create(self):
        self.name = str(input("What is your name?\n>"))
        difficulty = prompt.multiple_choice("How powerful will you be?", ["Extreme", "Standard", "Classic"])
        self.gold_on_person = dice.roll(3,6,3)*10
        match difficulty:
            case "Extreme":
                self.CHA = dice.roll(3,20,1)
                self.CON = dice.roll(3,20,1)
                self.DEX = dice.roll(3,20,1)
                self.INT = dice.roll(3,20,1)
                self.STR = dice.roll(3,20,1)
                self.WIS = dice.roll(3,20,1)
            case "Standard":
                self.CHA = dice.roll(3,10,2)
                self.CON = dice.roll(3,10,2)
                self.DEX = dice.roll(3,10,2)
                self.INT = dice.roll(3,10,2)
                self.STR = dice.roll(3,10,2)
                self.WIS = dice.roll(3,10,2)
            case "Classic":
                self.CHA = dice.roll(3,6,3)
                self.CON = dice.roll(3,6,3)
                self.DEX = dice.roll(3,6,3)
                self.INT = dice.roll(3,6,3)
                self.STR = dice.roll(3,6,3)
                self.WIS = dice.roll(3,6,3)
        print(f"\nYou're naturally most proficient in {self.calculate_highest_stat()}.")
        self.character_class = prompt.multiple_choice("What is your class?",
            [
                "Cleric", 
                "Druid",
                "Dwarf",
                "Elf",
                "Fighter",
                "Halfling",
                "Magic-User",
                "Paladin",
                "Ranger",
                "Warlock"
            ]
        )
        match self.character_class:
            case "Cleric":
                self.die = 8
                self.max_weapon_die = 6
                self.max_armor = "Medium"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 12, 13, 13, 14, 14, 14]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Divine"
                self.abilities = ["Channel Energy", "Turn Undead"]
            case "Druid":
                self.die = 6
                self.max_weapon_die = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 9, 9, 9, 10, 10, 11, 11, 11]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Nature"
                self.abilities = ["Sustain in Nature", "Rituals"]
            case "Dwarf":
                self.die = 8
                self.max_weapon_die = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
                self.abilities = ["Science and Medicine", "Inspire"]
            case "Elf":
                self.die = 6
                self.max_weapon_die = 8
                self.max_armor = "Medium"
                self.max_shield = "Small"
                self.AV_by_level = [11, 11, 12, 13, 13, 14, 15, 15, 16, 17]
                self.spellcasting_stat = "INT"
                self.spell_list = "Arcane"
                self.abilities = ["Surge", "Exert"]
            case "Fighter":
                self.die = 10
                self.max_weapon_die = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 12, 12, 13, 14, 14, 15, 16, 16, 17]
                self.abilities = ["Multikill", "Sunder"]
            case "Halfling":
                self.die = 6
                self.max_weapon_die = 6
                self.max_armor = "Light"
                self.max_shield = "Small"
                self.AV_by_level = [12, 12, 12, 12, 13, 13, 13, 13, 14, 14]
                self.abilities = ["Advantageous Strike", "Favors"]
            case "Magic-User":
                self.die = 4
                self.max_weapon_die = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 8, 9, 9, 9, 10, 10, 10, 11]
                self.spellcasting_stat = "INT"
                self.spell_list = "Arcane"
                self.abilities = ["Rituals", "Metamagic"]
            case "Paladin":
                self.die = 10
                self.max_weapon_die = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
                self.spellcasting_stat = "CHA"
                self.spell_list = "Divine"
                self.abilities = ["Lay on Hands", "Body Shield"]
            case "Ranger":
                self.die = 8
                self.max_weapon_die = 6
                self.max_armor = "Medium"
                self.max_shield = "Small"
                self.AV_by_level = [11, 11, 12, 12, 13, 13 ,14, 14, 15, 15]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Nature"
                self.abilities = ["Quarry", "Favored Terrain"]
            case "Warlock":
                self.die = 4
                self.max_weapon_die = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 8, 9, 9, 9, 10, 10, 10, 11]
                self.spellcasting_stat = "INT"
                self.spell_list = "Necronomicon"
                self.abilities = ["Corruption",]
        self.level = 1
        self.max_hp = dice.roll(1,self.die,1) + 4
        self.current_hp = self.max_hp
        self.gold_to_next_level = self.calculate_level_up_gold()
        
        self.character_sheet()
        
        confirm = prompt.multiple_choice("Confirm the above character?", ["Yes", "No"])
        match confirm:
            case "Yes":
                print("\nYou confirmed.")
            case "No":
                print("TODO: Make it so that the player reselects everything.")