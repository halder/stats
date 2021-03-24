import numpy as np

def nrt(x, n):
    """
    compute n_th root of x
    """
    return x ** (1 / n)


def sqrt(x):
    return n_root(x, 2)


def median(sample):
    """
    sample: list
    """
    n = len(sample)
    srt = sorted(sample)

    if n % 2 != 0:
        half = n // 2
        med = srt[half]
    else:
        half_l = (n // 2) - 1
        half_r = n // 2
        med = (srt[half_l] + srt[half_r]) / 2

    return med


def sample_mean(sample):
    """
    sample: list
    """
    n = len(sample)
    return sum(sample) / n


def var(sample, unbiased=False):
    if unbiased:
        denom = len(sample) - 1
    else:
        denom = len(sample)

    mu = sample_mean(sample)
    # vectorized calculation
    var = (np.array(sample) - mu) ** 2

    return np.sum(var) / denom


def std(sample, unbiased=False):
    # calculate SD from sample or variance?
    # (un)biased? -> research
    return sqrt(var(sample, unbiased=unbiased))
