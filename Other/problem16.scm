;; MIT Scheme

(define digits
  (lambda (n)
    (map string->number 
      (map char->string 
        (string->list (number->string n))))))

(define sum-digits (lambda (n) (reduce + '() (digits n))))

(let ((input (arithmetic-shift 2 999)))
  (sum-digits input))

