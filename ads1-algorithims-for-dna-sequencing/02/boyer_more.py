def boyer_moore(p, p_bm, t):
    i = 0
    occurences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
                if not p[j] == t[i+j]:
                        skip_bc = p_bm.bad_character_rule(j, t[+j])
                        skip_bs = p_bm.good_suffix_rule(j)
                        shift = max(shift, skip_bc, skip_gs)
                        mismatched = True
                        break
        if not mistmatched:
                occurences.append(i)
                skip_gs = p_bm.match_skip()
                shift = max(shift, skip_gs)
        i += shift
    return occurences
