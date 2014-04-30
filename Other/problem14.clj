(ns problem14)

(use '[clojure.test :only (is)])

(defn count-collatz
  "Returns a vector [a b] where b is the 
  number that initiated the sequence, and
  a is the number of steps taken to reach 1."
  [input-num]
  (loop [num input-num count 1]
  (if (= num 1)
    (vector count input-num)
    (do (if (= (mod num 2) 0)
      (recur (/    num 2)     (inc count))
      (recur (+ (* num 3) 1)  (inc count)))))))

;; Test case from the project description.
(is (= (count-collatz 13) [10 13]))

(loop [number 1 peak [0 0]]
    (if (>= number 1e6)
      (str "Longest chain is " (last peak))
      (do (let [result (count-collatz number)]
        (do (if (> (first result) (first peak))
          (recur (inc number) result)
          (recur (inc number)   peak)))))))
