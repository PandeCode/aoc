use std::collections::HashMap;

fn compute_sum(input_vec: &Vec<&str>, priorities: &HashMap<char, u16>) -> u16 {
	let mut sum: u16 = 0;
	for i in input_vec {
		let len = i.len();
		let first = &i[0..(len / 2)];
		let secon = &i[(len / 2)..len];
		for c in first.chars() {
			if secon.contains(c) {
				sum += priorities[&c];
				break;
			}
		}
	}
	sum
}

fn compute_common_sum(input_vec: &Vec<&str>, priorities: &HashMap<char, u16>) -> u16 {
	let mut sum: u16 = 0;

	for (index, value) in input_vec.iter().enumerate() {
		if index % 3 != 0 {
			continue;
		}
		for c in value.chars() {
			if input_vec[index + 1].contains(c) && input_vec[index + 2].contains(c) {
				sum += priorities[&c];
				break;
			}
		}
	}

	sum
}

fn main() {
	let args: Vec<String> = std::env::args().collect();

	let input: String;
	let fun: u8;

	if args.len() > 2 {
		fun = args[1]
			.parse::<u8>()
			.expect("Expected a number as the first arg");
		input = std::fs::read_to_string(&args[2]).expect("Failed To read file");
	} else {
		panic!(
			"At least two args: [ test_number:int:(1|2) ] [ \
			 input_file:str:(./example_input|./input) ]"
		);
	}

	let priorities: HashMap<char, u16> = (b'a'..=b'z')
		.map(char::from)
		.chain((b'A'..=b'Z').map(char::from))
		.enumerate()
		.map(|(k, v)| (v, (k + 1) as u16))
		.collect();

	let input_vec: Vec<&str> = input.split('\n').collect();

	println!(
		"sum = {}",
		match fun {
			1 => compute_sum(&input_vec, &priorities),
			2 => compute_common_sum(&input_vec, &priorities),
			v => panic!("Unknown test {v}. (1|2)"),
		},
	);
}
