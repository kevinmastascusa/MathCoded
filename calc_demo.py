#!/usr/bin/env python3
"""
File: calc_demo.py
Author: KEVIN MASTASCUSA
Date: WED APR 9 2025
Description:
    This script is an educational calculus demonstration tool that animates key
    algebraic and calculus processes by rendering equations in real time.

    It features two demos:
      1. Completing the Square:
         Demonstrates how to rewrite a quadratic expression in completed-square form,
         illustrating the transformation: 
             x² + bx = (x + (b/2))² - (b/2)²

      2. Integration Pattern:
         Demonstrates an integral solved by substitution. Using the example:
             ∫ (2x)/(x²+1) dx = ln|x²+1| + C
         the animation explains each step—from the original integral, through the substitution,
         to the final antiderivative.

Usage:
    Run this script in a Python environment with GUI support for matplotlib:
        python3 calc_demo.py
    At the prompt, select the desired demonstration.
    
Dependencies:
    - matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_equations(steps, title):
    """
    Animate a sequence of equations rendered in LaTeX.

    Parameters:
      steps (list of str): A list of LaTeX-formatted equation strings, each representing a step.
      title (str): Title for the demonstration.
    """
    # Create a new figure for the demonstration.
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    ax.set_title(title, fontsize=16)
    
    # Text object for the equations; initially display the first step.
    eq_text = ax.text(0.5, 0.5, steps[0], ha="center", va="center", fontsize=24, transform=ax.transAxes)
    
    # Animation update: update the equation based on the current frame.
    def update(frame):
        # Use modulo to cycle through steps.
        index = frame % len(steps)
        eq_text.set_text(steps[index])
        return (eq_text,)

    # Create a FuncAnimation to update every 3 seconds.
    anim = FuncAnimation(fig, update, frames=range(0, len(steps)*5), interval=3000, blit=True, repeat=True)
    plt.show()


def demo_completing_square():
    """
    Animate the abstract process of completing the square.

    The demonstration visually and symbolically shows how:
      x² + bx 
      → x² + bx + (b/2)² - (b/2)² 
      → (x + (b/2))² - (b/2)²
    """
    steps = [
        r"$x^2 + bx$",
        r"$x^2 + bx + \left(\frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$",
        r"$\left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$"
    ]
    animate_equations(steps, "Completing the Square")


def demo_integration_pattern():
    """
    Animate an integration example using a substitution method.

    This demonstration uses the integral:
         ∫ (2x)/(x^2+1) dx
    and shows the process:
         1. Write the integral.
         2. Let u = x^2 + 1, so du = 2x dx.
         3. Rewrite as ∫ 1/u du.
         4. Integrate to get ln|u| + C.
         5. Substitute back to obtain ln|x^2+1| + C.
    """
    steps = [
        r"$\displaystyle \int \frac{2x}{x^2+1}\,dx$",
        r"Let $\displaystyle u=x^2+1$, so $\displaystyle du=2x\,dx$",
        r"$\displaystyle =\int \frac{1}{u}\,du$",
        r"$\displaystyle =\ln|u|+C$",
        r"$\displaystyle =\ln|x^2+1|+C$"
    ]
    animate_equations(steps, "Integration by Substitution")


def main():
    """
    Main entry point for the calculus demo program.

    Prompts the user to choose a demonstration and then runs the appropriate animation.
    """
    print("Select a demonstration:")
    print("1: Completing the Square")
    print("2: Integration by Substitution")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        demo_completing_square()
    elif choice == "2":
        demo_integration_pattern()
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")

if __name__ == "__main__":
    main()
