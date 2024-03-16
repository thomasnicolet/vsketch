import vsketch
import numpy as np


class GravityPolygonsSketch(vsketch.SketchClass):
    
    NUM_POLYGONS = vsketch.Param(5)
    MIN_SIZE = vsketch.Param(2)
    MAX_SIZE = vsketch.Param(10)
    GRAVITY_STRENGTH = vsketch.Param(0.1)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False)
        vsk.scale("cm")

        all_polygons = []

        # Gravity point
        gravity_x = vsk.width / 2
        gravity_y = vsk.height / 2

        for _ in range(self.NUM_POLYGONS):
            x = vsk.width * np.random.random()
            y = vsk.height * np.random.random()

            size = np.random.uniform(self.MIN_SIZE, self.MAX_SIZE)

            # Apply gravity lines
            distance = ((x - gravity_x) ** 2 + (y - gravity_y) ** 2) ** 0.5
            angle = np.arctan2(gravity_y - y, gravity_x - x)
            gravity_force = self.GRAVITY_STRENGTH / (distance + 1)

            x += np.cos(angle) * gravity_force
            y += np.sin(angle) * gravity_force

            all_polygons.append([(x - size / 2, y - size / 2),
                                 (x + size / 2, y - size / 2),
                                 (x + size / 2, y + size / 2),
                                 (x - size / 2, y + size / 2)])
            
            print(all_polygons)

        # Draw polygons
        for polygon in all_polygons:
            vsk.polygon(polygon)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    GravityPolygonsSketch.display()
   