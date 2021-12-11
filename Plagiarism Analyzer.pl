main :-
    open('Student1.txt', read, Str),
    read_file(Str,Lines),
    close(Str),
    write(Lines), nl.

read_file(Stream,[]) :-
    at_end_of_stream(Stream).

read_file(Stream,[X|L]) :-
    \+ at_end_of_stream(Stream),
    read(Stream,X),
    read_file(Stream,L).

plagiarismCheck(A,B,Res) :-
    (A = B, Res=1); (A \= B, Res=2).
    %%(A = B, write("Yes")); (A \= B, write("No")).
    %%(A = B, X); (A \= B, X).
    %%isub(A, B, D, [normalize(true),zero_to_one(true)]). %%use the function that currently have

