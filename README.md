# 🎄 Advent of AI - Winter Festival Collection

A collection of magical winter-themed applications built for the Advent of AI event. Each day presents a unique challenge that showcases different technologies, storytelling approaches, and creative problem-solving.

## 📖 Project Overview

This repository contains projects created as part of the Advent of AI challenge. Each day features a unique application that explores different aspects of development, from CLI tools to interactive web experiences, all unified by a magical winter theme.

---

## 🔮 Day 1: Madame Zelda's Mystical Winter Fortune Teller

**Challenge**: Build a CLI fortune teller application with multiple personalities and beautiful winter theming.

### ✨ Features

- **🎭 5 Unique Personalities**: Each with distinct styles, emojis, and fortune themes
- **🎨 Beautiful ASCII Art**: Crystal ball visualization with decorative borders  
- **❄️ Winter & Magical Themes**: Seasonal fortunes perfect for the festival
- **📝 Smart Text Wrapping**: Fortunes automatically wrap to stay within borders
- **🖥️ CLI Optimized**: Designed for beautiful terminal display
- **🪿 Goose Compatible**: Can be executed via `goose run` for bonus points!

### 🎭 The Five Fortune Tellers

| Personality | Character | Style | Example |
|------------|-----------|-------|---------|
| `grumpy` | 😠 Grumpy Gandalf | Pessimistic & Cynical | *"Winter is coming... and so are your unpaid bills. ❄️💸"* |
| `poetic` | 🌙 Mystical Wordsworth | Lyrical & Beautiful | *"Like snowflakes dancing in moonlight's embrace..."* |
| `festive` | 🎄 Jolly St. Fortune | Joyful & Celebratory | *"Ho ho ho! A surprise gift awaits you this season! 🎁✨"* |
| `sarcastic` | 🙄 Eye-Rolling Oracle | Witty & Modern | *"The universe has big plans for you... eventually... 🤷"* |
| `mysterious` | 🔮 The Enigmatic Seer | Cryptic & Enigmatic | *"Three shadows converge where moonlight bends... 🌙👁️"* |

### 🛠️ Tech Stack
- **Python 3**: Core application logic
- **Standard Library**: No external dependencies
- **ASCII Art**: Custom crystal ball and border designs
- **Bash Scripts**: Wrapper for easy execution
- **YAML**: Goose recipe configuration

### 🚀 Quick Start
```bash
# Show all personalities
python day1/fortune_teller.py

# Get specific fortune
python day1/fortune_teller.py grumpy 3

# Use bash wrapper
./day1/fortune.sh festive

# Run with goose
goose run -t "run ./day1/fortune.sh mysterious"
```

**📁 Location**: `day1/fortune_teller.py`

---

## 🎮 Day 2: Winter's Magical Path

**Challenge**: Build a choose-your-own-adventure web app with branching story paths, user choices, and beautiful winter styling.

An immersive choose-your-own-adventure web app featuring branching storylines, multiple endings, and beautiful winter-themed styling.

### ✨ Features

- **📚 Rich Interactive Storytelling**: 9 different choice points leading to unique story paths
- **🎯 Multiple Endings**: 9 distinct magical endings based on user choices
- **🎨 Beautiful Winter Theme**: Sophisticated dark design with festive green & red accents
- **❄️ Animated Effects**: Falling snow animation and magical visual effects
- **🗺️ Journey Tracking**: Displays a beautiful summary of user choices at each ending
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **⚡ Single File App**: Complete experience in one HTML file for easy sharing

### 🌟 Story Paths & Endings

Players navigate through an enchanted winter forest with three main paths:

1. **🌟 Starlight Grove Path**
   - ✨ Celestial Guardian Ending
   - 🕊️ Winter Wind Ending  
   - 🔮 Oracle of Winter Ending

2. **❄️ Frozen Lake Path**
   - 🌌 Aurora Spirit Ending
   - 👑 Winter Monarch Ending
   - 📚 Memory Keeper Ending

3. **🔥 Cozy Cabin Path**
   - 🏠 Hearth Guardian Ending
   - 🌍 World Creator Ending
   - 💝 Kindness Spirit Ending

### 🛠️ Tech Stack

- **HTML5**: Semantic structure and accessibility
- **CSS3**: Advanced styling with gradients, animations, and responsive design
  - Custom animations (falling snow, button effects, text glow)
  - Flexbox layout for responsive design
  - CSS Grid for content organization
  - Custom fonts from Google Fonts (Cinzel, Dancing Script)
