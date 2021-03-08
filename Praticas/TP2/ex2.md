**a)**

**State representation:** 2D Array
```
state = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15, 0]
]
```

0 represents the empty space

**Initial State:** 

```
state = [
    [ 4, 1, 3, 2],
    [ 5,13,14, 8],
    [15,10, 0,12],
    [13, 6, 9,11]
]
```

**Objective state:** 

```
state = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15, 0]
]
```

**Operators:** (X horizontal, left->right; Y vertical, up->down)

| Operator | Pre-conditions | Effects | Cost |
| -------- | -------------- | ------- | ---- |
| up | Ys > 1 | B[Xs,Ys] = B[Xs, Ys-1]; B[Xs, Ys-1] = 0; Ys = Ys-1 | 1 |
| down | Ys < N | B[Xs,Ys] = B[Xs, Ys+1]; B[Xs, Ys+1] = 0; Ys = Ys+1 | 1 |
| left | Xs > 1 | B[Xs,Ys] = B[Xs-1, Ys]; B[Xs-1, Ys] = 0; Xs = Xs-1 | 1 |
| right | Xs < N | B[Xs,Ys] = B[Xs+1, Ys]; B[Xs+1, Ys] = 0; Xs = Xs+1 | 1 |

**b)** ![](bfs.png)

**c)** ![](a_star.png)