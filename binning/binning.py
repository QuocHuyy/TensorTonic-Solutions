def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    w = (max(values) - min(values))/num_bins
    if w == 0:
        b = [0]*len(values)
    else:
        b = [min(int((x - min(values))/w), num_bins - 1) for x in values] 
    return b