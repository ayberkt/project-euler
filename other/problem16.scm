;;; MIT Scheme

(define sum-of-digits
  (lambda (num sum)
    (let ((next-digit (modulo num 10))
          (remaining-num (quotient num 10)))
      (if (> remaining-num 0)
        (sum-of-digits remaining-num (+ sum next-digit))
        sum))))


(let ((input (arithmetic-shift 2 999)))
  (sum-of-digits input 1))

