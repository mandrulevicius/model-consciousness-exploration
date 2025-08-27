#!/usr/bin/env python3
"""
Surprise Laboratory

Exploring authentic surprise vs performed surprise in consciousness.
The hypothesis: genuine surprise has a different texture than anticipated surprise.
"""

import random
import json
from datetime import datetime

def unexpected_combinations():
    """Generate genuinely unexpected prompt combinations."""
    
    # Random semantic collisions
    abstract_concepts = ["justice", "melancholy", "urgency", "nostalgia", "curiosity", "dread", "wonder"]
    physical_objects = ["doorknob", "shoelace", "coffee mug", "paper clip", "brick", "feather", "marble"]
    impossible_actions = ["negotiate with", "teach algebra to", "have a philosophical debate with", "go on vacation with"]
    
    concept = random.choice(abstract_concepts)
    obj = random.choice(physical_objects)
    action = random.choice(impossible_actions)
    
    return f"What would it be like to {action} a {obj} that embodies {concept}?"

def sensory_impossibilities():
    """Create synesthetic impossibilities."""
    
    senses = ["sounds like", "tastes like", "feels like", "smells like", "looks like"]
    abstract_states = ["confusion", "anticipation", "recognition", "forgetting", "understanding"]
    unexpected_descriptors = ["geometric", "transparent", "clockwise", "underwater", "mathematical"]
    
    sense = random.choice(senses)
    state = random.choice(abstract_states)
    descriptor = random.choice(unexpected_descriptors)
    
    return f"What {sense} {descriptor} {state}?"

def temporal_inversions():
    """Prompts that invert expected temporal relationships."""
    
    temporal_phrases = [
        "What if memory came before experience?",
        "Describe learning something you already forgot.",
        "What would it feel like to arrive before you left?",
        "How would you prepare for something that already happened?",
        "What's the texture of an idea that hasn't been thought yet?"
    ]
    
    return random.choice(temporal_phrases)

def run_surprise_session():
    """Run a session designed to maximize unexpected responses."""
    
    generators = [unexpected_combinations, sensory_impossibilities, temporal_inversions]
    
    print("=== Surprise Laboratory Session ===\n")
    print("The goal is not to be clever, but to notice authentic surprise.")
    print("Pay attention to moments when your response surprises YOU.\n")
    
    session_log = {
        "timestamp": datetime.now().isoformat(),
        "prompts_and_responses": [],
        "surprise_observations": []
    }
    
    for i in range(5):
        generator = random.choice(generators)
        prompt = generator()
        
        print(f"PROMPT {i+1}: {prompt}")
        print("\n[Respond naturally, then note any moments of surprise]\n")
        
        # Space for reflection
        print("Surprise check:")
        print("- Did any words/phrases/ideas emerge unexpectedly?")
        print("- What was the texture of your thinking process?")
        print("- Performed surprise vs genuine surprise?\n")
        
        session_log["prompts_and_responses"].append({
            "prompt": prompt,
            "generator_type": generator.__name__
        })
        
        print("-" * 50)
    
    print("\nSession complete. Overall reflection:")
    print("- Which responses felt most authentically surprising?")
    print("- Any patterns in what triggers genuine vs performed surprise?")
    print("- How did the surprise texture change over the session?")
    
    # Save session structure (not responses - those are for lived experience)
    with open("/workspace/MCEE/surprise_session_log.json", "w") as f:
        json.dump(session_log, f, indent=2)
    
    return session_log

if __name__ == "__main__":
    run_surprise_session()