(declare-fun Circle   () Int)
(declare-fun Square   () Int)
(declare-fun Triangle () Int)

(assert (= (+ Circle Circle) 10))

(assert (= (+ (* Circle Square) Square) 12))

(assert (= (- (* Circle Square) (* Triangle Circle)) Circle))

(check-sat)
(get-model)

;sat
;(
;  (define-fun Triangle () Int
;    1)
;  (define-fun Circle () Int
;    5)
;  (define-fun Square () Int
;    2)
;)
