(let [sum-of-squares (fn [x] (reduce +  (map #(* % %) (range x))))
      square-of-sum  (fn [x] (#(* % %) (reduce + (range x))))]
  (#(- (square-of-sum %) (sum-of-squares %)) 101))
