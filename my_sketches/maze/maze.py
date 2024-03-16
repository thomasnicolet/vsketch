import vsketch
import numpy as np


class RandomLinesSketch(vsketch.SketchClass):
    
    WIDTH = vsketch.Param(10.4)
    HEIGHT = vsketch.Param(14.7)
    TIMESTEP = vsketch.Param(0.005)
    SIZE = vsketch.Param(0.1)
    NOISE_RESOLUTION = vsketch.Param(0.01)
    STEP_MULTIPLIER = vsketch.Param(9)
    MARGIN = vsketch.Param(1.0)
    
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a6")
        vsk.scale("cm")
        margin = 1
        self.WIDTH -= self.MARGIN
        self.HEIGHT -= self.MARGIN
        TIMESTEP_INIT = 5
        if (int(self.WIDTH*self.STEP_MULTIPLIER) < 0):
            print(int(self.WIDTH*self.STEP_MULTIPLIER))
            
        for i in np.linspace(0, self.WIDTH, int(self.WIDTH*self.STEP_MULTIPLIER)):
            for j in np.linspace(0, self.HEIGHT, int(self.HEIGHT*self.STEP_MULTIPLIER)):
            
            
                noise = vsk.noise(
                    i*self.NOISE_RESOLUTION,
                    j*self.NOISE_RESOLUTION,
                    TIMESTEP_INIT)
                
                #noise = vsk.noise(x_noise, y_noise, TIMESTEP_INIT)
                
                if noise < 0.5:
                    vsk.line(i, j, i + self.SIZE, j + self.SIZE)
                else:
                    vsk.line(i + self.SIZE, j, i, j + self.SIZE)
                    
            TIMESTEP_INIT += self.TIMESTEP

        # Draw rectangle around the plot
        offset = 0
        vsk.rect(-offset, -offset, self.WIDTH+self.SIZE+(offset*2), self.HEIGHT+self.SIZE + (offset*2))
    
    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")
        
        
if __name__ == "__main__":
    RandomLinesSketch.display()
