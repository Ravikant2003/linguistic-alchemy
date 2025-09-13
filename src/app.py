import streamlit as st
import random
from language_generator import AncientLanguageGenerator
from rune_maker import RuneGenerator
from lore_generator import LoreGenerator
from translator import LinguisticTranslator

# Set page config
st.set_page_config(
    page_title="Linguistic Alchemy",
    page_icon="🔮",
    layout="wide"
)

# Initialize components with session state
if 'language_gen' not in st.session_state:
    st.session_state.language_gen = AncientLanguageGenerator()
if 'rune_gen' not in st.session_state:
    st.session_state.rune_gen = RuneGenerator()
if 'lore_gen' not in st.session_state:
    st.session_state.lore_gen = LoreGenerator()
if 'translator' not in st.session_state:
    st.session_state.translator = LinguisticTranslator(st.session_state.language_gen)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #8A2BE2;
        text-align: center;
        margin-bottom: 2rem;
    }
    .rune-display {
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .language-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #8A2BE2;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔮 Linguistic Alchemy</h1>', unsafe_allow_html=True)
st.markdown("### Generate Ancient Languages, Runic Scripts, and Magical Lore")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Language Creator", 
    "Rune Generator", 
    "Translator", 
    "Language Family"
])

with tab1:
    st.header("Create Ancient Languages")
    
    col1, col2 = st.columns(2)
    
    with col1:
        language_name = st.text_input("Language Name", "Elvish")
        language_family = st.selectbox(
            "Language Family",
            ["elvish", "dwarvish", "demonic", "celestial"]
        )
        seed = st.number_input("Random Seed (optional)", min_value=0, value=None)
        generate_btn = st.button("Create Language", type="primary")
    
    if generate_btn:
        with st.spinner("Weaving linguistic magic..."):
            if seed is not None:
                st.session_state.language_gen = AncientLanguageGenerator(seed)
            
            language = st.session_state.language_gen.generate_language(
                language_name, language_family
            )
            lore = st.session_state.lore_gen.generate_language_lore(language)
            example_sentence = st.session_state.language_gen.generate_sentence(language_name)
            
            st.session_state.current_language = language
            
            with col2:
                st.markdown(f'<div class="language-card">', unsafe_allow_html=True)
                st.subheader(f"✨ {language['name']}")
                st.write(f"**Family:** {language['family']}")
                st.write(f"**Grammar:** {language['grammar_type']}")
                st.write(f"**Writing System:** {language['script']}")
                st.write(f"**Plural Rules:** {language['morphology']['plural_rules']}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.subheader("Example Sentence")
                st.info(example_sentence)
                
                st.subheader("Language Lore")
                st.write(lore)
                
                # Show some vocabulary
                st.subheader("Sample Vocabulary")
                vocab_sample = dict(list(language['vocabulary'].items())[:10])
                st.json(vocab_sample)

with tab2:
    st.header("Generate Runic Inscriptions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        text_to_convert = st.text_area("Text to convert to runes", "Magic is real")
        script_type = st.selectbox(
            "Script Type",
            ["runic", "alchemical", "geometric", "astrological"]
        )
        generate_runes_btn = st.button("Generate Runes", type="primary")
    
    if generate_runes_btn and text_to_convert:
        with st.spinner("Carving ancient symbols..."):
            runic_text = st.session_state.rune_gen.generate_rune_script(text_to_convert, script_type)
            rune_circle = st.session_state.rune_gen.generate_rune_circle(text_to_convert)
            sigil = st.session_state.rune_gen.generate_magic_sigil(text_to_convert)
            lore = st.session_state.lore_gen.generate_rune_lore(runic_text, text_to_convert)
            
            with col2:
                st.subheader("Runic Translation")
                st.markdown(f'<div class="rune-display">{runic_text}</div>', unsafe_allow_html=True)
                
                st.subheader("Magic Sigil")
                st.markdown(f'<div class="rune-display">{sigil}</div>', unsafe_allow_html=True)
                
                st.subheader("Circular Inscription")
                st.code(rune_circle)
                
                st.subheader("Lore of the Runes")
                st.write(lore)

with tab3:
    st.header("Ancient Language Translator")
    
    if 'current_language' not in st.session_state:
        st.warning("Create a language first in the 'Language Creator' tab!")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            english_text = st.text_area("English text to translate", "The sky is beautiful today")
            translate_btn = st.button("Translate", type="primary")
        
        if translate_btn:
            with st.spinner("Deciphering ancient texts..."):
                # Ensure translation model exists
                lang_name = st.session_state.current_language['name']
                if lang_name not in st.session_state.translator.translation_models:
                    english_words = ["sky", "earth", "fire", "water", "light", 
                                   "dark", "life", "death", "beautiful", "today"]
                    st.session_state.translator.create_translation_system(lang_name, english_words)
                
                translated = st.session_state.translator.translate_to_ancient(english_text, lang_name)
                bilingual = st.session_state.translator.create_bilingual_inscription(english_text, lang_name)
                
                with col2:
                    st.subheader("Translation")
                    st.info(translated)
                    
                    st.subheader("Bilingual Inscription")
                    st.text(bilingual)
                    
                    # Show translation pairs
                    st.subheader("Translation Dictionary")
                    st.json(st.session_state.translator.translation_models[lang_name][:10])

with tab4:
    st.header("Create Language Families")
    
    col1, col2 = st.columns(2)
    
    with col1:
        base_name = st.text_input("Base Language Name", "Ancient")
        num_languages = st.slider("Number of related languages", 2, 5, 3)
        create_family_btn = st.button("Create Language Family", type="primary")
    
    if create_family_btn:
        with st.spinner("Evolving linguistic roots..."):
            family = st.session_state.language_gen.create_language_family(base_name, num_languages)
            st.session_state.language_family = family
            
            with col2:
                st.subheader(f"{base_name} Language Family")
                
                for lang_name, lang_data in family.items():
                    with st.expander(f"🌐 {lang_name}"):
                        st.write(f"**Grammar:** {lang_data['grammar_type']}")
                        st.write(f"**Writing:** {lang_data['script']}")
                        
                        # Show a sample sentence
                        example = st.session_state.language_gen.generate_sentence(lang_name)
                        st.write(f"**Example:** {example}")
                        
                        # Show vocabulary differences
                        st.write("**Sample Vocabulary:**")
                        sample_words = dict(list(lang_data['vocabulary'].items())[:5])
                        st.json(sample_words)

# Sidebar with info and controls
with st.sidebar:
    st.header("⚙️ Parameters & Controls")
    
    st.subheader("Model Parameters")
    temperature = st.slider("Creativity Temperature", 0.1, 2.0, 0.9, 0.1)
    max_length = st.slider("Max Generation Length", 50, 200, 100, 10)
    
    st.subheader("App Info")
    st.info("""
    **Linguistic Alchemy** uses advanced NLP techniques
    to generate fictional languages, runic scripts,
    and magical lore for game development.
    """)
    
    if st.button("Clear Session"):
        st.session_state.clear()
        st.rerun()

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Linguistic Alchemy v1.0 • For Game Development")