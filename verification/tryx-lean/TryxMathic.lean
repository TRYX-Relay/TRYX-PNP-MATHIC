import TryxProof

namespace TRYX.PNP.Mathic

/-- Native local-closure measure names, preserved in locked M0-M9 order. -/
inductive Measure where
  | m0TypeSetZero
  | m1Distinction
  | m2CurrentNumber
  | m3VPARotation
  | m4HingeSiblings
  | m5MirrorClosure
  | m6ExistentialFold
  | m7CurrentSuccessor
  | m8OrdinalSuccession
  | m9LocalClosure
  deriving DecidableEq, Repr

/-- The paper-sync MATHIC is required to preserve this exact native order. -/
def nativeOrder : List Measure :=
  [ Measure.m0TypeSetZero
  , Measure.m1Distinction
  , Measure.m2CurrentNumber
  , Measure.m3VPARotation
  , Measure.m4HingeSiblings
  , Measure.m5MirrorClosure
  , Measure.m6ExistentialFold
  , Measure.m7CurrentSuccessor
  , Measure.m8OrdinalSuccession
  , Measure.m9LocalClosure
  ]

theorem nativeOrder_length : nativeOrder.length = 10 := by
  decide

theorem nativeOrder_nodup : nativeOrder.Nodup := by
  decide

/-- M0: the zero-variable assignment carrier is Unit. -/
theorem m0_type_set_zero : Assignment 0 = Unit := by
  rfl

/-- M1: the Boolean distinction is genuine. -/
theorem m1_distinction : (false : Bool) ≠ true := by
  decide

/-- M2: the current formula-state is carried without mutation at admission. -/
def m2CurrentNumber {n : Nat} (f : Assignment n → Bool) : Assignment n → Bool := f

theorem m2_current_exact {n : Nat} (f : Assignment n → Bool) :
    m2CurrentNumber f = f := by
  rfl

/-- M3: typed VPA office rotation has period three. -/
inductive Office where
  | value
  | perception
  | action
  deriving DecidableEq, Repr

def rotate : Office → Office
  | .value => .perception
  | .perception => .action
  | .action => .value

theorem m3_rotate_three (o : Office) :
    rotate (rotate (rotate o)) = o := by
  cases o <;> rfl

/-- M4: expose the two Boolean siblings of the exact current state. -/
def m4HingeSiblings {α : Type} (f : Bool × α → Bool) (a : α) : Bool × Bool :=
  (f (false, a), f (true, a))

/-- M5 receipt: shared truth is recorded once; unmatched truth remains as left/right residue. -/
structure MirrorReceipt where
  shared : Bool
  leftResidue : Bool
  rightResidue : Bool
  deriving DecidableEq, Repr

def m5MirrorClosure (a b : Bool) : MirrorReceipt :=
  { shared := a && b
  , leftResidue := a && !b
  , rightResidue := !a && b
  }

def m5RetainedTruth (r : MirrorReceipt) : Bool :=
  r.shared || r.leftResidue || r.rightResidue

/-- M5 preserves exactly the truth carried by the sibling OR while retaining provenance lanes. -/
theorem m5_mirror_preserves_truth (a b : Bool) :
    m5RetainedTruth (m5MirrorClosure a b) = (a || b) := by
  cases a <;> cases b <;> decide

/-- M6: exact Boolean existential fold. -/
def m6ExistentialFold (a b : Bool) : Bool :=
  a || b

theorem m6_after_m5 (a b : Bool) :
    m5RetainedTruth (m5MirrorClosure a b) = m6ExistentialFold a b := by
  exact m5_mirror_preserves_truth a b

def m6FoldAt {α : Type} (f : Bool × α → Bool) (a : α) : Bool :=
  m6ExistentialFold (f (false, a)) (f (true, a))

theorem m6_matches_hinge {α : Type} (f : Bool × α → Bool) (a : α) :
    m6FoldAt f a = hinge f a := by
  rfl

theorem m6_existential_exact {α : Type} (f : Bool × α → Bool) (a : α) :
    m6FoldAt f a = true ↔ ∃ b : Bool, f (b, a) = true := by
  simpa [m6_matches_hinge] using hinge_exact f a

/-- M7: the folded hinge becomes the exact next current state. -/
def m7CurrentSuccessor {α : Type} (f : Bool × α → Bool) : α → Bool :=
  hinge f

theorem m7_successor_exact {α : Type} (f : Bool × α → Bool) :
    m7CurrentSuccessor f = hinge f := by
  rfl

/-- M8: ordinal succession repeats the same semantic elimination on each exact successor. -/
def m8OrdinalSuccession (n : Nat) (f : Assignment n → Bool) : Bool :=
  resolve n f

/-- M9: local closure is the scalar result after finite semantic elimination. -/
def m9LocalClosure (n : Nat) (f : Assignment n → Bool) : Bool :=
  m8OrdinalSuccession n f

theorem m9_local_closure_correct (n : Nat) (f : Assignment n → Bool) :
    m9LocalClosure n f = true ↔ ∃ a : Assignment n, f a = true := by
  simpa [m9LocalClosure, m8OrdinalSuccession] using resolve_correct n f

/-- End-to-end MATHIC semantic pass: the native M6-M9 execution returns true exactly when a finite witness exists. -/
theorem localClosureMathicPass (n : Nat) (f : Assignment n → Bool) :
    m9LocalClosure n f = true ↔ ∃ a : Assignment n, f a = true :=
  m9_local_closure_correct n f

end TRYX.PNP.Mathic

#print axioms TRYX.PNP.Mathic.nativeOrder_length
#print axioms TRYX.PNP.Mathic.nativeOrder_nodup
#print axioms TRYX.PNP.Mathic.m3_rotate_three
#print axioms TRYX.PNP.Mathic.m5_mirror_preserves_truth
#print axioms TRYX.PNP.Mathic.m6_existential_exact
#print axioms TRYX.PNP.Mathic.m9_local_closure_correct
#print axioms TRYX.PNP.Mathic.localClosureMathicPass
