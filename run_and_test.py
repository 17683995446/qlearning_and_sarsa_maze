
from matplotlib import pyplot as plt

epoch = 1000
from RL import  RL,QLearningTable,SarsaTable
from maze import Maze
import  time
count_times=[]
def update():
    for episode in range(epoch):
        current_state = env.reset()
        count=0
        while True:
            env.render()
            #步数加一
            count += 1

            # Sarsa学习，执行action得到回报值和新的状态, ε-greedy随机选择动作，取该动作对应的Q值，再更新Q表
            if(count==1):
                action = RL.choose_action(str(current_state))
            new_state, reward, finished_or_not = env.step(action, count, RL)
            new_action = RL.choose_action(str(new_state))
            RL.learn(str(current_state), action, reward, str(new_state),new_action)
            action = new_action


            #Q学习，执行action得到回报值和新的状态，取新的状态的Q的最大值 ，再更新Q表
            # action = RL.choose_action(str(current_state))
            # new_state, reward, finished_or_not = env.step(action, count, RL)
            # RL.learn(str(current_state), action, reward, str(new_state))



            current_state = new_state
            if finished_or_not:
                if(episode==epoch-1):
                    env.diaplay(RL.q_table)
                    print(env.get_outcome())
                    with open(RL.__class__.__name__+"5.txt", "w") as f:
                        for i in env.get_outcome():
                            text = f.write(str(i) + "\n")
                    f.close()

                    time.sleep()
                break
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    #RL = QLearningTable(actions=list(range(env.n_actions)))
    RL = SarsaTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()
    #print(count_times)