;;; Racket Scheme

(define fibonacci 
  (case-lambda 
    ((limit) (fibonacci limit '(1 1)))
    ((limit seq) (let ((next-element (+ (car seq) (cadr seq))))
                   (if (not (> next-element limit))
                       (fibonacci limit (cons next-element seq))
                       seq)))))

(apply + (filter even? (fibonacci 4000000)))
