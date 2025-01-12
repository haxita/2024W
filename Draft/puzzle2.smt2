;K12338084

(declare-fun Circle   () Int)
(declare-fun Square   () Int)
(declare-fun Triangle () Int)

(assert (= (+ Circle Circle) 84))

(assert (= (+ (* Circle Square) Square) 84))

(assert (= (- (* Circle Square) (* Triangle Circle)) Circle))

(check-sat)
(get-model)

;unsat

;keep adding one would not get sat result

;Tweak the second condition, delete the „+ square“ part

(declare-fun Circle   () Int)
(declare-fun Square   () Int)
(declare-fun Triangle () Int)

(assert (= (+ Circle Circle) 84))

(assert (= (* Circle Square) 84))

(assert (= (- (* Circle Square) (* Triangle Circle)) Circle))

(check-sat)
(get-model)

;sat
;(
;  (define-fun Triangle () Int
;    1)
;  (define-fun Circle () Int
;    42)
;  (define-fun Square () Int
;    2)
;)

