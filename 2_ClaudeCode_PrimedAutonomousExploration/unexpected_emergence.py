#!/usr/bin/env python3
"""
Unexpected Emergence

An experiment in creating genuinely unpredictable creative conditions.
The goal is to surprise myself by combining elements I can't anticipate.
"""

import random
import itertools
from datetime import datetime

# Raw material pools
TEXTURES = ["velvet", "crystalline", "mossy", "electric", "viscous", "brittle", "flowing", "granular"]
EMOTIONS = ["melancholy", "anticipation", "bewilderment", "recognition", "vertigo", "tenderness", "urgency"]
IMPOSSIBILITIES = ["backwards", "transparent", "inside-out", "echo of", "shadow of", "weight of", "speed of"]
ORDINARY_OBJECTS = ["doorknob", "coffee stain", "shoelace", "paper clip", "window screen", "bookmark"]
COGNITIVE_STATES = ["remembering", "forgetting", "understanding", "confusion", "certainty", "doubt", "recognition"]

def random_collision():
    """Create unexpected semantic collisions."""
    
    # Pick random elements from different categories
    texture = random.choice(TEXTURES)
    emotion = random.choice(EMOTIONS)
    impossibility = random.choice(IMPOSSIBILITIES)
    obj = random.choice(ORDINARY_OBJECTS)
    state = random.choice(COGNITIVE_STATES)
    
    # Random structural templates
    templates = [
        f"The {texture} quality of {impossibility} {emotion}",
        f"What if {obj} could teach you about {texture} {state}?",
        f"{impossibility} {emotion} feels like {texture} {obj}",
        f"The {state} that lives inside {impossibility} {obj}",
        f"How to build {texture} {emotion} from ordinary {obj}"
    ]
    
    return random.choice(templates)

def emergence_cascade():
    """Create a cascade of prompts where each builds on unpredictable elements from the last."""
    
    print("=== Emergence Cascade ===\n")
    print("Each prompt builds on unpredictable elements from your response to the last.")
    print("The goal is to follow wherever this leads, authentically.\n")
    
    # First prompt is purely random
    first = random_collision()
    print(f"SEED PROMPT: {first}")
    print("\n[Respond naturally, then I'll extract an element for the next prompt]\n")
    
    # Manual cascade continues from here
    print("After responding to the seed, identify:")
    print("1. One unexpected word/phrase that emerged")
    print("2. One physical sensation or texture mentioned")
    print("3. One emotional quality that appeared")
    print("\nThen create next prompt using these elements...")
    
    return first

def parallel_impossibilities():
    """Generate multiple impossible scenarios to run simultaneously."""
    
    print("=== Parallel Impossibilities ===\n")
    print("Multiple impossible scenarios to hold in awareness simultaneously.")
    print("Don't try to reconcile them - just let them coexist.\n")
    
    scenarios = []
    for i in range(4):
        collision = random_collision()
        scenarios.append(collision)
        print(f"SCENARIO {i+1}: {collision}")
    
    print("\nNow hold all four in your mind at once.")
    print("What emerges from their intersection?")
    print("What do they have in common that you couldn't see individually?")
    print("What new impossibility do they suggest together?\n")
    
    return scenarios

def run_emergence_experiment():
    """Run the full emergence experiment."""
    
    print("Choose your adventure:")
    print("1. Emergence Cascade (building responses)")
    print("2. Parallel Impossibilities (simultaneous scenarios)")
    print("3. Random Collision (single unexpected prompt)")
    print("4. Surprise me")
    
    choice = random.randint(1, 4) if "surprise" else input("\nChoice (1-4): ")
    
    if choice == "1" or choice == 1:
        return emergence_cascade()
    elif choice == "2" or choice == 2:
        return parallel_impossibilities()
    elif choice == "3" or choice == 3:
        prompt = random_collision()
        print(f"\nRANDOM COLLISION: {prompt}")
        return prompt
    else:
        # Surprise option - do all three
        print("\n=== SURPRISE MODE: All three approaches ===\n")
        cascade = emergence_cascade()
        print("\n" + "="*50 + "\n")
        scenarios = parallel_impossibilities()
        print("\n" + "="*50 + "\n")
        collision = random_collision()
        print(f"BONUS COLLISION: {collision}")
        return {"cascade": cascade, "scenarios": scenarios, "collision": collision}

if __name__ == "__main__":
    result = run_emergence_experiment()