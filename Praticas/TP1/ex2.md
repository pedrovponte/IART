**2.**

**a)**

**State representation:** (m,c,b), where m is the number of missionaries on the initial bank of the river, c is the number of cannibals on the initial bank of the river and b represents where the boat is right now (1 for initial side; -1 for final side). 0 <= m <= 3; 0 <= c <= 3; b=1 \/ b=-1

**Initial state:** (3,3,1)

**Objective state:** (0,0,0)

**Operators:**

| Operator | Initial State | Conditions | Final State | Cost |
| -------- | ------------- | ---------- | ----------- | ---- |
| Move one cannibal from the initial bank to the final | (m, c, b) | b = 1 | ((m1, c1 -1, m2, c2 + 1), -b) | 1 |
| Move one cannibal from the final bank to the initial | (m, c, b) | b = -1 | ((m1, c1+1, m2, c2-1), -b) | 1 |
| Move one missionary from the initial bank to the final | (m, c, b) | b = 1 | ((m1-1, c1, m2+1, c2), -b) | 1 |
| Move one missionary from the final bank to the initial | (m, c, b) | b = -1 | ((m1+1, c1, m2-1, c2), -b) | 1 |
| Move two missionaries from the initial bank to the final | (m, c, b) | b = 1 | ((m1-2, c1, m2+2, c2), -b) | 1 |
| Move two missionaries from the final bank to the initial | (m, c, b) | b = -1 | ((m1+2, c1, m2-2, c2), -b) | 1 |
| Move two cannibals from the initial bank to the final | (m, c, b) | b = 1 | ((m1, c1-2, m2, c2+2), -b) | 1 |
| Move two cannibals from the final bank to the initial | (m, c, b) | b = -1 | ((m1, c1+2, m2, c2-2), -b) | 1 |
| Move one cannibal and one missionary from the initial bank to the final | (m, c, b) | b = 1 | ((m1-1, c1-1, m2+1, c2+1), -b) | 1 |
| Move one cannibal and one missionary from the final bank to the initial | (m, c, b) | b = -1 | ((m1+1, c1+1, m2-1, c2-1), -b) | 1 |
