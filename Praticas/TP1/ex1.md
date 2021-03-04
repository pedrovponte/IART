**1.**

**a)** Neste caso, são necessárias 2 variáveis, cada uma representando a quantidade de água de cada balde. Por exemplo, b1 e b2.

**State representation:** (b1,b2); 0 < b1 < 4; 0 < b2 < 3
**Initial State:** (0,0)
**Objective state:** Fill the first bucket with n litres (n,b2), in this case n is 2 and we don't care about b2 final value
**Operators:**

| Operator | Initial State and Preconditions | Final State | Cost |
| -------- | ------------------------------- | ----------- | ---- |
| 1- Fill the 4L bucket | (x, y) with x < 4 | (4, y) | 1 |
| 2- Fill the 3L bucket | (x, y) with y < 3 | (x, 3) | 1 |
| 3- Empty the 4L bucket | (x, y) with x > 0 | (0, y) | 1
| 4- Empty the 3L bucket | (x, y) with y > 0 | (x, 0) | 1
| 5- Pour water from the 3L bucket to completely fill the 4L bucket | (x, y) with x+y >= 4 and y > 0 | (4, y-(4-x)) | 1 |
| 6- Pour water from the 4L bucket to completely fill the 3L bucket | (x, y) with x+y >= 3 and x > 0 | (x-(3-y), 3) | 1 |
| 7- Pour all the water from the 3L bucket to the 4L bucket | (x, y) with x+y <= 4 and y >= 0 | (x+y, 0) | 1 |
| 8- Pour all the water from the 4L bucket to the 3L bucket | (x, y) with x+y <= 3 and x >= 0 | (0, x+y) | 1 |

**b)**

![](ex1b.png)