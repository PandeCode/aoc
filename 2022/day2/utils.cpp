#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

template <typename T>
std::ostream& operator<<(std::ostream& stream, const std::vector<T>& listType) {
	stream << "{ ";
	for(auto it = listType.begin(); it != listType.end(); it++)
		stream << *it << (std::next(it) != listType.end() ? ", " : " }");
	return stream;
}

const std::string read_file(const char* filename) {
	std::ifstream file(filename);
	if(!file.is_open()) {
		std::cerr << "Failed to open file '" << filename << "'" << std::endl;
		exit(-1);
	}

	file.seekg(0, std::ios::end);
	size_t size = file.tellg();
	file.seekg(0, std::ios::beg);

	std::string res(size, '\0');
	file.read(res.data(), size);
	return res;
}

std::vector<std::string> split(std::string s, std::string delimiter) {
	size_t                   pos_start = 0, pos_end, delim_len = delimiter.length();
	std::string              token;
	std::vector<std::string> res;

	while((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
		token     = s.substr(pos_start, pos_end - pos_start);
		pos_start = pos_end + delim_len;
		res.push_back(token);
	}

	res.push_back(s.substr(pos_start));
	return res;
}
template <typename T>
T sum(std::vector<T> vec) {
	T s {};
	for(T v: vec) {
		s += v;
	}
	return s;
}
