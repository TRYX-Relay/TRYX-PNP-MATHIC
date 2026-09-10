import Mathlib

namespace TRYX.NS

theorem one_tension_accounting (g c d : ℝ) :
    g + max (-(g - c - d)) 0 = c + d + max (g - c - d) 0 := by
  rcases le_total 0 (g - c - d) with h | h
  · rw [max_eq_left h, max_eq_right (neg_nonpos.mpr h)]
    ring
  · rw [max_eq_right h, max_eq_left (neg_nonneg.mpr h)]
    ring

theorem v6_recorded_positive_remainder  :
    max ((82087564089412 : ℝ) / 100000000000 - 13487564089412 / 100000000000 - 588) 0 = 98 := by
  norm_num

theorem v6_atomic_remainder_not_exhausted  :
    max ((82087564089412 : ℝ) / 100000000000 - 13487564089412 / 100000000000 - 588) 0 ≠ 0 := by
  norm_num

end TRYX.NS

#print axioms TRYX.NS.one_tension_accounting
#print axioms TRYX.NS.v6_recorded_positive_remainder
#print axioms TRYX.NS.v6_atomic_remainder_not_exhausted

namespace TRYX.PNP

/-- Semantic assignment carrier only; no constant-cost implementation assumption. -/
def Assignment : Nat → Type
  | 0 => Unit
  | n + 1 => Bool × Assignment n

/-- Exact current-state existential hinge. -/
def hinge {α : Type} (f : Bool × α → Bool) (a : α) : Bool :=
  f (false, a) || f (true, a)

/-- Repeated semantic elimination. Representation costs are not bounded here. -/
def resolve : (n : Nat) → (Assignment n → Bool) → Bool
  | 0, f => f ()
  | n + 1, f => resolve n (hinge f)

theorem boolean_fold_algebra (a b : Bool) :
    (if a || b then (1 : ℤ) else 0) = (if a then 1 else 0) + (if b then 1 else 0) - (if a then 1 else 0) * (if b then 1 else 0) := by
  cases a <;> cases b <;> norm_num

theorem hinge_exact {α : Type} (f : Bool × α → Bool) (a : α) :
    hinge f a = true ↔ ∃ b : Bool, f (b, a) = true := by
  constructor
  · intro h
    have h' : f (false, a) = true ∨ f (true, a) = true := by
      simpa [hinge] using h
    rcases h' with hf | ht
    · exact ⟨false, hf⟩
    · exact ⟨true, ht⟩
  · rintro ⟨b, hb⟩
    cases b <;> simp [hinge, hb]

theorem resolve_correct (n : Nat) (f : Assignment n → Bool) :
    resolve n f = true ↔ ∃ a : Assignment n, f a = true := by
  induction n with
  | zero =>
    constructor
    · intro h
      exact ⟨(), h⟩
    · rintro ⟨a, ha⟩
      cases a
      exact ha
  | succ n ih =>
    rw [resolve, ih]
    constructor
    · rintro ⟨a, ha⟩
      obtain ⟨b, hb⟩ := (hinge_exact f a).mp ha
      exact ⟨(b, a), hb⟩
    · rintro ⟨⟨b, a⟩, ha⟩
      exact ⟨a, (hinge_exact f a).mpr ⟨b, ha⟩⟩

end TRYX.PNP

#print axioms TRYX.PNP.boolean_fold_algebra
#print axioms TRYX.PNP.hinge_exact
#print axioms TRYX.PNP.resolve_correct
