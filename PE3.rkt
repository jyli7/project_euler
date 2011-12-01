#lang planet neil/sicp

;write a function that takes in a number and returns true if the number is prime, and false if it is not

(define (isprime n try)
  (cond ((= (remainder n try) 0) #f)
        ((> try (sqrt n)) #t)
        (else (isprime n (+ try 1)))))

(define (gpf x try)
  (if (and (= (remainder x try) 0)
           (isprime try 2))
      ((display try) (newline) (gpf (/ x try) 2))
      (gpf x (+ try 1))))

(gpf 100 2)