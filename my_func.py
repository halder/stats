def SQRT(x):
    return x**(1/2)

def descriptive_stats(data, unbiased=False):
    """
    pass list/np.array holding raw data
    """
    n = len(data)
    mean = sum(data) / n
    # median
    if len(data) % 2 != 0:
        half = len(data) // 2
        med = sorted(data)[half]
    else:
        half_l = (len(data) // 2) - 1
        half_r = len(data) // 2
        med = (sorted(data)[half_l] + sorted(data)[half_r]) / 2
    # variance
    if unbiased:
        denom = n - 1
    else:
        denom = n
    var_s = 0
    for v in data:
        var_s += (v - mean)**2
    var = var_s / denom
    return mean, var, SQRT(var), med

def z_score(data, estimate):
    """
    Normalization to N(0,1)
    X ~ N(mu,sigma^2) -> Z = (X - mu) / sigma ~ N(0,1)
    n >= 30 by CLT
    """
    n = len(data)
    if n < 30:
        print("n < 30; CLT does not apply.")
    mean, _, std, __ = descriptive_stats(data)
    return (SQRT(n) / std) * (mean - estimate)
