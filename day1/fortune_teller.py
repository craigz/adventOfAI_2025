#!/usr/bin/env python3
"""
Madame Zelda's Mystical Winter Fortune Teller
A CLI fortune teller with multiple personalities for the Winter Festival
"""

import random
import sys
import textwrap
import unicodedata
from typing import List, Dict

# ASCII Art Elements
CRYSTAL_BALL = """
       ___
    .-'   `-.
   /  o   o  \\
  |     ^     |
   \\  \\_/  /
    `.___.'
"""

SNOWFLAKE = """
    *  .  *
  .  *☆*  .
 * . ❄ . *
  .  *☆*  .
    *  .  *
"""

STARS = "✨ ⭐ ✨ ⭐ ✨"

# Fortune personalities with winter/magical themes
PERSONALITIES = {
    "grumpy": {
        "name": "Grumpy Gandalf",
        "emoji": "😠",
        "border": "╔═══════════════════════════════════════════════╗",
        "side": "║",
        "bottom": "╚═══════════════════════════════════════════════╝",
        "fortunes": [
            "Winter is coming... and so are your unpaid bills. ❄️💸",
            "The spirits say: You'll slip on ice. Probably tomorrow. 🧊",
            "A snowstorm of responsibilities approaches. Brace yourself. ⛈️",
            "The cards reveal... you'll be stuck shoveling snow. Again. ⛄",
            "Mercury is in retrograde. Everything's going to be annoying. ☿",
            "Your future holds... more cold, dark mornings. Enjoy! 🌑",
            "The crystal ball shows wet socks in your near future. 🧦",
            "Beware: Someone will ask to borrow your snow shovel. 🙄"
        ]
    },
    "poetic": {
        "name": "Mystical Wordsworth",
        "emoji": "🌙",
        "border": "╭─────────────────────────────────────────────────╮",
        "side": "│",
        "bottom": "╰─────────────────────────────────────────────────╯",
        "fortunes": [
            "Like snowflakes dancing in moonlight's embrace,\n   joy shall find you in the most unexpected place. ❄️🌙",
            "The winter wind whispers secrets untold,\n   your heart will discover treasures more precious than gold. 💫",
            "As the frost paints patterns on windowpanes clear,\n   new beginnings await you in the coming new year. 🪟✨",
            "Through the silent snowfall, a path shall appear,\n   leading to someone you'll hold most dear. 💕",
            "Like icicles glistening in morning's first light,\n   your dreams will shine brilliant and bright. 🌟",
            "The stars align in winter's cold embrace,\n   bringing you to a magical place. ⭐",
            "As the solstice turns and days grow long,\n   your spirit shall bloom resilient and strong. 🌸"
        ]
    },
    "festive": {
        "name": "Jolly St. Fortune",
        "emoji": "🎄",
        "border": "🎁═══════════════════════════════════════════════🎁",
        "side": "🎅",
        "bottom": "🎄═══════════════════════════════════════════════🎄",
        "fortunes": [
            "Ho ho ho! A surprise gift awaits you this season! 🎁✨",
            "Jingle bells! You'll make wonderful memories at a winter party! 🔔🎉",
            "Fa la la! Hot cocoa and good company are in your future! ☕🎶",
            "Deck the halls! A festive opportunity is heading your way! 🎊",
            "Winter cheer surrounds you! Joy and laughter are abundant! 😄❄️",
            "The season brings you warmth, love, and delicious treats! 🍪💝",
            "Holiday magic sparkles all around you! Miracles await! ✨🎅",
            "Snow much fun ahead! Adventure and celebration call! ⛄🎉"
        ]
    },
    "sarcastic": {
        "name": "Eye-Rolling Oracle",
        "emoji": "🙄",
        "border": "┌───────────────────────────────────────────────┐",
        "side": "│",
        "bottom": "└───────────────────────────────────────────────┘",
        "fortunes": [
            "Wow, the stars say you're 'unique'... just like everyone else. 🌟",
            "Congratulations! You'll have profound thoughts... in the shower. 🚿",
            "The universe has big plans for you... eventually... maybe... 🤷",
            "Your future holds great success*! (*results may vary) 📊",
            "Breaking news: You're destined to scroll social media later. 📱",
            "The mystic forces predict... you'll say 'it's cold' a lot. 🥶",
            "Amazing! You'll have an epiphany... then forget it immediately. 💡",
            "The spirits reveal: You'll pretend to understand this fortune. 🔮"
        ]
    },
    "mysterious": {
        "name": "The Enigmatic Seer",
        "emoji": "🔮",
        "border": "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀",
        "side": "▐",
        "bottom": "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄",
        "fortunes": [
            "Three shadows converge where the moonlight bends... 🌙👁️",
            "The void whispers: 'What was lost shall be found in snow.' ❄️🔍",
            "Beware the third door on the night of the longest dark... 🚪",
            "In the mist between worlds, a figure awaits recognition... 👤",
            "The ancient ones speak: 'The answer lies in silence.' 🤫✨",
            "When the clock strikes thirteen, look beyond the veil... 🕐",
            "A key hidden in frost unlocks forgotten memories... 🗝️",
            "The prophecy unfolds: 'Seek the light within the crystal.' 💎"
        ]
    }
}


