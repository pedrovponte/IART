**a)** 

* 12 variables {Sol1, Sol2, ..., Sol12} with values 1..4
* Array with 12 positions/ disciplines: sol[12] 

```py
create_solution:
    for(int i = 0; i < 12; i++):
        sol[i] = random.random(1,4)
```

**b)**

* Data is read to matrix: bool discStud[Nd, Na]; if discStud[4,8] = True => student 8 registered at discipline 4

```py
incompatib(d1, d2):
    count = 0
    for a in range Na:
        if(discStud[d1, a] and discStud[d2, a]):
            count++
    return count
```

**c)**

```py
evaluate(sol):
    eval = 0
    for 
        for


```

**d)**

* Example of sol = [1,1,1,1,2,2,2,2,3,3,4,4]
* Possible neighbours: [3,1,1,1,2,2,2,2,3,3,4,4], [1,1,1,1,2,2,4,2,3,3,4,4], ... // Neighbour1: change a discipline from slot

```py
def neighbour1(sol):
    d1 = rand(1,Nd) 
    while new_slot == sol[d1]
        new_slot = rand(1, Ns)
    
    sol[d1] = new_slot
    return sol
```

```py
def neighbour2(sol):
    d1 = rand(1, Nd)
    while d1 == d2 || sol[d1] == sol[d2]
        d2 = rand(1, Nd)
    
    aux = sol[d1]
    sol[d1] = sol[d2]
    sol[d2] = aux

    return sol
```

```py
def neighbour3(sol):
    if rand(0,1) == 0
        return 

```

**e)**

```py
def hillClimbing:
    sol = initialSolution()
    it = 0
    while(it < 1000):
        neig = neighbour3(sol)
        it++
        if(eval(neig) < eval(sol)):
            sol = neig
            it = 0
    
    return sol
```

```py
def simulatedAnnealing:
    sol = initialSolution()
    T = Tinit() #T = 1000
    while(it < 1000):
        T=schedule(T) #T = 0.9*T
        neig = neighbour(sol)
        it++
        delta = eval(sol) - eval(neig)
        if((delta > 0 || e**(-delta/T)) > rand(0,1)):
            sol = neig
            it = 0
    
    return sol
```
