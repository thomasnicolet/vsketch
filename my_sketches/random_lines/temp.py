import vsketch
import numpy as np


class RandomLinesSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False)
        vsk.scale("cm")

        all_polygons = []

        num_lines = 4
        
        # Vertical lines
        all_column_points = []
        for row in np.linspace(0, num_lines, num_lines):
            # Initialize as empty 2D numpy array
            column_points = np.empty((0, 2))
            for col in np.linspace(0, num_lines, num_lines):
                # Add randomness within a range that ensures no overlap
                x = row + vsk.random(-0.4, 0.4)
                # Add randomness within a range that ensures no overlap
                y = col + vsk.random(-0.4, 0.4)
                vsk.point(x, y)
                # Stack new point onto array
                column_points = np.vstack((column_points, [x, y]))
            all_column_points.append(column_points)

 

        # Interpolate and draw vertical lines
        for index in range(len(all_column_points) - 1):
            current_column_points = all_column_points[index]
            next_column_points = all_column_points[index + 1]

            interpolation_steps = 9
            for interpolation_step in range(interpolation_steps):
                interpolated_points = vsk.lerp(
                    current_column_points,
                    next_column_points,
                    interpolation_step / interpolation_steps)
                all_polygons.append(interpolated_points)
                
        # # Horizontal lines
        # all_row_points = []
        # for col in np.linspace(0, num_lines, num_lines):
        #     row_points = np.empty((0, 2))  # Initialize as empty 2D numpy array
        #     for row in np.linspace(0, num_lines, num_lines):
        #         # Add randomness within a range that ensures no overlap
        #         x = row + vsk.random(-0.4, 0.4)
        #         # Add randomness within a range that ensures no overlap
        #         y = col + vsk.random(-0.4, 0.4)
        #         vsk.point(x, y)
        #         # Stack new point onto array
        #         row_points = np.vstack((row_points, [x, y]))
        #     all_row_points.append(row_points)

        # # Interpolate and draw horizontal lines
        # for index in range(len(all_row_points) - 1):
        #     current_row_points = all_row_points[index]
        #     next_row_points = all_row_points[index + 1]

        #     interpolation_steps = 9
        #     for interpolation_step in range(interpolation_steps):
        #         interpolated_points = vsk.lerp(
        #             current_row_points,
        #             next_row_points,
        #             interpolation_step / interpolation_steps)
        #         all_polygons.append(interpolated_points)

        # Sort polygons by y-coordinate of first point
        all_polygons.sort(key=lambda polygon: polygon[0, 1])

        # Draw polygons
        for polygon in all_polygons:
            vsk.polygon(polygon)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    RandomLinesSketch.display()
