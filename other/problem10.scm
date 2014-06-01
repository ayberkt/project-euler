(define prime?
  (case-lambda
    [(x)
     (prime? x (cddr  (iota (inexact->exact (round (add1 (sqrt x)))))))]
    [(x test-seq)
     (cond
       ((null? test-seq) #t)
       (else (cond
               ((zero? (modulo x (car test-seq))) #f)
                (else (prime? x (cdr test-seq))))))]))

(display
    (fold-left + 0
        (filter prime? (cddr (iota 2000000)))))
