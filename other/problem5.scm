(define gcd
    (lambda (a b)
        (let ((r (modulo a b)))
            (if (zero? r)
                b
                (gcd b r)))))

(define lcm (lambda (a b) (quotient (* a b) (gcd a b))))

(display (fold-right lcm 1 (cddr (iota 21))))

