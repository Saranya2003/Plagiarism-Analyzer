solve(Rubik, Solution) :- solve_basic(Rubik,Solution).
 
% BFS
solve_basic(Rubik,[]) :- solved(Rubik). 
solve_basic(Rubik,[NewMove | Moves]) :- solve_basic(NewState,Moves), move(NewMove, Rubik, NewState).
 
% A Star, Heuristic by manhattan distance
solve_Astar_1(Rubik,Steps) :- solve_Astar(Rubik,Steps,h_function1), !.
 
% A Star, Heuristic using Corner Edges
solve_Astar_2(Rubik,Steps) :- solve_Astar(Rubik,Steps,h_function2), !.
 
solve_Astar(Rubik,Steps,H_func) :- f_function(Rubik,FunctionF,0,H_func),search([[Rubik,[],FunctionF,0]],ReversedSteps,H_func), reverse(ReversedSteps,Steps).
 
search([[Rubik,Steps,_,_]|_],Steps,_) :- solved(Rubik).
search([CheapestNode|NodeList],Steps,H_func) :- find_followers(CheapestNode,AllFollowers,H_func),insert_followers(AllFollowers,NodeList,NewNodeList),search(NewNodeList,Steps,H_func).
 
find_followers([Rubik,Steps,_,DistanceFromStart],AllFollowers,H_func) :- bagof([Follower,[Move|Steps],F,NewDistanceFromStart],
           (NewDistanceFromStart is DistanceFromStart+1,move(Move,Rubik,Follower),f_function(Follower,F,NewDistanceFromStart,H_func)),
           AllFollowers).
 
% insert_followers(+ListToInsert,+NodeList,-NewNodeList) :- NewNodeList is a list created by inserting nodes from ListToInsert into NodeList,
%                                                   still ordered by function F and without repeated same states of Rubiks. 
insert_followers([ElementToInsert|ListToInsert],NodeList,NewNodeList) :- insert_single(ElementToInsert,NodeList,NodeListWithOneInserted), insert_followers(ListToInsert,NodeListWithOneInserted,NewNodeList).
insert_followers([],NodeList,NodeList).
 
insert_single(ElementToInsert,NodeList,NodeList) :- repeating_nodes(ElementToInsert,NodeList),!.
insert_single(ElementToInsert,[X|NodeList],[ElementToInsert,X|NodeList]) :- not_ordered_nodes_by_F(ElementToInsert,X),!.
insert_single(ElementToInsert,[X|NodeList],[X|NodeListWithOneInserted]) :- insert_single(ElementToInsert,NodeList,NodeListWithOneInserted),!.
insert_single(ElementToInsert,[],[ElementToInsert]).
 
repeating_nodes([Rubik,_,_,_], [[Rubik,_,_,_]|_]).
 
not_ordered_nodes_by_F( [_,_,FunctionF1,_], [_,_,FunctionF2,_] ) :- FunctionF1 < FunctionF2.
 
f_function(Rubik,FunctionF,DistanceFromStart,H_func) :- call(H_func,Rubik,FunctionH),FunctionF is DistanceFromStart + FunctionH.
 
h_function1(R, H) :- h_singleFields(R, H).
h_function2(R, H) :- h_max(R, H).
 
%Misplaced number of cube represent by H variable
h_singleFields(rubik(A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9), H) :-
     same(A1, A5, N11), same(A2, A5, N12), same(A3, A5, N13), same(A4, A5, N14), same(A6, A5, N16), same(A7, A5, N17), same(A8, A5, N18), same(A9, A5, N19),
     same(B1, B5, N21), same(B2, B5, N22), same(B3, B5, N23), same(B4, B5, N24), same(B6, B5, N26), same(B7, B5, N27), same(B8, B5, N28), same(B9, B5, N29),
     same(C1, C5, N31), same(C2, C5, N32), same(C3, C5, N33), same(C4, C5, N34), same(C6, C5, N36), same(C7, C5, N37), same(C8, C5, N38), same(C9, C5, N39),
     same(D1, D5, N41), same(D2, D5, N42), same(D3, D5, N43), same(D4, D5, N44), same(D6, D5, N46), same(D7, D5, N47), same(D8, D5, N48), same(D9, D5, N49),
     same(E1, E5, N51), same(E2, E5, N52), same(E3, E5, N53), same(E4, E5, N54), same(E6, E5, N56), same(E7, E5, N57), same(E8, E5, N58), same(E9, E5, N59),
     same(F1, F5, N61), same(F2, F5, N62), same(F3, F5, N63), same(F4, F5, N64), same(F6, F5, N66), same(F7, F5, N67), same(F8, F5, N68), same(F9, F5, N69),
     H is 48-N11-N12-N13-N14-N16-N17-N18-N19-N21-N22-N23-N24-N26-N27-N28-N29-N31-N32-N33-N34-N36-N37-N38-N39-N41-N42-N43-N44-N46-N47-N48-N49-N51-N52-N53-N54-N56-N57-N58-N59-N61-N62-N63-N64-N66-N67-N68-N69.
 
