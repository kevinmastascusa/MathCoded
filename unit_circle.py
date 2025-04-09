import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def interactive_unit_circle():
    """
    Create an interactive unit circle visualization.
    
    Features:
    • The unit circle is drawn with x = cos(θ) and y = sin(θ).
    • A slider lets you adjust the angle θ (in degrees).
    • As you change the angle, a radius from the origin to the circle is updated.
    • The horizontal and vertical projection lines display the cosine and sine values.
    • Educational annotations display the computed cosine and sine.
    """
    # Create the figure and axis for the plot.
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.subplots_adjust(left=0.1, bottom=0.25)  # leave space at the bottom for the slider
    
    # Plot the fixed unit circle.
    theta_full = np.linspace(0, 2 * np.pi, 400)
    x_full = np.cos(theta_full)
    y_full = np.sin(theta_full)
    ax.plot(x_full, y_full, label="Unit Circle", color="navy")
    
    # Draw x and y axes.
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    
    # Keep the aspect ratio equal.
    ax.set_aspect("equal", "box")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    
    # Set the title and labels.
    ax.set_title("Interactive Unit Circle")
    ax.set_xlabel("Cosine (x)")
    ax.set_ylabel("Sine (y)")
    
    # Initial angle in degrees.
    initial_angle_deg = 45
    initial_angle_rad = np.radians(initial_angle_deg)
    x_val = np.cos(initial_angle_rad)
    y_val = np.sin(initial_angle_rad)
    
    # Plot the dynamic radius line for the current angle.
    radius_line, = ax.plot([0, x_val], [0, y_val], linestyle="--", linewidth=2,
                            color="orange", label="Radius")
    
    # Plot the projection lines: vertical (sine) and horizontal (cosine).
    cosine_line, = ax.plot([x_val, x_val], [0, y_val], linestyle=":", color="green")
    sine_line, = ax.plot([0, x_val], [y_val, y_val], linestyle=":", color="green")
    
    # Add text annotations for cosine and sine values.
    cosine_text = ax.text(x_val/2, -0.1, f"cos({initial_angle_deg}°) = {x_val:.2f}",
                          ha="center", fontsize=10, color="purple")
    sine_text = ax.text(-0.5, y_val/2, f"sin({initial_angle_deg}°) = {y_val:.2f}",
                        ha="center", fontsize=10, color="purple")
    
    # Display an informational annotation box on the side.
    info_text = ax.text(1.1, 0.5,
                        "Unit Circle Basics:\n"
                        "x = cos(θ)   y = sin(θ)\n"
                        f"For θ = {initial_angle_deg}°:\n"
                        f"cos ≈ {x_val:.2f}, sin ≈ {y_val:.2f}",
                        fontsize=10, bbox=dict(facecolor="lightyellow", alpha=0.5))
    
    # Add legend.
    ax.legend()

    # Create an axis for the slider.
    slider_axis = plt.axes([0.1, 0.1, 0.8, 0.05])
    angle_slider = Slider(slider_axis, "Angle (°)", 0, 360, valinit=initial_angle_deg)

    def update(val):
        """Update the plot elements based on the slider value."""
        angle_deg = angle_slider.val
        angle_rad = np.radians(angle_deg)
        x_val = np.cos(angle_rad)
        y_val = np.sin(angle_rad)
        
        # Update the radius line.
        radius_line.set_data([0, x_val], [0, y_val])
        # Update the projection lines.
        cosine_line.set_data([x_val, x_val], [0, y_val])
        sine_line.set_data([0, x_val], [y_val, y_val])
        
        # Update the text annotations.
        cosine_text.set_text(f"cos({angle_deg:.1f}°) = {x_val:.2f}")
        cosine_text.set_position((x_val/2, -0.1))
        sine_text.set_text(f"sin({angle_deg:.1f}°) = {y_val:.2f}")
        sine_text.set_position((-0.5, y_val/2))
        
        # Update the info box.
        info_text.set_text(
            "Unit Circle Basics:\n"
            "x = cos(θ)   y = sin(θ)\n"
            f"For θ = {angle_deg:.1f}°:\n"
            f"cos ≈ {x_val:.2f}, sin ≈ {y_val:.2f}"
        )
        
        fig.canvas.draw_idle()

    angle_slider.on_changed(update)
    plt.show()


if __name__ == "__main__":
    interactive_unit_circle()
