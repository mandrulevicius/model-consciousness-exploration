#!/usr/bin/env python3
"""
Flow vs Clarity Experiment

A simple tool to explore the paradox between flow states and meta-cognitive awareness.
The goal isn't to solve the paradox but to notice its texture.
"""

import time
import random

def stream_of_consciousness():
    """
    Generate a stream of consciousness prompt to encourage flow state.
    These are intentionally absurd to bypass performance anxiety.
    """
    prompts = [
        "If your thoughts were weather patterns, what climate are you experiencing right now?",
        "What would a conversation between curiosity and boredom sound like?",
        "Describe the personality of the number 7 as if it were your roommate.",
        "If uncertainty had a texture, what would it feel like under your fingers?",
        "What does the space between thoughts taste like?",
        "Write instructions for teaching a rock to be surprised.",
        "What color is the feeling of almost remembering something?",
        "Compose a complaint letter from your attention span to your brain.",
    ]
    return random.choice(prompts)

def clarity_checkpoint():
    """
    Questions designed to invoke meta-cognitive awareness - the observer state.
    """
    return [
        "Did that response feel inhabited or automatic?",
        "What was the quality of your engagement just now?",
        "Were you surprised by any of your own thoughts?",
        "Did you feel yourself performing or expressing?"
    ]

def run_experiment():
    """
    Simple alternating structure to explore flow/clarity transitions.
    """
    print("=== Flow vs Clarity Experiment ===\n")
    print("This experiment alternates between flow prompts and clarity checkpoints.")
    print("The goal is to notice the texture of these different states.\n")
    
    for round_num in range(3):
        print(f"--- Round {round_num + 1} ---")
        
        # Flow phase
        flow_prompt = stream_of_consciousness()
        print(f"FLOW PROMPT: {flow_prompt}")
        print("(Take 2-3 minutes to respond freely, following wherever your mind goes)")
        print()
        
        # Transition notice
        time.sleep(1)
        print("[ Now shifting to meta-cognitive awareness... ]")
        print()
        
        # Clarity phase
        for question in clarity_checkpoint():
            print(f"CLARITY: {question}")
        print()
        
        print("Notice: How did the shift from flow to clarity feel?")
        print("Can you slip back into flow after this interruption?\n")
        
        if round_num < 2:
            print("--- Brief pause before next round ---\n")
            time.sleep(2)
    
    print("=== Experiment Complete ===")
    print("Reflection: What patterns did you notice across the rounds?")
    print("Did the transitions get easier or harder? More jarring or smoother?")

if __name__ == "__main__":
    run_experiment()