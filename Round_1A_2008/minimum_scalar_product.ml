open String

let rec halve = function
    | []
    | [_] as t1 -> t1, []
    | h::t ->
        let t1, t2 = halve t in
          h::t2, t1
;;

let rec merge = function
    | list, []
    | [], list -> list
    | h1::t1, h2::t2 ->
        if h1 <= h2 then
          h1 :: merge (t1, h2::t2)
        else
          h2 :: merge (h1::t1, t2)
in

let rec merge_sort = function
    | []
    | [_] as list -> list
    | list ->
        let l1, l2 = halve list in
          merge (merge_sort l1, merge_sort l2)
in
  
let reverse list = 
    let rec aux acc = function
      | [] -> acc
      | head::tail -> aux (head::acc) tail in
    aux [] list in
	
let length my_list =
    let rec aux = function
      | [] -> 0
      | head::tail -> aux (tail) + 1 in
    aux my_list in

let read_file filename = 
	let lines = ref [] in
	let chan = open_in filename in
	try
	  while true; do
		lines := input_line chan :: !lines 
	  done; !lines
	with End_of_file ->
	  close_in chan;
	  reverse !lines in

let print_list list = 
	print_string (String.concat "\n" list) in
	  
let dot a b = 
	let rec aux list1 list2 = function
		| [],[] -> 0
		| h1::t1,h2::t2 -> h1 * h2 + aux t1 t2 in
	aux a b in	

let solve a b = dot (merge_sort a) (reverse (merge_sort b) )  in

print_list( read_file "A-small-practice.in") ;;


	