import random
import re
from typing import Dict, List
import markovify

class AncientLanguageGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        
        # Phonetic inventory for different language families
        self.phonemes = {
            "elvish": ["ae", "th", "iel", "wen", "lor", "mir", "del", "ion", "eth", "uil"],
            "dwarvish": ["thor", "din", "bal", "nor", "grim", "dur", "bok", "gron", "thok", "urn"],
            "demonic": ["zul", "kath", "gor", "morg", "xul", "neth", "rax", "vorth", "zel", "ak"],
            "celestial": ["cel", "est", "lum", "or", "ath", "riel", "phos", "hel", "aur", "sol"]
        }
        
        # Grammar rules
        self.grammar_rules = {
            "SOV": ["SUBJ OBJ VERB", "SUBJ OBJ ADJ VERB"],
            "SVO": ["SUBJ VERB OBJ", "SUBJ VERB ADJ OBJ"],
            "VSO": ["VERB SUBJ OBJ", "VERB SUBJ ADJ OBJ"]
        }
        
        self.languages = {}

    def generate_language(self, language_name: str, family: str = "elvish") -> Dict:
        """Generate a complete fictional language with grammar and vocabulary"""
        # Select phonemes based on language family
        base_phonemes = self.phonemes.get(family, self.phonemes["elvish"])
        
        # Generate vocabulary (50-100 words)
        vocabulary = self._generate_vocabulary(base_phonemes, word_count=random.randint(50, 100))
        
        # Select grammar structure
        grammar_type = random.choice(list(self.grammar_rules.keys()))
        
        # Generate morphological rules
        morphology = self._generate_morphology()
        
        language = {
            "name": language_name,
            "family": family,
            "vocabulary": vocabulary,
            "grammar_type": grammar_type,
            "morphology": morphology,
            "script": self._generate_script_pattern()
        }
        
        self.languages[language_name] = language
        return language

    def _generate_vocabulary(self, phonemes: List[str], word_count: int) -> Dict[str, str]:
        """Generate vocabulary using phonetic patterns and rules"""
        vocabulary = {}
        categories = ["noun", "verb", "adjective", "adverb", "preposition"]
        
        # Define some common suffixes and prefixes for different categories
        affixes = {
            "noun": ["-ion", "-eth", "-ul", "-ar", "-en", "-il", "-or", "-ath"],
            "verb": ["-ate", "-ish", "-ize", "-en", "-ify", "-es", "-eth"],
            "adjective": ["-ic", "-al", "-ous", "-ive", "-y", "-ed", "-ing", "-an"],
            "adverb": ["-ly", "-ward", "-wise", "-way", "-time"],
            "preposition": ["a-", "be-", "for-", "with-", "out-"]
        }

        for i in range(word_count):
            category = random.choice(categories)
            
            # Build a word from 1-3 phonemes
            num_phonemes = random.randint(1, 3)
            base_word = ""
            
            for _ in range(num_phonemes):
                base_word += random.choice(phonemes)
            
            # Add category-appropriate affixes with some probability
            if random.random() > 0.3:  # 70% chance to add an affix
                if category in affixes:
                    if category == "preposition" and random.random() > 0.5:
                        # Add prefix for prepositions
                        base_word = random.choice(affixes[category]) + base_word
                    else:
                        # Add suffix for other categories
                        base_word += random.choice(affixes[category])
            
            # Ensure the word is not empty and unique
            if base_word and base_word not in vocabulary:
                vocabulary[base_word] = category
        
        return vocabulary
    def _generate_morphology(self) -> Dict:
        """Generate morphological rules for the language"""
        return {
            "plural_rules": random.choice([
                "add 'i' suffix", "add 'en' suffix", "vowel change", "add 'ath' suffix"
            ]),
            "verb_conjugation": random.choice([
                "regular", "irregular", "prefix-based", "tone-based"
            ]),
            "case_system": random.choice([
                "none", "nominative-accusative", "ergative-absolutive"
            ])
        }

    def _generate_script_pattern(self) -> str:
        """Generate a description of the writing system"""
        scripts = [
            "cursive flowing script", "angular runic carvings", 
            "geometric patterns", "dot-based notation",
            "circular glyphs", "linear phonetic symbols"
        ]
        return random.choice(scripts)

    def generate_sentence(self, language_name: str, complexity: int = 1) -> str:
        """Generate a sentence in the created language"""
        if language_name not in self.languages:
            raise ValueError(f"Language {language_name} not found")
        
        lang = self.languages[language_name]
        words = list(lang['vocabulary'].keys())
        
        # Simple sentence generation based on grammar type
        if lang['grammar_type'] == "SVO":
            structure = random.choice(["SUBJ VERB OBJ", "SUBJ VERB ADJ OBJ"])
        elif lang['grammar_type'] == "SOV":
            structure = random.choice(["SUBJ OBJ VERB", "SUBJ OBJ ADJ VERB"])
        else:  # VSO
            structure = random.choice(["VERB SUBJ OBJ", "VERB SUBJ ADJ OBJ"])
        
        # Replace placeholders with actual words
        sentence = structure
        for placeholder in ["SUBJ", "VERB", "OBJ", "ADJ"]:
            if placeholder in sentence:
                # Get words of appropriate category
                if placeholder == "SUBJ" or placeholder == "OBJ":
                    category_words = [w for w, cat in lang['vocabulary'].items() if cat == "noun"]
                elif placeholder == "VERB":
                    category_words = [w for w, cat in lang['vocabulary'].items() if cat == "verb"]
                elif placeholder == "ADJ":
                    category_words = [w for w, cat in lang['vocabulary'].items() if cat == "adjective"]
                
                if category_words:
                    sentence = sentence.replace(placeholder, random.choice(category_words), 1)
        
        return sentence.capitalize()

    def create_language_family(self, base_name: str, num_languages: int = 3) -> Dict:
        """Create a family of related languages"""
        family = {}
        
        # Create the base language and add it to the main registry
        base_language = self.generate_language(f"{base_name}_prime", "elvish")
        family[f"{base_name}_prime"] = base_language
        self.languages[f"{base_name}_prime"] = base_language  # ← THIS LINE WAS MISSING
        
        for i in range(1, num_languages):
            # Create derived languages with shared vocabulary
            derived_lang = base_language.copy()
            derived_lang_name = f"{base_name}_{i}"
            derived_lang["name"] = derived_lang_name
            
            # Modify some vocabulary (about 1/3 of words)
            words_to_change = random.sample(
                list(derived_lang["vocabulary"].keys()), 
                k=len(derived_lang["vocabulary"]) // 3
            )
            
            for word in words_to_change:
                new_word = word + random.choice(["a", "i", "o", "th", "n", "el", "ar"])
                # Keep the same word category
                category = derived_lang["vocabulary"][word]
                derived_lang["vocabulary"][new_word] = category
                del derived_lang["vocabulary"][word]
            
            # Also change the grammar sometimes
            if random.random() > 0.7:  # 30% chance to change grammar
                derived_lang["grammar_type"] = random.choice(["SVO", "SOV", "VSO"])
            
            # Add to both the family and the main languages registry
            family[derived_lang_name] = derived_lang
            self.languages[derived_lang_name] = derived_lang  # ← THIS LINE WAS MISSING
        
        return family 