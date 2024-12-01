#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <pthread.h>
#include <string>
#include <unordered_map>
#include <vector>

template <typename T, size_t size>
std::ostream& operator<<(std::ostream& stream, const std::array<T, size>& listType) {
	stream << "{ ";
	for(auto it = listType.begin(); it != listType.end(); it++)
		stream << *it << (std::next(it) != listType.end() ? ", " : " }");
	return stream;
}
template <typename T>
std::ostream& operator<<(std::ostream& stream, const std::vector<T>& listType) {
	stream << "{ ";
	for(auto it = listType.begin(); it != listType.end(); it++)
		stream << *it << (std::next(it) != listType.end() ? ", " : " }");
	return stream;
}

std::vector<std::string> split(const std::string& s, const std::string& delimiter) {
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
std::string readFile(const std::string& filename) {
	std::ifstream file(filename);
	if(!file.is_open()) throw std::runtime_error("Failed to open file: " + filename);
	file.seekg(0, std::ios::end);
	size_t size = file.tellg();
	file.seekg(0, std::ios::beg);
	std::string result(size, '\0');
	file.read(result.data(), size);
	return result;
}

using ListPair = std::pair<std::vector<std::string>, std::vector<std::string>>;

ListPair processInput(const std::string& input) {
	auto lines = split(input, "\n");

	std::vector<std::string> list_1;
	std::vector<std::string> list_2;

	list_1.reserve(lines.size());
	list_2.reserve(lines.size());

	for(std::string line: lines) {
		auto nums = split(line, " ");
		list_1.push_back(nums[0]);
		list_2.push_back(nums[3]);
	}

	std::sort(list_1.begin(), list_1.end());
	std::sort(list_2.begin(), list_2.end());

	return std::pair(std::move(list_1), std::move(list_2));
}

#define IGNORE_ABORT(x) \
	try {           \
		x;      \
	} catch(std::exception & e) {}

int32_t processSum(const ListPair& lists) {
	std::int32_t sum = 0;
	auto         s   = lists.first.size();
	for(size_t i = 0; i < s; i++) {

		auto a = lists.first[i];
		auto b = lists.second[i];

		IGNORE_ABORT(auto a_i = std::stoi(a); auto b_i = std::stoi(b);
			     sum += abs(a_i - b_i););
	}

	return sum;
}

int32_t processSimilarity(const ListPair& lists) {
	std::int32_t sum = 0;

	auto s           = lists.first.size();

	std::unordered_map<std::string, std::pair<int32_t, int32_t>> map;
	map.reserve(s);

	auto list_1 = lists.first;

	for(const auto& key: list_1) {
		if(!map.contains(key)) {
			map.insert({key, std::pair(0, 1)});
		} else {
			map[key].second++;
			continue;
		}

		for(const auto& num: lists.second)
			if(num == key) map[key].first++;
	}

	IGNORE_ABORT(for(const auto& [key, value]
			 : map) { sum += std::stoi(key) * value.first * value.second; });

	return sum;
}

int main() {
	std::string input = R"(3   4
4   3
2   5
1   3
3   9
3   3)";

	input             = readFile("input");

	auto lists        = processInput(input);

	std::cout << "Sum: " << processSum(lists) << std::endl;
	std::cout << "Similarity: " << processSimilarity(lists) << std::endl;

	return 0;
}