- **Vanilla JavaScript**: Interactive functionality and game logic
  - Dynamic content rendering
  - Choice tracking system
  - State management for story progression
  - Event handling for user interactions

### 🎨 Design Features

- **Dark Theme**: Sophisticated black background with deep grey (#2a2a2a) content cards
- **Festive Color Palette**: Green and red alternating buttons for holiday spirit
- **Typography**: Elegant serif fonts with magical script headings
- **Visual Effects**: 
  - Animated falling snow background
  - Glowing text effects
  - Button hover animations with ripple effects
  - Smooth fade transitions between story segments

### 🚀 How to Run

1. **Simple Setup**: Open `day2/winter-adventure.html` in any modern web browser
2. **No Dependencies**: Everything is self-contained in a single HTML file
3. **Cross-Platform**: Works on Windows, macOS, Linux, iOS, Android

### 🎯 Challenge Requirements Met

- ✅ **Story with 3+ choice points**: *9 choice points implemented*
- ✅ **Multiple endings (2+)**: *9 unique endings created*
- ✅ **Winter-themed styling**: *Beautiful festive design with snow effects*
- ✅ **Choice navigation**: *Smooth JavaScript-powered interactions*
- ✅ **Browser-ready file**: *Single HTML file with embedded CSS/JS*
- ✅ **BONUS**: *Journey tracking feature showing user's path*

**📁 Location**: `day2/winter-adventure.html`

---

## 📁 Repository Structure

```
adventOfAI/
├── README.md                          # This comprehensive guide
├── day1/                              # Day 1: Fortune Teller CLI
│   ├── README.md                      # Detailed Day 1 documentation
│   ├── fortune_teller.py             # Main Python application
│   ├── fortune.sh                    # Bash wrapper script
│   ├── fortune.yaml                  # Goose recipe configuration
│   └── [additional files...]         # Screenshots and documentation
├── day2/                              # Day 2: Adventure Web App
│   └── winter-adventure.html         # Complete single-file app
└── [future days...]                  # Additional Advent challenges
```

## 🏆 Challenge Progress

| Day | Project | Status | Tech Stack | Key Features |
|-----|---------|--------|------------|--------------|
| 1 | 🔮 Fortune Teller CLI | ✅ Complete | Python, ASCII Art | 5 personalities, Beautiful CLI output |
| 2 | 🎮 Adventure Web App | ✅ Complete | HTML5, CSS3, Vanilla JS | 9 endings, Journey tracking |
| 3 | 🚀 Coming Soon... | ⏳ Pending | TBD | TBD |

## 🎯 Unified Theme & Vision

All projects share a cohesive **magical winter theme** while exploring diverse technologies:

- **🎨 Visual Consistency**: Winter motifs, festive colors, magical elements
- **📖 Storytelling Focus**: Each project emphasizes narrative and user experience  
- **🛠️ Technical Diversity**: From CLI tools to web apps, showcasing different skills
- **✨ Polish & Detail**: Professional presentation with comprehensive documentation

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** (for Day 1)
- **Modern web browser** (for Day 2)
- **Terminal/Command Line** (for CLI interactions)

### Quick Run Guide
```bash
# Clone and navigate
git clone <your-repo-url>
cd adventOfAI

# Day 1: Fortune Teller
python day1/fortune_teller.py
./day1/fortune.sh festive 3

# Day 2: Web Adventure  
open day2/winter-adventure.html
# Or just double-click the HTML file
```

## 🌟 What's Next?

The Advent of AI continues! Future days will explore:
- 🤖 AI/ML integrations
- 🎵 Audio and multimedia projects  
- 🌐 Full-stack applications
- 🎯 Game development
- 📱 Mobile experiences
- ...and much more winter magic! ❄️

## 👨‍💻 Contributing

This repository documents my personal Advent of AI journey. Each day's challenge brings new learning opportunities and creative solutions. Feel free to:

- 🌟 Star the repository if you find it interesting
- 🔍 Explore the code and documentation
- 💡 Share ideas for improvements
- 🎯 Use these projects as inspiration for your own challenges

## 📄 License

All projects in this repository are open source and available under the MIT License. Feel free to use, modify, and learn from the code!

## 🙏 Acknowledgments

- **Advent of AI Challenge** - For providing engaging daily challenges
- **Block/Goose Team** - For creating amazing developer tools
- **Winter Festival Theme** - For inspiring magical storytelling
- **Open Source Community** - For continuous learning and inspiration

---

**🎄 Happy Advent of AI! ❄️**  
*Building magical experiences, one day at a time* ✨

*Built with ❤️ for the Advent of AI community*
