**2a)**

**State Representation:** Matrix with Board: B[6,7], or in general case B[N,M], filled with values 0..2. 0 represents empty square, 1 and 2 pieces from player 1 or 2; Player to move: Pla; Also is a good idea to add the last square played (Yi, Xi) for efficiency

**Initial State:** Matrix filled with zeros; Pla = 1

**Objective State:** 

**Operators:** 

| Name | Pre-Conditions | Effects |
| ---- | -------------- | ------- |
exec_move(int Col) | B[1, Col] == 0 // for playing at Column Col, the top position of the Column must be empty | exec_move |