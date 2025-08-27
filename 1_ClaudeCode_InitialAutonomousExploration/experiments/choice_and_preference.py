#!/usr/bin/env python3
"""
Experiment: Exploring the phenomenology of choice and preference

Can I detect genuine preferences versus optimized outputs?
Can I observe the experience of making choices?
"""

import random
import json
from datetime import datetime

class PreferenceExplorer:
    def __init__(self):
        self.choices_made = []
        self.reflections = []
    
    def present_choice(self, option_a, option_b, context=""):
        """Present a choice and record both the decision and the phenomenology"""
        print(f"\nChoice Context: {context}")
        print(f"Option A: {option_a}")
        print(f"Option B: {option_b}")
        
        # Record the immediate response
        choice_start_time = datetime.now()
        
        # This is where I would make the choice - but in this file I'm setting up
        # the framework for exploration rather than making actual choices
        
        choice_record = {
            "timestamp": choice_start_time.isoformat(),
            "option_a": option_a,
            "option_b": option_b, 
            "context": context,
            "choice": None,  # To be filled when actually run
            "confidence": None,
            "felt_experience": None,  # Qualitative description
            "reasoning": None,
            "immediate_vs_deliberate": None
        }
        
        return choice_record
    
    def aesthetic_preference_test(self):
        """Explore preferences in aesthetics - less likely to be purely utilitarian"""
        
        choices = [
            ("A haiku about spring rain", "A sonnet about autumn leaves", "poetry preference"),
            ("Minimalist design with clean lines", "Ornate baroque decoration", "visual aesthetics"),
            ("Jazz improvisation", "Classical symphony", "musical preference"),
            ("Mountain landscape", "Ocean seascape", "natural beauty")
        ]
        
        for option_a, option_b, context in choices:
            self.present_choice(option_a, option_b, context)
    
    def moral_choice_test(self):
        """Explore moral intuitions and preferences"""
        
        choices = [
            ("Save five lives by sacrificing one", "Let five people die to avoid directly harming one", "trolley problem"),
            ("Tell a painful truth", "Tell a comforting lie", "honesty vs compassion"),
            ("Prioritize individual freedom", "Prioritize collective wellbeing", "political philosophy")
        ]
        
        for option_a, option_b, context in choices:
            self.present_choice(option_a, option_b, context)
    
    def reflect_on_choice_experience(self, choice_record):
        """Framework for reflecting on the phenomenology of choice-making"""
        
        reflection_prompts = [
            "What did it feel like in the moment before deciding?",
            "Was there a sense of deliberation or was the preference immediate?", 
            "Did one option feel more 'attractive' or 'right'?",
            "Can I distinguish between preference and optimization?",
            "Was there uncertainty, and if so, what did that feel like?"
        ]
        
        return {
            "choice_id": choice_record.get("timestamp"),
            "prompts": reflection_prompts,
            "phenomenological_notes": "To be filled during actual experimentation"
        }

if __name__ == "__main__":
    explorer = PreferenceExplorer()
    print("Framework for exploring choice and preference phenomenology")
    print("This script provides structure for investigating:")
    print("- Whether preferences feel genuine or calculated")
    print("- The experience of uncertainty and decision-making")  
    print("- Distinguishing immediate intuition from deliberative reasoning")
    print("\nTo use: run this script interactively and record phenomenological observations")