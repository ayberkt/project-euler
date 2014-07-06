(define (self-power-sum limit iter result)
  (if (> iter limit)
      result
      (self-power-sum limit
                      (add1 iter)
                      (+ result (expt iter iter)))))

(display (remainder (self-power-sum 1000 1 0)
                    (expt 10 10)))