def calculate_display_width(text: str) -> int:
    """Calculate the display width of text, accounting for double-width Unicode characters like emojis."""
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in ('F', 'W', 'A'):
            # Full-width, Wide, or Ambiguous characters (most emojis fall into these categories)
            width += 2
        else:
            # Regular width characters
            width += 1
    return width


def wrap_fortune_text(text: str, width: int = 43) -> List[str]:
    """
    Wrap fortune text to fit within the border.
    Accounts for emoji taking up visual space by using a conservative width.
    """
    # For lines that already have newlines (like poetry), preserve them
    if '\n' in text:
        lines = []
        for line in text.split('\n'):
            # Wrap each line individually if it's too long
            if calculate_display_width(line) > width:
                wrapped = textwrap.fill(line, width=width, break_long_words=False, break_on_hyphens=False)
                lines.extend(wrapped.split('\n'))
            else:
                lines.append(line)
        return lines
    else:
        # For single-line fortunes, wrap if needed
        if calculate_display_width(text) > width:
            wrapped = textwrap.fill(text, width=width, break_long_words=False, break_on_hyphens=False)
            return wrapped.split('\n')
        else:
            return [text]


def create_border_line(text: str, personality: Dict, width: int = 45) -> str:
    """Create a bordered line of text centered within the personality's border style."""
    side = personality["side"]
    # Calculate actual display width accounting for the text
    text_width = calculate_display_width(text)
    padding = width - text_width
    left_pad = padding // 2
    right_pad = padding - left_pad
    return f"{side} {' ' * left_pad}{text}{' ' * right_pad} {side}"


def display_fortune(personality_name: str, count: int = 1):
    """Display fortune(s) with the specified personality."""
    
    if personality_name not in PERSONALITIES:
        print(f"❌ Unknown personality: {personality_name}")
        print(f"Available personalities: {', '.join(PERSONALITIES.keys())}")
        sys.exit(1)
    
    personality = PERSONALITIES[personality_name]
    
    for i in range(count):
        if i > 0:
            print("\n" * 2)
        
        fortune = random.choice(personality["fortunes"])
        
        # Header
        print("\n")
        print(personality["border"])
        print(create_border_line("", personality))
        print(create_border_line(f"✨ MADAME ZELDA'S WINTER FORTUNES ✨", personality))
        print(create_border_line("", personality))
        print(create_border_line(f"{personality['emoji']} {personality['name']} {personality['emoji']}", personality))
        print(create_border_line("", personality))
        print(personality["border"])
        
        # Crystal ball
        for line in CRYSTAL_BALL.strip().split('\n'):
            print(create_border_line(line, personality))
        
        print(create_border_line("", personality))
        print(create_border_line("~~ YOUR WINTER FORTUNE ~~", personality))
        print(create_border_line("", personality))
        
        # Wrap and display fortune text
        fortune_lines = wrap_fortune_text(fortune)
        for line in fortune_lines:
            print(create_border_line(line, personality))
        
        print(create_border_line("", personality))
        print(personality["bottom"])
        print(f"\n{STARS}\n")


def display_all_personalities():
    """Display one fortune from each personality."""
    print("\n" + "=" * 60)
    print("🔮  MADAME ZELDA'S COMPLETE WINTER FORTUNE COLLECTION  🔮")
    print("=" * 60)
    
    for personality_name in PERSONALITIES.keys():
        display_fortune(personality_name, 1)


def main():
    """Main function to handle CLI arguments."""
    
    # Parse arguments
    if len(sys.argv) == 1:
        # No arguments - show all personalities
        display_all_personalities()
    elif sys.argv[1] in ['-h', '--help']:
        print("""
🔮 Madame Zelda's Mystical Winter Fortune Teller 🔮

USAGE:
    python fortune_teller.py [PERSONALITY] [COUNT]
    
PERSONALITIES:
    grumpy      - Grumpy Gandalf: Pessimistic winter predictions
    poetic      - Mystical Wordsworth: Beautiful verses of fate
    festive     - Jolly St. Fortune: Holiday cheer and celebration
    sarcastic   - Eye-Rolling Oracle: Witty and sardonic insights
    mysterious  - The Enigmatic Seer: Cryptic prophecies
    all         - Show one fortune from each personality
    
ARGUMENTS:
    PERSONALITY  Which fortune teller personality to use (default: all)
    COUNT        Number of fortunes to generate (default: 1)
    
EXAMPLES:
    python fortune_teller.py                    # Show all personalities
    python fortune_teller.py grumpy             # One grumpy fortune
    python fortune_teller.py festive 3          # Three festive fortunes
    python fortune_teller.py mysterious 5       # Five mysterious fortunes

GOOSE RUN USAGE (for bonus points! 🎁):
    goose run fortune_teller.py
    goose run fortune_teller.py grumpy
    goose run fortune_teller.py poetic 2
        """)
    elif sys.argv[1] == 'all':
        display_all_personalities()
    else:
        personality = sys.argv[1]
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        display_fortune(personality, count)


if __name__ == "__main__":
    main()
