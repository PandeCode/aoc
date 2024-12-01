all: test_1_example test_1 test_2_example test_2

total_score: total_score.cpp utils.cpp
	$(CXX) -std=c++20 total_score.cpp -o total_score

total_score_2: total_score_2.cpp utils.cpp
	$(CXX) -std=c++20 total_score_2.cpp -o total_score_2

test_1_example: total_score
	./total_score ./example_input

test_2_example: total_score_2
	./total_score_2 ./example_input

test_1: total_score
	./total_score ./input

test_2: total_score_2
	make total_score_2
	./total_score_2 ./input

clean:
	rm ./total_score ./total_score_2
