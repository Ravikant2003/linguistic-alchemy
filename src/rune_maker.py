import random

class RuneGenerator:
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
        
        # Unicode blocks for interesting symbols
        self.symbol_blocks = {
            "alchemical": ["\u26B0", "\u26B1", "\u2695", "\u2697", "\u26E8"],
            "runic": ["\u16A0", "\u16A1", "\u16A2", "\u16A3", "\u16A4", "\u16A5"],
            "geometric": ["\u25A0", "\u25B2", "\u25C6", "\u25C7", "\u25C8"],
            "astrological": ["\u2600", "\u2601", "\u2602", "\u2603", "\u2604"]
        }
    
    def generate_rune_script(self, text: str, script_type: str = "runic") -> str:
        """Convert text to a runic representation"""
        # Create mapping from letters to symbols
        symbols = self.symbol_blocks.get(script_type, self.symbol_blocks["runic"])
        symbol_mapping = {}
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(letters):
            symbol_mapping[char] = symbols[i % len(symbols)]
        
        # Convert text to runes
        runic_text = ""
        for char in text.lower():
            if char in symbol_mapping:
                runic_text += symbol_mapping[char]
            else:
                runic_text += char
        
        return runic_text
    
    def generate_rune_circle(self, phrase: str, diameter: int = 5) -> str:
        """Generate a circular rune inscription (ASCII art)"""
        circle = ""
        chars = list(phrase.replace(" ", ""))
        
        if not chars:
            return "O"
        
        # Simple circular pattern
        for i in range(diameter):
            line = ""
            for j in range(diameter):
                # Calculate position in circular pattern
                dist_from_center = ((i - diameter/2)**2 + (j - diameter/2)**2)**0.5
                if dist_from_center < diameter/2:
                    idx = int((i * diameter + j) % len(chars))
                    line += chars[idx]
                else:
                    line += " "
            circle += line + "\n"
        
        return circle
    
    def generate_magic_sigil(self, intent: str) -> str:
        """Generate a magical sigil based on intent words"""
        words = intent.split()
        sigil = ""
        
        for word in words:
            # Take first and last letter or other pattern
            if len(word) > 1:
                sigil += word[0] + word[-1]
            else:
                sigil += word
        
        # Convert to runic
        return self.generate_rune_script(sigil, "alchemical")