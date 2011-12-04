#lang planet neil/sicp

;checks to see if a given integer n is divisible by all the numbers from "current" to "upper bound"
(define (divisible n current upper-bound)
  (if (> current upper-bound)
      #t
      (if (= (remainder n current) 0)
          (divisible n (+ 1 current) upper-bound)
          #f)))

(divisible 100 1 10)

(define (cycle current end)
  (cond ((divisible current 1 20) (display current))
        ((> current end) (display "none"))
        (else (cycle (+ current 1) end))))

(cycle 1 500000000)