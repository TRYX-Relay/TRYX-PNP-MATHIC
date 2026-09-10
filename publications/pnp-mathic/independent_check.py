"""Independent bit-mask oracle for every initial and folded benchmark state."""
import itertools as it
import json
import replay

def main():
    clauses = tuple(tuple((i+1)*s for i,s in enumerate(t) if s)
                    for t in it.product((-1,0,1), repeat=3) if any(t))
    if set(clauses) != set(replay.admissible_clauses()):
        raise AssertionError('Clause population mismatch')
    assignments = tuple(it.product((False,True),repeat=3))
    masks = {}
    for clause in clauses:
        masks[clause] = sum(1 << k for k,b in enumerate(assignments)
            if any((b[abs(l)-1] and l>0) or (not b[abs(l)-1] and l<0) for l in clause))
    formulas=folds=sat=unsat=0
    for size in range(5):
        for formula in it.combinations(clauses,size):
            mask=255
            for c in formula: mask &= masks[c]
            field=replay.initial_field(formula)
            for eliminated in range(4):
                expected={tail:any(bool(mask & (1<<k)) for k,b in enumerate(assignments)
                                  if b[eliminated:]==tail)
                          for tail in it.product((False,True),repeat=3-eliminated)}
                if field != expected: raise AssertionError((formula,eliminated))
                if eliminated<3:
                    field=replay.existential_fold(field);folds+=1
            formulas+=1;sat+=bool(mask);unsat+=not bool(mask)
    f=replay.initial_field(((1,),))
    wrong={tail:f[(False,)+tail] and f[(True,)+tail] for tail in {a[1:] for a in f}}
    if wrong==replay.existential_fold(f): raise AssertionError('AND mutation escaped')
    result=dict(formulas=formulas,folds=folds,sat=sat,unsat=unsat,
                disagreements=0,checked_initial_and_intermediate_states=True,
                negative_control='OR replaced with AND: DETECTED')
    if (formulas,folds,sat,unsat)!=(17902,53706,16241,1661):
        raise AssertionError(result)
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
