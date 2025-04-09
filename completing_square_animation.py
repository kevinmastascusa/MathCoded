#!/usr/bin/env python3
"""
File: completing_square_animation.py
Author: Kevin Mastascusa
Date: Wed Apr 9, 2025
Description:
    This script provides an animated, visual demonstration of the "completing the square"
    process. It shows how an L-shaped region—composed of a square (x²) and two rectangular pieces 
    (each representing x · (b/2))—can be completed into a perfect square with the missing piece 
    (b/2)². In the animation, the missing piece gradually appears and then the complete square 
    outline (representing (x + b/2)²) is revealed. All labels use symbolic notation (e.g., x², (b/2)²) 
    to focus on the geometric transformation rather than numeric details.
    
Usage:
    Run this script in a Python environment with GUI support for matplotlib:
        python3 completing_square_animation.py

Dependencies:
    - matplotlib
    - numpy
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation

def animate_completing_square():
    """
    Animate the completing-the-square process.

    The animation illustrates:
      - An original square representing x².
      - Two rectangles, each representing x · (b/2).
      - A missing square (b/2)² that gradually appears.
      - The final complete square (x + b/2)² outlined with a dashed line.
    All labels are symbolic to emphasize the geometric rearrangement.
    """
    # Setup figure and axis.
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.1, 1.6)
    ax.set_ylim(-0.1, 1.6)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes for a clean, instructional look.

    # For visualization purposes: assume x = 1 and b/2 = 0.5.
    x = 1.0
    b_half = 0.5
    complete_side = x + b_half  # Total side length of the completed square.

    # ---------------------------
    # Create the component patches.
    # ---------------------------
    # 1. x² (the original square)
    square_x2 = Rectangle((0, 0), x, x, facecolor='#ADD8E6', edgecolor='black', lw=2)
    ax.add_patch(square_x2)
    ax.text(0.5 * x, 0.5 * x, "x²", ha='center', va='center', fontsize=14, color='black')

    # 2. The two rectangles representing x · (b/2)
    rect_R1 = Rectangle((x, 0), b_half, x, facecolor='#90EE90', edgecolor='black', lw=2)  # Right rectangle
    rect_R2 = Rectangle((0, x), x, b_half, facecolor='#90EE90', edgecolor='black', lw=2)  # Top rectangle
    ax.add_patch(rect_R1)
    ax.add_patch(rect_R2)
    ax.text(x + 0.5 * b_half, 0.5 * x, "x·(b/2)", ha='center', va='center', fontsize=12, color='black')
    ax.text(0.5 * x, x + 0.5 * b_half, "x·(b/2)", ha='center', va='center', fontsize=12, color='black')

    # 3. The missing square (representing (b/2)²), initially invisible.
    missing_piece = Rectangle((x, x), b_half, b_half, facecolor='#FFB6C1', edgecolor='black', lw=2, alpha=0)
    ax.add_patch(missing_piece)
    missing_text = ax.text(x + 0.5 * b_half, x + 0.5 * b_half, "(b/2)²", ha='center', va='center', fontsize=12, color='black', alpha=0)

    # 4. The complete square outline (representing (x + b/2)²), initially invisible.
    complete_square_outline = Rectangle((0, 0), complete_side, complete_side, fill=False, edgecolor='red', lw=2, linestyle='--', alpha=0)
    ax.add_patch(complete_square_outline)
    complete_text = ax.text(complete_side/2, complete_side/2, "(x + b/2)²", ha='center', va='center', fontsize=16, color='red', alpha=0)

    # ---------------------------
    # Animation update function.
    # ---------------------------
    def update(frame):
        """
        Update the animation for the given frame.

        Frames 0-50: Gradually reveal the missing square (b/2)².
        Frames 51-100: Gradually reveal the complete square outline (x + b/2)².
        """
        if frame <= 50:
            # Phase 1: Gradually reveal the missing piece.
            new_alpha = frame / 50.0  # Interpolate alpha from 0 to 1.
            missing_piece.set_alpha(new_alpha)
            missing_text.set_alpha(new_alpha)
        else:
            # Phase 2: Gradually reveal the complete square's outline and label.
            progress = (frame - 50) / 50.0  # Interpolate from 0 to 1.
            complete_square_outline.set_alpha(progress)
            complete_text.set_alpha(progress)
        return missing_piece, missing_text, complete_square_outline, complete_text

    # Create and run the animation.
    anim = FuncAnimation(fig, update, frames=101, interval=50, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    animate_completing_square()
