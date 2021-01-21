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

def z_statistic(data, estimate):
    """
    Z Test: Compare sample mean to population mean
    --------------------------------------------------
    Normalization to N(0,1)
    X ~ N(mu,sigma^2) -> Z = (X - mu) / sigma ~ N(0,1)
    n >= 30 by CLT
    """
    n = len(data)
    if n < 30:
        print("n < 30. CLT does not apply.")
    mean, _, std, __ = descriptive_stats(data)
    return (SQRT(n) / std) * (mean - estimate)

def t_statistic(sample1, sample2):
    """
    T Test: Compare to samples

    T = (mu1 - mu2) / sqrt( (var1 / n) / (var2 / m) )
    T ~ tN, where N = WS degrees of freedom
    """
    n, m = len(sample1), len(sample2)
    mu1, var1, _1, _11 = descriptive_stats(sample1)
    mu2, var2, _2, _22 = descriptive_stats(sample2)
    nom = mu1 - mu2
    denom = SQRT( (var1 / n) + (var2 / m) )
    return nom / denom

def ws_df(sample1, sample2):
    """
    Implementation of Welch-Satterthwaite to determine degrees of freedom for t-tests.

    df = [ (std1^2 / n) + (std2^2 / m) ]^2 / [ (std1^4 / n^2*(n-1)) + (std2^4 / m^2*(m-1)) ]
    """
    n, m = len(sample1), len(sample2)
    _1, var1, _11, _111 = descriptive_stats(sample1)
    _2, var2, _22, _222 = descriptive_stats(sample2)
    nom = ((var1 / n) + (var2 / m))**2
    denom = ((var1**2 / (n**2 * (n - 1))) + (var2**2 / (m**2 * (m - 1))))
    N = nom / denom
    # round down to be conservative
    return N // 1
