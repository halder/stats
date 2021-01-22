def SQRT(x):
    return x**(1/2)

def median(sample):
    """
    sample: list
    """
    n = len(sample)

    if n % 2 != 0:
        half = n // 2
        med = sorted(sample)[half]
    else:
        half_l = (n // 2) - 1
        half_r = n // 2
        med = (sorted(sample)[half_l] + sorted(sample)[half_r]) / 2
    return med

def metrics(sample, unbiased=False):
    """
    Sample mean, sample variance (plus std)
    """
    n = len(sample)
    mean = sum(sample) / n
    # variance
    if unbiased:
        denom = n - 1
    else:
        denom = n
    var_s = 0
    for v in sample:
        var_s += (v - mean)**2
    var = var_s / denom
    return mean, var, SQRT(var)

def z_statistic(sample, estimate):
    """
    Z Test: Compare sample mean to population mean
    --------------------------------------------------
    Normalization to N(0,1)
    X ~ N(mu,sigma^2) -> Z = (X - mu) / sigma ~ N(0,1)
    n >= 30 by CLT
    """
    n = len(sample)
    if n < 30:
        print("n < 30. CLT does not apply.")
    mean, _, std = metrics(sample)
    return (SQRT(n) / std) * (mean - estimate)

def t_statistic(sample1, sample2):
    """
    T Test: Compare to samples

    T = (mu1 - mu2) / sqrt( (var1 / n) / (var2 / m) )
    T ~ tN, where N = WS degrees of freedom
    """
    n, m = len(sample1), len(sample2)
    mu1, var1, _1 = metrics(sample1)
    mu2, var2, _2 = metrics(sample2)
    nom = mu1 - mu2
    denom = SQRT( (var1 / n) + (var2 / m) )
    return nom / denom

def ws_df(sample1, sample2):
    """
    Implementation of Welch-Satterthwaite to determine degrees of freedom for t-tests.

    df = [ (std1^2 / n) + (std2^2 / m) ]^2 / [ (std1^4 / n^2*(n-1)) + (std2^4 / m^2*(m-1)) ]
    """
    n, m = len(sample1), len(sample2)
    _1, var1, _11 = metrics(sample1)
    _2, var2, _22 = metrics(sample2)
    nom = ((var1 / n) + (var2 / m))**2
    denom = ((var1**2 / (n**2 * (n - 1))) + (var2**2 / (m**2 * (m - 1))))
    N = nom / denom
    # round down to be conservative
    return N // 1
