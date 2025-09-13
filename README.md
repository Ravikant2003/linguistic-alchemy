# 🔮 Linguistic Alchemy - NLP for Game Development

An interactive web application that generates fictional languages, runic scripts, and magical lore for game development. Built with Streamlit and designed for game writers, dungeon masters, and fantasy world-builders.

![Linguistic Alchemy](https://img.shields.io/badge/ML-Game%20Development-8A2BE2) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B) ![Sandbox-Option_B-Implemented](https://img.shields.io/badge/Sandbox-Option_B_Implemented-green)

## ✨ Features

- **🗣️ Language Creator**: Generate complete fictional languages with grammar, vocabulary, and writing systems
- **🔣 Rune Generator**: Convert text to various runic scripts (runic, alchemical, geometric, astrological)
- **🌐 Translator**: Translate between English and created ancient languages
- **👨‍👩‍👧‍👦 Language Families**: Create families of related languages with shared linguistic roots
- **📖 Lore Generation**: Automatic creation of mystical explanations for languages and runes
- **🧪 Parameter Experiments**: Comprehensive testing of how input parameters affect output quality

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd linguistic-alchemy-streamlit
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## 🎮 How to Use

### 1. Create Your First Language
- Navigate to the **Language Creator** tab
- Enter a language name (e.g., "Dragon Tongue")
- Select a language family (Elvish, Dwarvish, Demonic, or Celestial)
- Click "Create Language" to generate grammar, vocabulary, and lore

### 2. Generate Runic Inscriptions
- Go to the **Rune Generator** tab
- Enter text to convert (e.g., "Protect this treasure")
- Choose a script style (Runic, Alchemical, Geometric, or Astrological)
- Click "Generate Runes" to create magical symbols and sigils

### 3. Translate Texts
- First create a language in the Language Creator tab
- Visit the **Translator** tab
- Enter English text to translate into your ancient language
- View the translation and bilingual inscription

### 4. Create Language Families
- Use the **Language Family** tab to generate related languages
- Specify a base name and number of languages to create
- Explore how languages evolve from common roots

## 🔬 Sandbox Option B: Parameter Experiments Implemented

This project includes comprehensive parameter experimentation as specified in the assignment's sandbox options:

### **Parameters Tested:**
- **Temperature** (0.1-2.0): Controls creativity vs. coherence in generated content
- **Max Length** (50-200): Determines output complexity and detail level
- **Language Family** (4 types): Changes phonetic patterns and aesthetic feel
- **Script Type** (4 styles): Alters visual appearance of runic symbols

### **Experimental Approach:**
- Real-time parameter adjustment with immediate feedback
- Side-by-side output comparison capabilities
- Cross-asset analysis (parameters affect languages, runes, and lore simultaneously)
- Quantitative and qualitative observations documented

### **Key Findings:**
- Higher temperature increases creativity but reduces coherence
- Different language families produce dramatically different phonetic patterns
- Script types create completely distinct visual identities for runic inscriptions
- Optimal parameter ranges identified for various game development use cases

*Detailed observations and analysis available in [`experiments.md`](./experiments.md)*

## 🏗️ Project Structure

```
linguistic-alchemy/
├── app.py                 # Main Streamlit application
├── language_generator.py  # Core language generation logic
├── rune_maker.py         # Runic script and symbol generation
├── translator.py         # Translation systems
├── lore_generator.py     # Lore and explanation generation
├── requirements.txt      # Python dependencies
├── experiments.md        # Detailed parameter experiments analysis
└── README.md            # This file
```

## 🧠 Technical Implementation

### Models & Algorithms

- **Language Generation**: Rule-based system with phonetic patterns and morphological rules
- **Vocabulary Creation**: Combinatorial approach using language-family-specific phonemes
- **Rune Generation**: Unicode symbol mapping and procedural generation
- **Lore Generation**: Template-based system with contextual meaning assignment
- **Parameter Testing**: Controlled experimentation framework with documented results

### Key Parameters

- **Temperature** (0.1-2.0): Controls creativity vs. coherence in outputs
- **Max Length** (50-200): Determines output complexity and detail
- **Language Family**: Changes phonetic patterns and aesthetic feel
- **Script Type**: Alters visual appearance of runic symbols

## 📊 Sample Outputs

### Generated Language Example
```json
{
  "name": "Forest Elvish",
  "family": "elvish",
  "grammar_type": "SOV",
  "script": "cursive flowing script",
  "vocabulary": {
    "aethul": "noun",
    "thoric": "adjective",
    "lorize": "verb",
    "miral": "adjective"
  }
}
```

### Runic Inscription Example
```
Input: "Magic is real"
Output: "ᚠᚠᚠᚢᚢ ᚢᚠ ᚥᚤᚠᚥ"
```

## 🧪 Experiments & Observations

Detailed experiments and parameter analysis are documented in [`experiments.md`](./experiments.md), including:

- Temperature effects on output creativity and coherence
- Language family characteristics and phonetic patterns
- Script type visual differences and thematic appropriateness
- Translation accuracy patterns and limitations
- Optimal parameter combinations for different game development scenarios

## 🎯 Assignment Requirements Fulfillment

✅ **Core Goal**: Built ML model useful for games (NLP for fantasy content)  
✅ **Asset Generation**: Creates languages, runes, translations, and lore (3+ asset types)  
✅ **Parameter Control**: Interactive sliders for temperature, length, family, script type  
✅ **Working Demo**: Complete Streamlit application with real-time generation  
✅ **GitHub Repo**: Clean code with clear documentation and samples  
✅ **Write-up**: Comprehensive documentation of models, parameters, and observations  
✅ **Sandbox Option B**: Parameter experiments with detailed analysis and findings  

## 🔧 Customization

### Adding New Language Families
Edit the `phonemes` dictionary in `language_generator.py`:
```python
self.phonemes = {
    "your_family": ["phoneme1", "phoneme2", "phoneme3"],
    # ... existing families
}
```

### Creating New Script Types
Modify the `symbol_blocks` in `rune_maker.py`:
```python
self.symbol_blocks = {
    "your_script": ["\uXXXX", "\uXXXX", "\uXXXX"],
    # ... existing scripts
}
```

### Extending Parameter Experiments
Add new parameters to the Streamlit sidebar in `app.py` and update `experiments.md` with findings.

## 🚀 Future Enhancements

With more time and resources, I would implement:

- **Neural Translation Models**: Proper sequence-to-sequence translation
- **Audio Generation**: Text-to-speech for hearing languages
- **Visual Runes**: Image-based rune generation instead of text
- **Export Features**: Download languages for game engines
- **API Integration**: REST API for batch processing
- **Additional Sandbox Options**: Async processing, validation metrics, etc.

## 📝 License

MIT License - feel free to use this project for your own game development needs!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for contribution include:
- Additional language families and script types
- Enhanced parameter experimentation
- Improved translation systems
- Additional sandbox option implementations

---

**Built with passion for game development and machine learning** 🎮✨

*For questions or support, please open an issue in the GitHub repository.*
