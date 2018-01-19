def longest(s1, s2):
    # your code
    s3=s1+s2
    s4=set(s3)
    s5=(''.join(s4))
    s6=sorted(s5)
    s7=(''.join(s6))
    return(s7)





longest("aretheyhere", "yestheyarehere")
longest("loopingisfunbutdangerous", "lessdangerousthancoding")
longest("inmanylanguages", "theresapairoffunctions")