import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# parameters

width = 960
height = 1080

n_blots = 1

spread = 10
theshold = 1

mu = 500000
sigma = 200000

# random walk

def random_walk(grid, start_pos, steps):
    current_pos = start_pos
    for i in range(steps):
        random_step = np.random.randint(0,4)
        try:
            if random_step==0:
                current_pos = (current_pos[0], current_pos[1]+1)
            if random_step==1:
                current_pos = (current_pos[0]+1, current_pos[1])
            if random_step==2:
                assert current_pos[1]-1>=0
                current_pos = (current_pos[0], current_pos[1]-1)
            if random_step==3:
                assert current_pos[0]-1>=0
                current_pos = (current_pos[0]-1, current_pos[1])
            grid[current_pos] += 1
        except:
            i -=1
            continue
    return grid


# initialize

grid = np.zeros((height,width))

# create blots

for i in range(n_blots):
    start_pos = (np.random.randint(0,height),np.random.randint(0,width))
    steps = np.abs(np.ceil(sigma * np.random.randn() + mu)).astype(int)
    grid = random_walk(grid,start_pos,steps)



# gaussian filter
grid = sp.ndimage.gaussian_filter(grid, sigma=spread, mode='wrap')

grid = (grid > theshold).astype(int)
plt.imshow(-grid, cmap='gray')
plt.axis('off')
plt.gca().set_position([0, 0, 1, 1])
plt.show()
