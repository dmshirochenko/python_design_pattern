#!/usr/bin/env python3

class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        print('Here lights', lights)
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        print('Here obstacles', obstacles)
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()



class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        # save adaptee object
        self.adaptee = adaptee

    def lighten(self, grid):
        #initialize empty list for lights sources and obstacles coordinates
        lights_list = []
        obstacles_list = []

        #check size and create map
        height_grid = len(grid)
        weight_grid = len(grid[0])
        self.adaptee.set_dim((weight_grid, height_grid))

        #check elements on source map
        for height in range(len(grid)):
            for weight in range(len(grid[height])):
                if grid[height][weight] == 1:
                    #print(f'height = {height}, weight = {weight}')
                    lights_list.append((weight, height))
                if grid[height][weight] == -1:
                    #print(f'height = {height}, weight = {weight}')
                    obstacles_list.append((weight, height))

        #transfer lights sources and obstacle to class Light
        self.adaptee.set_lights(lights_list)
        self.adaptee.set_obstacles(obstacles_list)

        #return light map
        return self.adaptee.generate_lights()


if __name__ == '__main__':
    system = System()
    light_mapper = Light((30, 20))
    print('Ligth grid = ', light_mapper.grid)
    adapter = MappingAdapter(light_mapper)
    system.get_lightening(adapter)
    print('Self map = ', system.map)
    print('Ligth map = ', system.lightmap)
