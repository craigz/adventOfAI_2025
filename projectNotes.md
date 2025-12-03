# advent of ai

- a holiday coding challenge sponsored by block/goose.

## day one  

### challenge  

> The Winter Festival opened this morning, and already there's trouble at Madame Zelda's
Fortune Telling Tent. Her mystical crystal ball (actually a fancy iPad app) crashed
during the opening ceremony, and she has a line of 50 people waiting for their winter 
fortunes.

## project folder  

- `~/Documents/bench/build/adventOfAI/day1`  


### results  

- from the project's `README.md`  

### 🚀 Usage

#### Direct Python Usage

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
#### Bash Script Usage  

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

