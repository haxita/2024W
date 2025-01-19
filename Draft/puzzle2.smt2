;K12338084

; Update the following
; Circle + Circle = 84
; Square + Circle = 84 + 2 (86)

(set-logic QF_BV)

; Declare bit-vectors (assuming 32 bits for Z_2^32)
(declare-fun Circle () (_ BitVec 32))
(declare-fun Square () (_ BitVec 32))
(declare-fun Triangle () (_ BitVec 32))

; Constraints
(assert (= (bvadd Circle Circle) (_ bv84 32)))
(assert (= (bvadd Square Circle) (_ bv86 32)))
(assert (= (bvsub (bvmul Circle Circle) (bvmul Triangle Circle)) Circle))

; Check and get solution
(check-sat)
(get-model)


;sat
;(
;  (define-fun Circle () (_ BitVec 32)
;    #x8000002a)
;  (define-fun Triangle () (_ BitVec 32)
;    #x00000029)
;  (define-fun Square () (_ BitVec 32)
;    #x8000002c)
;)