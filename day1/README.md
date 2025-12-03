# 🔮 Madame Zelda's Mystical Winter Fortune Teller

Welcome to Madame Zelda's Fortune Telling Tent at the Winter Festival! This CLI application generates beautiful, themed fortunes with multiple mystical personalities.

## ✨ Features

- **5 Unique Personalities** - Each with their own style, emojis, and fortune themes
- **Beautiful ASCII Art** - Crystal ball visualization with decorative borders
- **Winter & Magical Themes** - Seasonal fortunes perfect for the festival
- **Smart Text Wrapping** - Fortunes automatically wrap to stay within borders
- **CLI Friendly** - Designed for terminal display with proper formatting
- **Goose Run Compatible** - Can be executed via `goose run` for bonus points! 🎁

## 🎭 The Fortune Tellers

### 😠 Grumpy Gandalf
Pessimistic winter predictions with a grouchy attitude. Perfect for those who like their fortunes with a side of cynicism.

**Example:** *"Winter is coming... and so are your unpaid bills. ❄️💸"*

### 🌙 Mystical Wordsworth  
Beautiful poetic verses about fate and destiny. For those who appreciate the literary arts.

**Example:** *"Like snowflakes dancing in moonlight's embrace, joy shall find you in the most unexpected place. ❄️🌙"*

### 🎄 Jolly St. Fortune
Holiday cheer and festive celebrations! Spreading joy and winter magic.

**Example:** *"Ho ho ho! A surprise gift awaits you this season! 🎁✨"*

### 🙄 Eye-Rolling Oracle
Witty, sarcastic insights with a modern twist. Not your grandmother's fortune teller.

**Example:** *"The universe has big plans for you... eventually... maybe... 🤷"*

### 🔮 The Enigmatic Seer
Cryptic prophecies and mysterious omens. For those who like their fortunes wrapped in enigma.

**Example:** *"Three shadows converge where the moonlight bends... 🌙👁️"*

## 📦 Installation

No installation required! Just Python 3.

```bash
# Make the scripts executable
chmod +x fortune.sh
```

## 🚀 Usage

### Direct Python Usage

```bash
# Show help
python fortune_teller.py --help

# Display all personalities (one fortune each)
python fortune_teller.py

# Get a specific personality fortune
python fortune_teller.py grumpy
python fortune_teller.py poetic
python fortune_teller.py festive
python fortune_teller.py sarcastic
python fortune_teller.py mysterious

# Generate multiple fortunes
python fortune_teller.py grumpy 3
python fortune_teller.py festive 5
```

### Bash Script Usage

```bash
# Run with defaults (shows all personalities)
./fortune.sh

# Specify personality
./fortune.sh grumpy

# Specify personality and count
./fortune.sh mysterious 3
```

### 🎁 BONUS: Goose Run Usage

For those using the awesome **goose** CLI tool by Block:

```bash
# Run via goose (using text instructions)
goose run -t "run ./fortune.sh festive 2"

# Or run Python directly
goose run -t "run python fortune_teller.py poetic"
```

## 📋 Available Personalities

| Personality | Name | Emoji | Mood |
|------------|------|-------|------|
| `grumpy` | Grumpy Gandalf | 😠 | Pessimistic & Cynical |
| `poetic` | Mystical Wordsworth | 🌙 | Lyrical & Beautiful |
| `festive` | Jolly St. Fortune | 🎄 | Joyful & Celebratory |
| `sarcastic` | Eye-Rolling Oracle | 🙄 | Witty & Sardonic |
| `mysterious` | The Enigmatic Seer | 🔮 | Cryptic & Enigmatic |
| `all` | All Personalities | 🎭 | Shows one from each |

## 🎨 Sample Output

```
╔═══════════════════════════════════════════════╗
║                                                 ║
║       ✨ MADAME ZELDA'S WINTER FORTUNES ✨        ║
║                                                 ║
║               😠 Grumpy Gandalf 😠                ║
║                                                 ║
╔═══════════════════════════════════════════════╗
║                       ___                       ║
║                      .-'   `-.                  ║
║                    /  o   o  \                  ║
║                   |     ^     |                 ║
║                     \  \_/  /                   ║
║                       `.___.'                   ║
║                                                 ║
║            ~~ YOUR WINTER FORTUNE ~~            ║
║                                                 ║
║     The spirits say: You'll slip on ice.        ║
║              Probably tomorrow. 🧊               ║
║                                                 ║
╚═══════════════════════════════════════════════╝

✨ ⭐ ✨ ⭐ ✨
```

**Note:** All fortunes feature intelligent text wrapping to ensure perfect formatting within borders!

## 🏆 Winter Festival Challenge

This project was created for the Winter Festival Fortune Telling Tent challenge, sponsored by the kind folks who build **goose** - the AI-powered CLI assistant by Block.

### Requirements Met ✅

- ✅ **3+ Fortunes** - 5 unique personalities with 7-8 fortunes each
- ✅ **Different Moods** - Grumpy, Poetic, Festive, Sarcastic, Mysterious
- ✅ **Visual Appeal** - ASCII art, emojis, decorative borders
- ✅ **Themed Content** - Winter and magical themes throughout
- ✅ **CLI Optimized** - Designed for terminal window display
- ✅ **Goose Run Compatible** - Works with `goose run` command

### Bonus Features 🎁

- 🎯 **Argument Support** - Pass personality and count as flags
- 🎨 **Unique Borders** - Each personality has custom ASCII borders
- 🔮 **Crystal Ball Art** - Beautiful ASCII crystal ball in every fortune
- 📚 **Multiple Fortunes** - Can generate multiple fortunes per run
- 🎭 **Show All Mode** - Display samples from all personalities

## 🧑‍💻 Technical Details

- **Language:** Python 3
- **Dependencies:** None (uses only standard library)
- **Output:** ANSI-compatible terminal output
- **Random Selection:** Uses Python's `random.choice()` for fortune selection
- **Text Wrapping:** Intelligent line wrapping prevents border overflow
- **Extensible:** Easy to add new personalities and fortunes

### 🔧 Text Wrapping Feature

The application includes intelligent text wrapping to ensure all fortune text stays perfectly within the decorative borders:

- **Conservative Width:** Fortunes wrap at 43 characters to account for emoji spacing
- **Multi-line Support:** Preserves intentional line breaks in poetic fortunes
- **Automatic Wrapping:** Long fortunes automatically break at natural word boundaries
- **Centered Display:** Wrapped text remains centered within borders

**Example:**
```
Before Fix:  ║ Text extending past the border... ❌ ║
After Fix:   ║     Text properly wrapped and      ║
             ║       centered within! ✅           ║
```

## 📝 Files

- `fortune_teller.py` - Main Python application
- `fortune.sh` - Bash wrapper script
- `fortune.yaml` - Goose recipe configuration (experimental)
- `README.md` - This file

## 🎪 About the Winter Festival

The Winter Festival opened this morning, and Madame Zelda's mystical crystal ball (actually a fancy iPad app) crashed during the opening ceremony. With 50 people waiting for their winter fortunes, this CLI app saves the day by generating beautiful fortunes right in the terminal!

## 📄 License

Created for the Winter Festival Challenge - Free to use and modify!

---

**Built with ❄️ for the Winter Festival**  
*Powered by goose 🪿 - The AI assistant by Block*
