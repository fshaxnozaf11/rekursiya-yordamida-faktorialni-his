def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
```

```python
def faktorial_iterativ(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```

```python
def faktorial_rekursiya_saf(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    else:
        result = n * faktorial_rekursiya_saf(n-1, memo)
        memo[n] = result
        return result
