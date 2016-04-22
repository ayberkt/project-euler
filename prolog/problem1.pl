divides(X,Y) :- 0 is Y mod X.

sumlist([],0).
sumlist([H|T],Sum) :-
    sumlist(T,SumOfTail),
    Sum is H + SumOfTail.

mult_3_or_5(X) :-
    between(1,999,X),
    (divides(3,X) -> true; divides(5,X)).

find_sum(X) :-
    findall(Y,mult_3_or_5(Y),L),
    sumlist(L,X).
