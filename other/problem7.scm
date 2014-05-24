;;; Chez Scheme / R6RS Standard

(define prime?
  (case-lambda
    ((num) 
     (prime? num (cddr (iota (inexact->exact (+ (ceiling (sqrt num)) 1))))))
    ((num test-seq)
     (if (null? test-seq)
         #t ;; num is a prime if test-list is exhausted
         (if (eq? 0 (modulo num (car test-seq)))
             #f ;; if any number from test-seq divides: num not a prime
             (prime? num (cdr test-seq)))))))

(define primes
  (case-lambda
    ((limit) (primes limit '(3 2) 4 2))
    ((limit seq candidate prime-count)
     (if (= prime-count limit)
         seq
         (if (prime? candidate)
             (primes 
               limit (cons candidate seq) (+ candidate 1) (+ prime-count 1))
             (primes 
               limit seq (+ candidate 1) prime-count))))))

(display (car (primes 10001)))
