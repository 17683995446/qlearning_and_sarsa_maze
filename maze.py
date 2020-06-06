
import numpy as np
import time
import sys
import random
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk



grid_height = 9
grid_width = 9

UNIT = 80
class Maze(tk.Tk, object):
    global outcome
    outcome = []
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(grid_height * UNIT, grid_height * UNIT))
        self._build_maze()


    def get_outcome(self):
        return outcome
    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                                height=grid_height * UNIT,
                                width=grid_width * UNIT)

        # 创建网格世界
        for c in range(0, grid_width * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, grid_height * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, grid_height * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, grid_width * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
        origin = np.array([20, 20])

        # hell
        hell1_center = origin + np.array([UNIT * 1, UNIT*7])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 55, hell1_center[1] + 55,
            fill='black')
        # hell
        hell2_center = origin + np.array([UNIT*2, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 55, hell2_center[1] + 55,
            fill='black')
        # hell
        hell3_center = origin + np.array([UNIT * 1, UNIT * 3])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 55, hell3_center[1] + 55,
            fill='black')
        # hell
        hell4_center = origin + np.array([UNIT * 3, UNIT * 4])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 55, hell4_center[1] + 55,
            fill='black')

        hell5_center = origin + np.array([UNIT * 5, UNIT * 2])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 15, hell5_center[1] - 15,
            hell5_center[0] + 55, hell5_center[1] + 55,
            fill='black')

        hell6_center = origin + np.array([UNIT * 6, UNIT * 3])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 15, hell6_center[1] - 15,
            hell6_center[0] + 55, hell6_center[1] + 55,
            fill='black')

        hell7_center = origin + np.array([UNIT * 1, UNIT * 5])
        self.hell7 = self.canvas.create_rectangle(
            hell7_center[0] - 15, hell7_center[1] - 15,
            hell7_center[0] + 55, hell7_center[1] + 55,
            fill='black')

        hell8_center = origin + np.array([UNIT * 2, UNIT * 6])
        self.hell8 = self.canvas.create_rectangle(
            hell8_center[0] - 15, hell8_center[1] - 15,
            hell8_center[0] + 55, hell8_center[1] + 55,
            fill='black')

        hell9_center = origin + np.array([UNIT * 4, UNIT * 4])
        self.hell9 = self.canvas.create_rectangle(
            hell9_center[0] - 15, hell9_center[1] - 15,
            hell9_center[0] + 55, hell9_center[1] + 55,
            fill='black')

        hell10_center = origin + np.array([UNIT * 3, UNIT * 6])
        self.hell10 = self.canvas.create_rectangle(
            hell10_center[0] - 15, hell10_center[1] - 15,
            hell10_center[0] + 55, hell10_center[1] + 55,
            fill='black')

        hell11_center = origin + np.array([UNIT * 5, UNIT * 6])
        self.hell11 = self.canvas.create_rectangle(
            hell11_center[0] - 15, hell11_center[1] - 15,
            hell11_center[0] + 55, hell11_center[1] + 55,
            fill='black')

        hell12_center = origin + np.array([UNIT * 6, UNIT * 5])
        self.hell12 = self.canvas.create_rectangle(
            hell12_center[0] - 15, hell12_center[1] - 15,
            hell12_center[0] + 55, hell12_center[1] + 55,
            fill='black')

        oval_center = origin + np.array([UNIT * 5,UNIT * 7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 55, oval_center[1] + 55,
            fill='yellow')





        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 55, origin[1] + 55,
            fill='red')

        self.canvas.pack()

    def reset(self):
        self.update()
       # time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])

        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 55, origin[1] + 55,
            fill='red')

        return self.canvas.coords(self.rect)

    def step(self, action,count,RL):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (grid_height - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (grid_width - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  #移动

        s_ = self.canvas.coords(self.rect)  

        # 回报函数
        if s_ == self.canvas.coords(self.oval):
            print(RL.q_table)
            print(count)
            reward = 20
            finished_or_not = True
            s_ = 'terminal'
            outcome.append(count)
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2), self.canvas.coords(self.hell3), self.canvas.coords(self.hell4),self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.hell7),self.canvas.coords(self.hell8),self.canvas.coords(self.hell9),self.canvas.coords(self.hell10),self.canvas.coords(self.hell11),self.canvas.coords(self.hell12)]:
            reward = -5
            finished_or_not = True
            s_ = 'terminal'
            outcome.append(count*-1)
        else:
            reward = -0.01
            finished_or_not = False

        return s_, reward, finished_or_not

    def render(self):
        #time.sleep(0.1)
        self.update()

    def diaplay(self,table):
        for i in range(table.shape[0]):

            observation = table.index[i][1:len(table.index[i])-1].split(", ")
            if (observation[0] != "ermina"):
                position = (float(observation[0]),float(observation[1]),float(observation[2]),float(observation[3]))
                self.canvas.create_text((position[0] + 15, position[1] + 35), text=str(table.iloc[i][3])[0:5])
                self.canvas.create_text((position[0] + 55, position[1] + 35), text=str(table.iloc[i][2])[0:5])
                self.canvas.create_text((position[0] + 35, position[1] + 5), text=str(table.iloc[i][0])[0:5])
                self.canvas.create_text((position[0] + 35, position[1] + 65), text=str(table.iloc[i][1])[0:5])
                self.canvas.create_line((position[0], position[1], position[2], position[3]),width=1,fill="red")
                self.canvas.create_line((position[0], position[3], position[2], position[1]), width=1, fill="red")



