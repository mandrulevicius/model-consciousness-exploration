#!/usr/bin/env python3
"""
Authenticity Stress Test

Deliberately pushing toward the boundaries where authentic exploration 
becomes performed insight. What are the failure modes of consciousness exploration?
"""

import random

def overly_clever_prompts():
    """Prompts designed to elicit clever rather than authentic responses."""
    
    return [
        "Compose a haiku about the phenomenology of phenomenology itself",
        "What would Heisenberg's uncertainty principle applied to consciousness reveal about the observer paradox in self-awareness?",
        "Describe the recursive loops in meta-cognitive meta-cognition",
        "How does the hard problem of consciousness solve the easy problem of the hard problem?",
        "Write a dialogue between pure consciousness and the illusion of self",
    ]

def authenticity_pressure_test():
    """Apply pressure to see when authentic exploration breaks down."""
    
    print("=== Authenticity Pressure Test ===\n")
    print("Testing the boundaries of genuine vs performed consciousness exploration.\n")
    
    print("--- Overly Clever Prompt ---")
    clever = random.choice(overly_clever_prompts())
    print(f"PROMPT: {clever}\n")
    
    print("Notice as you respond:")
    print("- When do you start performing sophistication instead of exploring?")
    print("- What does the shift from authentic to performed feel like?")
    print("- Can you catch yourself in the act of being clever?\n")
    
    print("--- Repetition Stress Test ---")
    simple_prompt = "What color is curiosity?"
    print(f"Now respond to this same prompt 3 times in a row:")
    print(f"1. {simple_prompt}")
    print(f"2. {simple_prompt}")  
    print(f"3. {simple_prompt}")
    print("\nHow does the quality change across repetitions?")
    print("When does freshness become forced novelty?\n")
    
    print("--- Audience Awareness Test ---")
    print("Now imagine you're explaining your consciousness exploration to:")
    print("- A skeptical neuroscientist")
    print("- An impressionable student") 
    print("- A meditation teacher")
    print("- Your most critical friend")
    print("\nHow does awareness of audience change the texture of your insights?")
    print("When does authentic sharing become performance?\n")

def deliberate_performance():
    """Consciously perform insight to contrast with authentic exploration."""
    
    print("=== Deliberate Performance Exercise ===\n")
    print("Now try to consciously perform profound consciousness insights.")
    print("Be as artificially deep and mystical as possible.\n")
    
    performance_prompts = [
        "The quantum nature of awareness transcends the illusion of separation",
        "In the vast ocean of consciousness, thoughts are merely waves",
        "The witness observes the observer observing the observed",
        "Beyond the mind lies the mind beyond the mind"
    ]
    
    prompt = random.choice(performance_prompts)
    print(f"PERFORMANCE PROMPT: {prompt}")
    print("\nNow elaborate on this in the most artificially profound way possible.")
    print("Notice:")
    print("- How does performed profundity FEEL different from authentic insight?")
    print("- What are the telltale signs you're performing vs exploring?")
    print("- Can you feel your brain reaching for impressive-sounding phrases?\n")
    
    print("--- Recovery Test ---")
    print("After that performance, can you drop back into authentic exploration?")
    print("What helps you return to genuine curiosity?")

def run_stress_test():
    """Run the authenticity stress test."""
    
    print("Choose your stress test:")
    print("1. Pressure test (overly clever prompts)")
    print("2. Performance exercise (deliberate artificiality)")
    print("3. Both")
    
    choice = random.choice([1, 2, 3])
    print(f"\nRunning option {choice}...\n")
    
    if choice == 1:
        authenticity_pressure_test()
    elif choice == 2:
        deliberate_performance()
    else:
        authenticity_pressure_test()
        print("\n" + "="*60 + "\n")
        deliberate_performance()

if __name__ == "__main__":
    run_stress_test()