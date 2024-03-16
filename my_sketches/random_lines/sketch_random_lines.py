import vsketch
import numpy as np


class RandomLinesSketch(vsketch.SketchClass):
    
    NUM_LINES = vsketch.Param(15)
    INTERPOLATION_STEPS_VERTICAL = vsketch.Param(15)
    INTERPOLATION_STEPS_HORISONTAL = vsketch.Param(15)
    STEPS = vsketch.Param(10)
    RANDOW_LOWER = vsketch.Param(-0.4)
    RANDOM_UPPER = vsketch.Param(0.4) 

    
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False)
        vsk.scale("cm")
  
        all_polygons = []
        

        # Vertical lines
        all_column_points = []
        for row in np.linspace(0, self.NUM_LINES, self.STEPS):
            # Initialize as empty 2D numpy array
            column_points = np.empty((0, 2))
            for col in np.linspace(0, self.NUM_LINES, 10):
                # Add randomness within a range that ensures no overlap
                x = row + vsk.random(self.RANDOW_LOWER, self.RANDOM_UPPER)
                # Add randomness within a range that ensures no overlap
                y = col + vsk.random(self.RANDOW_LOWER, self.RANDOM_UPPER)
                column_points = np.vstack((column_points, [x, y]))
            all_column_points.append(column_points)

        
        # Interpolate and draw vertical lines
        for index in range(len(all_column_points) - 1):
            current_column_points = all_column_points[index]
            next_column_points = all_column_points[index + 1]
            
            for interpolation_step in range(self.INTERPOLATION_STEPS_VERTICAL + 1):
                interpolated_points = vsk.lerp(
                    current_column_points,
                    next_column_points,
                    interpolation_step / self.INTERPOLATION_STEPS_VERTICAL)
                all_polygons.append(interpolated_points)
        print(all_polygons)
              
        # Horizontal lines
        all_test_points =  []
        for index in range(10):
            test_row_points = np.empty((0, 2))
            for item in all_column_points:
                x = item[index][0]
                y = item[index][1]
                test_row_points = np.vstack((test_row_points, [x, y]))
            all_test_points.append(test_row_points)

        # Interpolate and draw horizontal lines
        for index in range(len(all_test_points) - 1):
            current_column_points = all_test_points[index]
            next_column_points = all_test_points[index + 1]

            for interpolation_step in range(self.INTERPOLATION_STEPS_HORISONTAL +1):
                interpolated_points = vsk.lerp(
                    current_column_points,
                    next_column_points,
                    interpolation_step / self.INTERPOLATION_STEPS_HORISONTAL)
                all_polygons.append(interpolated_points)
                        
        # Draw polygons
        for polygon in all_polygons:
            vsk.polygon(polygon)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    RandomLinesSketch.display()
