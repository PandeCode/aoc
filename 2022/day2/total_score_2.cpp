#include "./utils.cpp"

enum class Move : uint16_t {
	A = 1, // ROCK
	B = 2, // PAPER
	C = 3  // SCISSORS
};

enum class Eg : uint16_t {
	X = 0, // Loss
	Y = 3, // Draw
	Z = 6  // Win
};

Move getMoveThatWinsAgainst(Move m) {
	if(m == Move::A) return Move::B;
	if(m == Move::B) return Move::C;
	if(m == Move::C) return Move::A;
	abort();
};
Move getMoveThatLosesAgainst(Move m) {
	if(m == Move::B) return Move::A;
	if(m == Move::C) return Move::B;
	if(m == Move::A) return Move::C;
	abort();
};

Move MoveFromString(const std::string str) {
	if(str == "A") return Move::A;
	if(str == "B") return Move::B;
	if(str == "C") return Move::C;
	else {
		std::cerr << "Invalid Op move '" << str << "'" << std::endl;
		exit(-1);
	}
}
Eg EgFromString(const std::string str) {
	if(str == "X") return Eg::X;
	if(str == "Y") return Eg::Y;
	if(str == "Z") return Eg::Z;
	else {
		std::cerr << "Invalid Eg move '" << str << "'" << std::endl;
		exit(-1);
	}
}

uint32_t computeGame(Move o, Eg e) {
	Move my_move;

	if(e == Eg::Y) my_move = o;
	else if(e == Eg::X) my_move = getMoveThatLosesAgainst(o);
	else my_move = getMoveThatWinsAgainst(o);

	return (uint16_t) my_move + (uint16_t) e;
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
		Move o = MoveFromString(str_list_2[0]);
		Eg   m = EgFromString(str_list_2[1]);
		scores.push_back(computeGame(o, m));
	}

	std::cout << std::reduce(scores.begin(), scores.end()) << std::endl;

	return 0;
}
