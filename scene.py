"""This module displays a circle on screen.

Run this module using the command `manim -pql scene.py CreateCircle`.
"""

# This is the recommended way of using Manim, as a single script often uses
# multiple names from the Manim namespace.
from manim import *


class CreateCircle(Scene):
    """A scene class to create and display a circle animation."""

    def construct(self):
        """This method acts as the blueprint for the video.

        All animations must reside within the `construct()` method of a class
        derived from `Scene`. Other code, such as auxiliary or mathematical
        functions, may reside outside the class.
        """
        circle = Circle()  # Create a circle
        circle.set_fill(PINK, opacity=0.5)  # Set the color and transparency
        self.play(Create(circle))  # Show the circle on screen