% same(+Color1, +Color2, -Num) :- For C1 == C2 we have Num = 1. Otherwise N = 0.
same(C1,C2,N) :- C1 == C2, !, N = 1.
same(C1,C2,N) :- C1 \= C2, N = 0.
 
%h_max(+Rubik'sCube,-N) :- maximum value of h_corner, h_e1, h_e2 for cube Rubik'sCube.
h_max(Rubik, N) :- h_corner(Rubik, N1),h_e1(Rubik, N2),h_e2(Rubik, N3),maxm(N1,N2,N3,N).
 
%h_corner(+Rubik'sCube,-N) :- N moves from cube Rubik'sCube to cube Corners with correctly placed corners.
h_corner(Rubik, N) :- solvedCorners(Corners),find_path(Rubik, Corners,Solution),!,length(Solution,N).
 
%h_e1(+Rubik'sCube,-N) :- N moves from cube Rubik'sCube to cube Edges1 with correctly placed half of edges.
h_e1(Rubik, N) :- solvedEdges1(Edges1), find_path(Rubik, Edges1,Solution),!,length(Solution, N).
 
%h_e2(+Rubik'sCube,-N) :-N moves from cube Rubik'sCube to cube Edges2 with correctly placed second half of edges.
h_e2(Rubik, N) :- solvedEdges2(Edges2), find_path(Rubik,Edges2,Solution),!,length(Solution,N).
 
%maxm(+A1, +A2, +A3, -N):- N=max(A1,A2,A3).
maxm(A1,A2,A3,N) :- A1>A2,A1>A3,!,N=A1.
maxm(A1,A2,A3,N) :- A1<A2,A2>A3,!,N=A2.
maxm(A1,A2,A3,N) :- A3>A2,A1<A3,!,N=A3.
maxm(A1,A2,A3,N) :- A1=A2,A1<A3,!,N=A3.
maxm(A1,A2,A3,N) :- A1<A2,A1=A3,!,N=A2.
maxm(A1,A2,A3,N) :- A2=A3,A1>A2,!,N=A1.
maxm(A1,A2,A3,N) :- A1=A2,A1>A3,!,N=A1.
maxm(A1,A2,A3,N) :- A1=A3,A2<A3,!,N=A1.
maxm(A1,A2,A3,N) :- A2=A3,A1<A3,!,N=A2.
maxm(A1,A2,A3,N) :- A1=A2,A1=A3,!,N=A1.
 
%find_path(+Rubik'sCube,+GoalCube,-Steps) :- Steps is a list of steps leading Rubik'sCube cube into GoalCube cube.
find_path(Rubik, Rubik,[]). 
find_path(Rubik, Goal, [NewMove | Moves]) :- !, find_path(NewState,Goal,Moves), move(NewMove, Rubik, NewState).
 
% true_false(T, N) :- for T .. true, return N = 1, otherwise return N = 0.
true_false(T, N) :- T, !, N = 1.
true_false(T, N) :- \+ T, N = 0.
 
% Cube State
 
%solved(?Rubik'sCube) :- Rubik'sCube is solved cube.
solved(rubik(W,W,W,W,W,W,W,W,W,G,G,G,G,G,G,G,G,G,R,R,R,R,R,R,R,R,R,B,B,B,B,B,B,B,B,B,O,O,O,O,O,O,O,O,O,Y,Y,Y,Y,Y,Y,Y,Y,Y)).
 
% solvedCorners(?Rubik'sCube) :- Rubik'sCube is a cube with correct corners.
solvedCorners(rubik(W,_,W,_,W,_,W,_,W,G,_,G,_,G,_,G,_,G,R,_,R,_,R,_,R,_,R,B,_,B,_,B,_,B,_,B,O,_,O,_,O,_,O,_,O,Y,_,Y,_,Y,_,Y,_,Y)).
 
% solvedEdges1(?Rubik'sCube) :- Rubik'sCube is a cube with a first half of correct edges.
solvedEdges1(rubik(_,_,_,_,W,W,_,W,_,_,_,_,G,G,_,_,G,_,_,R,_,_,R,R,_,_,_,_,B,_,B,B,_,_,_,_,_,_,_,_,O,O,_,O,_,_,_,_,Y,Y,_,_,Y,_)).
 
% solvedEdges2(?Rubik'sCube) :-  Rubik'sCube is a cube with a second half of correct edges.
solvedEdges2(rubik(_,W,_,W,W,_,_,_,_,_,G,_,_,G,G,_,_,_,_,_,_,R,R,_,_,R,_,_,_,_,_,B,B,_,B,_,_,O,_,O,O,_,_,_,_,_,Y,_,_,Y,Y,_,_,_)).
 
%Internal Rubik’s Cube Definition
 
%move(clockwise_up, CubeBefore, CubeAfter) :- If we rotate 'up' side ('W'hite color) in clockwise direction of CubeBefore, we get CubeAfter.
%                           
move(clockwise_UP,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(W7,W4,W1,W8,W5,W2,W9,W6,W3,R1,R2,R3,G4,G5,G6,G7,G8,G9,B1,B2,B3,R4,R5,R6,R7,R8,R9,O1,O2,O3,B4,B5,B6,B7,B8,B9,G1,G2,G3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_UP,Before,After) :- move(clockwise_UP,After,Before).
 
%move(clockwise_down, CubeBefore, CubeAfter) :- If we rotate 'down' side ('Y'ellow color) in clockwise direction of CubeBefore, we get CubeAfter.
%
move(clockwise_DOWN,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,R7,R8,R9,R1,R2,R3,R4,R5,R6,B7,B8,B9,B1,B2,B3,B4,B5,B6,O7,O8,O9,O1,O2,O3,O4,O5,O6,G7,G8,G9,Y3,Y6,Y9,Y2,Y5,Y8,Y1,Y4,Y7)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_DOWN,Before,After) :- move(clockwise_DOWN,After,Before).
 
%move(clockwise_left, CubeBefore, CubeAfter) :- If we rotate 'left' side ('G'reen color) in clockwise direction of CubeBefore, we get CubeAfter.
%
move(clockwise_LEFT,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(O9,W2,W3,O6,W5,W6,O3,W8,W9,G7,G4,G1,G8,G5,G2,G9,G6,G3,W1,R2,R3,W4,R5,R6,W7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,Y7,O4,O5,Y4,O7,O8,Y1,R1,Y2,Y3,R4,Y5,Y6,R7,Y8,Y9)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_LEFT,Before,After) :- move(clockwise_LEFT,After,Before).
 
%move(clockwise_right, CubeBefore, CubeAfter) :- If we rotate 'right' side ('B'lue color) in clockwise direction of CubeBefore, we get CubeAfter.
%
move(clockwise_RIGHT,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(W1,W2,R3,W4,W5,R6,W7,W8,R9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,Y3,R4,R5,Y6,R7,R8,Y9,B7,B4,B1,B8,B5,B2,B9,B6,B3,W9,O2,O3,W6,O5,O6,W3,O8,O9,Y1,Y2,O7,Y4,Y5,O4,Y7,Y8,O1)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_RIGHT,Before,After) :- move(clockwise_RIGHT,After,Before).
 
%move(clockwise_front, CubeBefore, CubeAfter) :- If we rotate 'front' side ('R'ed color) in clockwise direction of CubeBefore, we get CubeAfter.
%
move(clockwise_FRONT,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(W1,W2,W3,W4,W5,W6,G9,G6,G3,G1,G2,Y1,G4,G5,Y2,G7,G8,Y3,R7,R4,R1,R8,R5,R2,R9,R6,R3,W7,B2,B3,W8,B5,B6,W9,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,B7,B4,B1,Y4,Y5,Y6,Y7,Y8,Y9)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_FRONT,Before,After) :- move(clockwise_FRONT,After,Before).
 
%move(clockwise_back, CubeBefore, CubeAfter) :- If we rotate 'back' side ('O'range color) in clockwise direction of CubeBefore, we get CubeAfter.
%
move(clockwise_BACK,
    rubik(W1,W2,W3,W4,W5,W6,W7,W8,W9,G1,G2,G3,G4,G5,G6,G7,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,B3,B4,B5,B6,B7,B8,B9,O1,O2,O3,O4,O5,O6,O7,O8,O9,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9),
    rubik(G7,G4,G1,W4,W5,W6,W7,W8,W9,Y7,G2,G3,Y8,G5,G6,Y9,G8,G9,R1,R2,R3,R4,R5,R6,R7,R8,R9,B1,B2,W1,B4,B5,W2,B7,B8,W3,O3,O6,O9,O2,O5,O8,O1,O4,O7,Y1,Y2,Y3,Y4,Y5,Y6,B9,B6,B3)).
% move(moveDescirption, CubeBefore, CubeAfter) :- move(moveDescription, CubeAfter,CubeBefore) is inverse move.
move(counter_clockwise_BACK,Before,After) :- move(clockwise_BACK,After,Before).