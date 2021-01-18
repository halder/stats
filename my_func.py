def descriptive_stats(data, unbiased=True):
    """
    pass list/np.array holding raw data
    """
    n = len(data)
    mean = sum(data) / n
    if len(data) % 2 != 0:
        half = len(data) // 2
        med = sorted(arr)[half]
    else:
        half_l = (len(data) // 2) - 1
        half_r = len(data) // 2
        med = (sorted(data)[half_l] + sorted(data)[half_r]) / 2
    if unbiased:
        var_s = 0
        for v in data:
            var_s += (v - mean)**2
        var = var_s / (n - 1)
    else:
        var_s = 0
        for v in data:
            var_s += (v - mean)**2
        var = var_s / n
    return mean, var, var**(0.5), med
