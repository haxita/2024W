(set-logic QF_BV)

(declare-fun Circle () (_ BitVec 32))
(declare-fun Square () (_ BitVec 32))
(declare-fun Triangle () (_ BitVec 32))

(assert (= (bvadd Circle Circle) (_ bv10 32)))
(assert (= (bvadd Square Circle) (_ bv12 32)))
(assert (= (bvsub (bvmul Circle Circle) (bvmul Triangle Circle)) Circle))

(check-sat)
(get-model) 

;sat
;(
;  (define-fun Circle () (_ BitVec 32)
;    #x80000005)
;  (define-fun Triangle () (_ BitVec 32)
;    #x80000004)
;  (define-fun Square () (_ BitVec 32)
;    #x80000007)
;)