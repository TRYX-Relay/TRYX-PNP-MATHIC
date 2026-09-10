#!/usr/bin/env python3
"""Independent replay of the upstream PNP continuity benchmark.

This executable uses only a distinction-bearing Boolean carrier and exact
existential folding.  It imports no Snowman/Collatz machinery.
"""

from __future__ import annotations

import hashlib
import itertools
import json


VARIABLES = (1, 2, 3)


def admissible_clauses() -> tuple[tuple[int, ...], ...]:
    clauses: list[tuple[int, ...]] = []
    for width in range(1, 4):
        for support in itertools.combinations(VARIABLES, width):
            for signs in itertools.product((-1, 1), repeat=width):
                clauses.append(tuple(v * s for v, s in zip(support, signs)))
    return tuple(clauses)


def satisfies(formula: tuple[tuple[int, ...], ...], bits: tuple[bool, ...]) -> bool:
    assignment = {i + 1: bit for i, bit in enumerate(bits)}
    return all(any(assignment[abs(lit)] is (lit > 0) for lit in clause) for clause in formula)


def initial_field(formula: tuple[tuple[int, ...], ...]) -> dict[tuple[bool, ...], bool]:
    return {
        bits: satisfies(formula, bits)
        for bits in itertools.product((False, True), repeat=3)
    }


def existential_fold(field: dict[tuple[bool, ...], bool]) -> dict[tuple[bool, ...], bool]:
    """Fold both distinguished hinge values simultaneously; no branch queue."""
    tails = {address[1:] for address in field}
    return {
        tail: field[(False,) + tail] or field[(True,) + tail]
        for tail in tails
    }


def main() -> None:
    clauses = admissible_clauses()
    assert len(clauses) == 26

    formulas = 0
    atomic_cycles = 0
    sat_terminals = 0
    unsat_terminals = 0
    failures = 0

    for size in range(5):
        for formula in itertools.combinations(clauses, size):
            formulas += 1
            field = initial_field(formula)
            direct = any(field.values())

            for _ in VARIABLES:
                field = existential_fold(field)
                atomic_cycles += 1

            terminal = field[()]
            failures += terminal != direct
            sat_terminals += terminal
            unsat_terminals += not terminal

    result = {
        "schema": "TRYX.PNP.CONTINUITY.BENCHMARK.REPLAY.v1",
        "origin": "0D_DISTINCTION",
        "physical_clock_governor": False,
        "sequential_branch_queue": False,
        "snowman_dependencies": 0,
        "admissible_clauses": len(clauses),
        "formulas": formulas,
        "atomic_cycles": atomic_cycles,
        "sat_terminals": sat_terminals,
        "unsat_terminals": unsat_terminals,
        "failures": failures,
        "local_atomic_enaid_closure": "PASS" if failures == 0 else "FAIL",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["receipt_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
