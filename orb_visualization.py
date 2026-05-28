"""
Jarvis Orb Visualization Module
Smooth animated orb for visual feedback and interface
"""

import time
import sys
from typing import List
from enum import Enum


class OrbState(Enum):
    """Possible states for the orb"""
    IDLE = "idle"
    LISTENING = "listening"
    PROCESSING = "processing"
    RESPONDING = "responding"
    ERROR = "error"


class JarvisOrb:
    """Animated Orb for Jarvis Assistant"""
    
    def __init__(self, size: int = 5):
        self.size = size
        self.state = OrbState.IDLE
        self.is_animating = False
        self.pulse_intensity = 0
        
    def _get_idle_frame(self, frame: int) -> str:
        """Generate idle state frame"""
        frames = [
            "◯ ◯ ◯ ◯ ◯",
            "◯ ◯ ◯ ◯ ◯",
            "◯ ◯ ◯ ◯ ◯",
        ]
        return frames[frame % len(frames)]
    
    def _get_listening_frame(self, frame: int) -> str:
        """Generate listening state frame with expanding waves"""
        frames = [
            "  ◯ ◯ ◯  ",
            " ◯ ◯ ◯ ◯ ",
            "◯ ◯ ◯ ◯ ◯",
        ]
        return frames[frame % len(frames)]
    
    def _get_processing_frame(self, frame: int) -> str:
        """Generate processing state frame with rotation"""
        frames = [
            "● ◯ ◯ ◯ ◯",
            "◯ ● ◯ ◯ ◯",
            "◯ ◯ ● ◯ ◯",
            "◯ ◯ ◯ ● ◯",
            "◯ ◯ ◯ ◯ ●",
        ]
        return frames[frame % len(frames)]
    
    def _get_responding_frame(self, frame: int) -> str:
        """Generate responding state frame with pulsing"""
        frames = [
            "◯ ◯ ◯ ◯ ◯",
            "◉ ◯ ◯ ◯ ◉",
            "◉ ◉ ◯ ◉ ◉",
            "◯ ◉ ● ◉ ◯",
            "◉ ◯ ◯ ◯ ◉",
        ]
        return frames[frame % len(frames)]
    
    def _get_error_frame(self, frame: int) -> str:
        """Generate error state frame"""
        frames = [
            "✗ ◯ ◯ ◯ ✗",
            "◯ ✗ ◯ ✗ ◯",
            "✗ ◯ ◯ ◯ ✗",
        ]
        return frames[frame % len(frames)]
    
    def animate(self, state: OrbState, duration: float = 2.0) -> None:
        """Animate the orb with smooth transitions"""
        self.state = state
        self.is_animating = True
        
        start_time = time.time()
        frame = 0
        
        print(f"\n[Orb State: {state.value.upper()}]")
        
        while time.time() - start_time < duration and self.is_animating:
            if state == OrbState.IDLE:
                output = self._get_idle_frame(frame)
            elif state == OrbState.LISTENING:
                output = self._get_listening_frame(frame)
            elif state == OrbState.PROCESSING:
                output = self._get_processing_frame(frame)
            elif state == OrbState.RESPONDING:
                output = self._get_responding_frame(frame)
            elif state == OrbState.ERROR:
                output = self._get_error_frame(frame)
            else:
                output = "◯ ◯ ◯ ◯ ◯"
            
            sys.stdout.write(f"\r{output}")
            sys.stdout.flush()
            
            frame += 1
            time.sleep(0.1)
        
        print("\n")
    
    def pulse(self, intensity: int = 3) -> None:
        """Create a pulsing effect"""
        for _ in range(intensity):
            self.animate(OrbState.RESPONDING, duration=0.5)
    
    def flash_error(self) -> None:
        """Flash error indication"""
        for _ in range(2):
            self.animate(OrbState.ERROR, duration=0.3)
    
    def reset(self) -> None:
        """Reset orb to idle state"""
        self.state = OrbState.IDLE
        self.is_animating = False
        self.pulse_intensity = 0


def demonstrate_orb():
    """Demonstrate orb visualization"""
    print("=" * 50)
    print("JARVIS ORB VISUALIZATION DEMO")
    print("=" * 50)
    
    orb = JarvisOrb()
    
    states_demo = [
        (OrbState.IDLE, "Idle state - waiting for input"),
        (OrbState.LISTENING, "Listening state - processing audio"),
        (OrbState.PROCESSING, "Processing state - analyzing input"),
        (OrbState.RESPONDING, "Responding state - generating output"),
    ]
    
    for state, description in states_demo:
        print(f"\n→ {description}")
        orb.animate(state, duration=2.0)
    
    print("→ Error demonstration")
    orb.flash_error()
    
    print("✓ Orb demonstration complete!")


if __name__ == "__main__":
    demonstrate_orb()
