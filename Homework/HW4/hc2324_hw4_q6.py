def appearances(s,low,high):
    if low==high:
        return {s[high]:1}
    else:
        appeare = appearances(s, low, high-1)
        if s[high] not in appeare:
            appeare[s[high]] = 1
        else:
            appeare[s[high]]+=1
        return appeare

