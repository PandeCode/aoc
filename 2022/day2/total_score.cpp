#include "./utils.cpp"

enum class Op : uint8_t {
	A = 1, // ROCK
	B = 2, // PAPER
	C = 3  // SCISSORS
};

enum class My : uint8_t {
	X = 1, // ROCK
	Y = 2, // PAPER
	Z = 3  // SCISSORS
};

Op OpFromString(const std::string str) {
	if(str == "A") return Op::A;
	if(str == "B") return Op::B;
	if(str == "C")
		return Op::C;
	else {
		std::cerr << "Invalid Op move '" << str << "'" << std::endl;
		exit(-1);
	}
}
My MyFromString(const std::string str) {
	if(str == "X") return My::X;
	if(str == "Y") return My::Y;
	if(str == "Z")
		return My::Z;
	else {
		std::cerr << "Invalid My move '" << str << "'" << std::endl;
		exit(-1);
	}
}
uint32_t computeGame(Op o, My m) {
	uint32_t score = 0;

	if((uint8_t) o == (uint8_t) m) {
		score += 3;
	} // draw
	else if(
	    (o == Op::A and m == My::Y) or (o == Op::B and m == My::Z) or
	    (o == Op::C and m == My::X)) {
		score += 6;
	} // win

	score += (uint8_t) m;

	return score;
}


int main(int argc, const char** argv) {
	if(!argc) {
		std::cerr << "Atleast one arg." << std::endl;
		return -1;
	}
	std::string           input = read_file(argv[1]);
	std::vector<uint32_t> scores;

	for(auto str_list: split(input, "\n")) {
		auto str_list_2 = split(str_list, " ");
		if(str_list_2.size() < 2) break;
		Op o = OpFromString(str_list_2[0]);
		My m = MyFromString(str_list_2[1]);
		scores.push_back(computeGame(o, m));
	}

	std::cout << std::reduce(scores.begin(), scores.end()) << std::endl;

	return 0;
}
