# Recurso 2018

## 1 

**a)** ![](images/ex_1a_2018R.png)

**b)** Uma possível heurística poderá ser o número de elementos que estão do lado esquerdo. É sempre admissível, uma vez que irá haver pelo menos um movimento para colocar esse elemento no sítio correto.

![](images/ex_1b_2018R.png)

**c)** ![](images/ex_1c_2018R.png)

## 2 

**a)** 

Custo S1:
* M1 = 10 + 7 + 8 = 25
* M2 = 11 + 12 = 23
* Max(23, 25) = 25

Custo = 25

**b)** 

* S2 = {A-M2, B-M1, C-M2, D-M2, E-M1}
* S3 = {A-M1, B-M3, C-M2, D-M2, E-M1}
* S4 = {A-M1, B-M1, C-M3, D-M2, E-M1}
* S5 = {A-M1, B-M1, C-M2, D-M3, E-M1}
* S6 = {A-M1, B-M1, C-M2, D-M2, E-M2}
* S7 = {A-M1, B-M1, C-M2, D-M2, E-M3}

* Custo S2 = Max(15,33) = 33
* Custo S3 = Max(18,23,7) = 23
* Custo S4 = Max(25,12,11) = 25
* Custo S5 = Max(25,11,12) = 25
* Custo S6 = Max(17,31) = 31
* Custo S7 = Max(17,23,8) = 23

Será escolhido o S3 ou o S7.

**c)** 

```
P(S2) = e^(delta/T) = e^(-8/10) = 0.449
delta = 25 - 33 = -8
T = 10
```

Como 0.449 < 0.55, então a S2 é rejeitada.

Como S3 < S1, então a solução S3 é aceite.

## 3

**a)**

```
E(S) = -(3/8*log2(3/8) + 5/8*log2(5/8)) = 0.954
```

**b)**

```
Hair

Blonde: 2Y 2N
Brown: 0Y 3N
Red: 1Y 0N

E(Hair) = 4/8 * (-2/4 * log2(2/4) - 2/4 * log2(2/4)) + 3/8 * (0/3 * log2(0/3) - 3/3 * log2(3/3)) + 1/8 * (-1 * log2(1) - 0/1 * log2(0)) = 0.5

-----------------
Height

Average: 2Y 1N
Tall: 0Y 2N
Short: 1Y 2N

E(Height) = 3/8 * (-2/3 * log2(2/3) - 1/3 * log2(1/3)) + 2/8 * (-0/8 * log2(0/8) - 2/2 * log2(2/2)) + 3/8 * (-1/3 * log2(1/3) - 2/3 * log2(2/3)) = 0.689

-----------------
Weight

Light: 1Y 1N
Average: 1Y 2N
Heavy: 1Y 2N

E(Weight) = 2/8 * (-1/2 * log2(1/2) - 1/2 * log2(1/2)) + 3/8 * (-1/3 * log2(1/3) - 2/3 * log2(2/3)) + 3/8 * (-1/3 * log2(1/3) - 2/3 * log2(2/3)) = 0.939

-----------------
Lotion

No: 3Y 2N
Yes: 0Y 3N

E(Lotion) = 5/8 * (-3/5 * log2(3/5) - 2/5 * log2(2/5)) + 3/8 * (-0/3 * log2(0/3) - 3/3 * log2(3/3)) = 0.607

O atributo escolhido é o "Hair".
```

**c)**

```
Hair

Blonde: 4
Brown: 3
Red: 1

Split Info = -4/8 * log2(4/8) - 3/8 * log2(3/8) - 1/8 * log2(1/8) = 1.406
Gain Ratio = (0.954 - 0.5) / 1.406 = 0.321

----------------
Height

Average: 3
Tall: 2
Short: 3

Split Info = -3/8 * log2(3/8) - 2/8 * log2(2/8) - 3/8 * log2(3/8) = 1.561
Gain Ratio = (0.954 - 0.689) / 1.561 = 0.1699

----------------
Weight

Light: 2
Average: 3
Heavy: 3

Split Info = -2/8 * log2(2/8) - 3/8 * log2(3/8) - 3/8 * log2(3/8) = 1.561
Gain Ratio = (0.954 - 0.939) / 1.561 = 0.0098

----------------
Lotion

Yes: 3
No: 5

Split Info = -3/8 * log2(3/8) - 5/8 * log2(5/8) = 0.954
Gain Ratio = (0.954 - 0.607) / 0.954 = 0.364

O atributo escolhido é o Lotion.
```

**d)**

```
Yes: 0Y 3N
No: 3Y 2N

Error(No) = (2+1)/(5+2) = 3/7 = 0.429
Error(Y) = (0+1)/(3+2) = 1/5 = 0.2
``` 

## 4 

**a)** Utilizava-se a pesquisa em profundidade com profundidade limitada, uma vez que permite obter uma solução a uma profundidade inferior ao limite dado, cujo valor máximo é sabido. Este algoritmo não garante que retorna sempre a melhor solução, mas este não é um dos requesitos. Em termos de gastos com memória, estes também são reduzidos, uma vez que não precisa de guardar os nós em memória, o que é importante devido à grande ramificação da árvore.

**b)** h' = h/1.1 = 0.999*h

**d)**

```
Total = 10 + 15 + 27 + 30 = 82
P(C1) = 10 / 82 = 0.122
P(C2) = 15 / 82 = 0.183
P(C3) = 27 / 82 = 0.329
P(C4) = 30 / 82 = 0.366
```

**e)**

![](images/ex_4e_2018R.png)

**f)** As regras são causais, uma vez que o agente conhece completamente todo o ambiente, sabendo a partir disso quais as causas de cada perceção que tem do mesmo.


