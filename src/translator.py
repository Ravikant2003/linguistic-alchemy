class LinguisticTranslator:
    def __init__(self, language_generator):
        self.lg = language_generator
        self.translation_models = {}
    
    def create_translation_system(self, language_name: str, english_corpus: list):
        """Create a simple translation model between English and the generated language"""
        # This is a simplified approach - in reality you'd use proper ML
        lang = self.lg.languages[language_name]
        translation_pairs = []
        
        # Create some basic translation pairs based on word categories
        for i, word in enumerate(lang['vocabulary'].keys()):
            if i < len(english_corpus):
                translation_pairs.append((english_corpus[i], word))
        
        self.translation_models[language_name] = translation_pairs
        return translation_pairs
    
    def translate_to_ancient(self, english_text: str, language_name: str) -> str:
        """Translate English text to the ancient language"""
        if language_name not in self.translation_models:
            raise ValueError(f"No translation model for {language_name}")
        
        # Simple word-by-word translation (this would be more complex IRL)
        words = english_text.lower().split()
        translated_words = []
        
        for word in words:
            # Find the best match in translation pairs
            found = False
            for eng, ancient in self.translation_models[language_name]:
                if word in eng:
                    translated_words.append(ancient)
                    found = True
                    break
            
            if not found:
                translated_words.append(word)  # Keep untranslated
        
        return " ".join(translated_words)
    
    def create_bilingual_inscription(self, text: str, language_name: str) -> str:
        """Create a side-by-side translation"""
        from rune_maker import RuneGenerator
        rune_gen = RuneGenerator()
        
        ancient_text = self.translate_to_ancient(text, language_name)
        runic_text = rune_gen.generate_rune_script(ancient_text)
        
        return f"""
English: {text}
{language_name}: {ancient_text}
Runic: {runic_text}
        """