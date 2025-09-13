import random

class LoreGenerator:
    def __init__(self):
        # Define actual meanings for common runic symbols
        self.rune_meanings = {
            "ᚠ": ["wealth", "cattle", "nourishment", "abundance"],
            "ᚢ": ["strength", "resilience", "primal force", "endurance"],
            "ᚦ": ["danger", "conflict", "protection", "threshold"],
            "ᚥ": ["magic", "mystery", "the unknown", "arcane power"],
            "ᚤ": ["journey", "path", "destiny", "travel"],
            "ᚨ": ["divinity", "inspiration", "higher power", "gods"],
            "ᚾ": ["necessity", "constraint", "fate", "need"],
            " ": ["separation", "pause", "breath", "transition"]
        }
        
        self.language_origins = {
            "elvish": ["ancient forest dwellers", "moon-worshipping scholars", "nature guardians"],
            "dwarvish": ["mountain clans", "deep-earth miners", "stone-shaping artisans"],
            "demonic": ["shadow realm entities", "forgotten abyss dwellers", "chaos manifestations"],
            "celestial": ["star-born beings", "light messengers", "sky deities"]
        }

    def generate_language_lore(self, language_data: dict) -> str:
        """Generate lore explaining the language's origins and features"""
        family = language_data.get('family', 'elvish')
        origins = self.language_origins.get(family, self.language_origins['elvish'])
        
        lore_templates = [
            f"The {language_data['name']} tongue was spoken by {random.choice(origins)}. "
            f"Their {language_data['script']} writing system reflects their "
            f"{random.choice(['connection to nature', 'stone-crafting traditions', 'arcane studies', 'celestial observations'])}. "
            f"With its {language_data['grammar_type']} structure, this language is perfect for "
            f"{random.choice(['complex spellcasting', 'precise engineering', 'poetic verses', 'ritual incantations'])}.",
            
            f"Originating from {random.choice(origins)}, {language_data['name']} features "
            f"{random.choice(['flowing', 'harsh', 'melodic', 'guttural'])} sounds suited for "
            f"{random.choice(['whispered secrets', 'mountain echoes', 'forest songs', 'temple chants'])}. "
            f"The {language_data['morphology']['plural_rules']} plural rules make it ideal for "
            f"{random.choice(['describing magical phenomena', 'documenting history', 'reciting prophecies', 'recording recipes'])}."
        ]
        
        return random.choice(lore_templates)

    def generate_rune_lore(self, rune_script: str, intent: str) -> str:
        """Generate meaningful lore for runic inscriptions"""
        # Clean the rune script and get unique symbols
        clean_runes = rune_script.replace(' ', '')
        unique_runes = list(set(clean_runes))
        
        # Analyze the most common runes
        rune_counts = {rune: clean_runes.count(rune) for rune in unique_runes}
        significant_runes = sorted(rune_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Build the lore
        lore_parts = []
        
        # Introduction
        intros = [
            f"This inscription '{rune_script}' was carved for {intent.lower()}.",
            f"The runes '{rune_script}' hold power related to {intent.lower()}.",
            f"Ancient artisans created this pattern '{rune_script}' to achieve {intent.lower()}."
        ]
        lore_parts.append(random.choice(intros))
        
        # Describe significant runes
        if significant_runes:
            lore_parts.append("\nThe symbols represent:")
            for rune, count in significant_runes:
                if rune in self.rune_meanings:
                    meaning = random.choice(self.rune_meanings[rune])
                    lore_parts.append(f"- '{rune}' signifies {meaning} (appears {count} times)")
        
        # Overall interpretation
        interpretations = [
            "\nTogether, these runes create a harmonious magical field.",
            "\nThe arrangement suggests a protective or enhancing effect.",
            "\nThis pattern channels elemental energies effectively.",
            "\nThe repetition indicates a focused, powerful intention."
        ]
        lore_parts.append(random.choice(interpretations))
        
        return "\n".join(lore_parts)

# Example usage:
if __name__ == "__main__":
    lore_gen = LoreGenerator()
    sample_runes = "ᚠᚠᚠᚢᚢ ᚢᚠ ᚥᚤᚠᚥ"
    print(lore_gen.generate_rune_lore(sample_runes, "Magic is real"))