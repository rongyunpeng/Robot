import numpy as np
s = np.array([int(i) for i in input().split()])
d_f, d_r, d_b, d_l = [int(i) for i in input().split()]
n = int(input())
direction = np.array([0, 1])
for i in range(n):
    e, c = input().split()
    if e == "m":
        if c == "F":
            s = s + d_f * direction
        elif c == "R":
            m_turn = np.array([[0, -1], [1, 0]])
            m_direction = np.dot(direction, m_turn)
            s = s + d_r * m_direction
        elif c == "B":
            s = s - d_b * direction
        elif c == "L":
            m_turn = np.array([[0, 1], [-1, 0]])
            m_direction = np.dot(direction, m_turn)
            s = s + d_l * m_direction
    
    else:
        if c == "R":
            turn = np.array([[0, -1], [1, 0]])
            direction = np.dot(direction, turn)
        elif c == "L":
            turn = np.array([[0, 1], [-1, 0]])
            direction = np.dot(direction, turn)
        elif c == "B": 
            direction = np.dot(direction, -1)
            
result = ""
for i in s:
    result += str(i) + " "
print(result[:-1])
