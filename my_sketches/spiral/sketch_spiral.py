import vsketch
import numpy as np
import random


class SpiralSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=True)
        vsk.scale("cm")

        # Parameters for the spiral
        num_points = 1000
        max_radius = 10  # Maximum radius of the spiral
        noise_scale = 0.1  # Scale of the noise
        rotations = 10  # Number of rotations in the spiral

        # Generate the points of the spiral
        theta = np.linspace(0, rotations * 2 * np.pi,
                            num_points)  # Angles for the spiral
        radius = np.linspace(0, max_radius, num_points)  # Radii for the spiral
        x = radius * np.cos(theta)  # x-coordinates of the spiral
        y = radius * np.sin(theta)  # y-coordinates of the spiral

        # Add random noise to the points
        for i in range(num_points):
            x[i] += random.uniform(-1, 1) * noise_scale
            y[i] += random.uniform(-1, 1) * noise_scale

        # Draw the spiral
        vsk.polygon(np.column_stack((x, y)))

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    SpiralSketch.display()
