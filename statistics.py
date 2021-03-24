from metrics import *

def z_statistic(sample, estimate, unbiased=False):
    """
    sample: list
    estimate: int/float
    --------------------------------------------------
    Z Test: Compare sample mean to population mean estimate

    Normalization to N(0,1):
        Z = (X - mu) / sigma

        * X ~ N(mu,sigma^2)
        * Z ~ N(0,1)

    n >= 30 in order for CLT to apply
    """
    n = len(sample)
    if n < 30:
        print("n < 30. CLT does not apply.")

    mu = sample_mean(sample)
    sd = std(sample, unbiased=False)

    return (sqrt(n) / sd) * (mu - estimate)


def t_statistic(N, M, unbiased=False):
    """
    samples N, M: list
    --------------------------------------------------
    T Test: Compare two samples

    T = (mu1 - mu2) / sqrt( (var1 / n) / (var2 / m) )
    T ~ tN, where N = WS degrees of freedom
    """
    n, m = len(N), len(M)

    mu_n, var_n = sample_mean(N), var(N, unbiased=unbiased)
    mu_m, var_m = sample_mean(M), var(M, unbiased=unbiased)

    nom = mu_n - mu_m
    denom = (var_n / n) + (var_m / m)
    return nom / sqrt(denom)


def ws_df(N, M, unbiased=False):
    """
    samples N, M: list
    --------------------------------------------------
    Implementation of Welch-Satterthwaite to determine degrees of freedom for t-tests.

    https://en.wikipedia.org/wiki/Welch%27s_t-test
    """
    n, m = len(N), len(M)

    var_n = var(N, unbiased=unbiased)
    var_m = var(M, unbiased=unbiased)

    nom = (var_n / n) + (var_m / m)
    denom = (
        (var_n ** 2 / (n ** 2 * (n - 1)))
        + (var_m ** 2 / (m ** 2 * (m - 1)))
    )

    df = (nom ** 2) / denom
    # round down to be conservative
    return df // 1
