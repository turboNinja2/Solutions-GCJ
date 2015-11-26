let rev my_list =
    let rec aux acc = function
      | [] -> acc
      | head::tail -> aux (head::acc) tail in
    aux [] my_list;;
	
let length my_list =
    let rec aux = function
      | [] -> 0
      | head::tail -> aux (tail) + 1 in
    aux my_list;;
  
let read_file filename = 
	let lines = ref [] in
	let chan = open_in filename in
	try
	  while true; do
		lines := input_line chan :: !lines 
	  done; !lines
	with End_of_file ->
	  close_in chan;
	  rev !lines ;;
  
print_string(string_of_int (length (read_file "B-small-practice.in"))) ;;
