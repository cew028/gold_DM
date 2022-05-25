import dice
import prompt

gold_to_reach_level = {
    # next level : cost to get there
    2: 500,
    3: 1000,
    4: 2000,
    5: 4000,
    6: 8000,
    7: 16000,
    8: 32000,
    9: 64000,
    10: 128000,
}

class Player():
    def __init__(
        self,
        name = "Unnamed",
        character_class = "None",
        die = 0,
        max_weapon = 0,
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
        AC = 0,
        AV = 0,
        gold_on_person = 0,
        gold_stored_away = 0,
        gold_spent_this_level = 0,
        gold_to_next_level = 0,
        inventory = [],
        spells = [],
        equipped_armor = {"Name" : "None", "Bonus" : 0, "Effect": "None"},
        equipped_shield = {"Name" : "None", "Bonus" : 0, "Effect": "None"},
        equipped_weapon = {"Name" : "None", "Bonus" : 0, "Effect": "None"},
        spellcasting_stat = "None",
        spell_list = "None",
    ):
        self.name = name
        self.character_class = character_class
        self.die = die
        self.max_weapon = max_weapon
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
        self.AC = AC
        self.AV = AV
        self.gold_on_person = gold_on_person
        self.gold_stored_away = gold_stored_away
        self.gold_spent_this_level = gold_spent_this_level
        self.gold_to_next_level = gold_to_next_level
        self.inventory = inventory
        self.spells = spells
        self.equipped_armor = equipped_armor
        self.equipped_shield = equipped_shield
        self.equipped_weapon = equipped_weapon
        self.spellcasting_stat = spellcasting_stat
        self.spell_list = spell_list
    
    def calculate_AC(self):
        return self.DEX + self.equipped_armor["Bonus"] + self.equipped_shield["Bonus"]
    
    def calculate_AV(self):
        return self.AV_by_level[self.level-1]
    
    def calculate_level_up_gold(self):
        return gold_to_reach_level[self.level+1]
    
    def create(self):
        self.name = str(input("What is your name?\n"))
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
                self.max_weapon = 6
                self.max_armor = "Medium"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 12, 13, 13, 14, 14, 14]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Divine"
            case "Druid":
                self.die = 6
                self.max_weapon = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 9, 9, 9, 10, 10, 11, 11, 11]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Nature"
            case "Dwarf":
                self.die = 8
                self.max_weapon = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
            case "Elf":
                self.die = 6
                self.max_weapon = 8
                self.max_armor = "Medium"
                self.max_shield = "Small"
                self.AV_by_level = [11, 11, 12, 13, 13, 14, 15, 15, 16, 17]
                self.spellcasting_stat = "INT"
                self.spell_list = "Arcane"
            case "Fighter":
                self.die = 10
                self.max_weapon = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 12, 12, 13, 14, 14, 15, 16, 16, 17]
            case "Halfling":
                self.die = 6
                self.max_weapon = 6
                self.max_armor = "Light"
                self.max_shield = "Small"
                self.AV_by_level = [12, 12, 12, 12, 13, 13, 13, 13, 14, 14]
            case "Magic-User":
                self.die = 4
                self.max_weapon = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 8, 9, 9, 9, 10, 10, 10, 11]
                self.spellcasting_stat = "INT"
                self.spell_list = "Arcane"
            case "Paladin":
                self.die = 10
                self.max_weapon = 8
                self.max_armor = "Heavy"
                self.max_shield = "Large"
                self.AV_by_level = [11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
                self.spellcasting_stat = "CHA"
                self.spell_list = "Divine"
            case "Ranger":
                self.die = 8
                self.max_weapon = 6
                self.max_armor = "Medium"
                self.max_shield = "Small"
                self.AV_by_level = [11, 11, 12, 12, 13, 13 ,14, 14, 15, 15]
                self.spellcasting_stat = "WIS"
                self.spell_list = "Nature"
            case "Warlock":
                self.die = 4
                self.max_weapon = 4
                self.max_armor = "Light"
                self.max_shield = "None"
                self.AV_by_level = [8, 8, 8, 9, 9, 9, 10, 10, 10, 11]
                self.spellcasting_stat = "INT"
                self.spell_list = "Necronomicon"
        self.level = 1
        self.AV = self.calculate_AV()
        self.max_hp = dice.roll(1,self.die,1) + 4
        self.current_hp = self.max_hp
        self.gold_to_next_level = self.calculate_level_up_gold()
        self.AC = self.calculate_AC()
        
        print(f"You just created a player with name {self.name} class {self.character_class} max weapon {self.max_weapon} max armor {self.max_armor} max shield {self.max_shield} level {self.level} AV by level {self.AV_by_level } CHA {self.CHA} CON {self.CON} DEX {self.DEX} INT {self.INT} STR {self.STR} WIS {self.WIS} current hp {self.current_hp} max hp {self.max_hp} AC {self.AC} AV {self.AV} gold on person {self.gold_on_person} gold stored away {self.gold_stored_away} gold spent this level {self.gold_spent_this_level} gold to next level {self.gold_to_next_level} inventory {self.inventory} spells {self.spells} equipped armor {self.equipped_armor} equipped shield {self.equipped_shield} equipped weapon {self.equipped_weapon} spellcasting stat {self.spellcasting_stat} spell list {self.spell_list}")