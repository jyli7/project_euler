#lang planet neil/sicp

;write a function that takes in a number and returns true if the number is prime, and false if it is not

(define (isprime n try)
  (cond ((= (remainder n try) 0) #f)
        ((> try (sqrt n)) #t)
        (else (isprime n (+ try 1)))))

(define (gpf n factor)
  (if (and (= (remainder n factor) 0) 
           (isprime factor 2))
      factor
      (gpf n (- factor 1))))

(gpf 600851475143 (round (/ 600851475143 2)))
        