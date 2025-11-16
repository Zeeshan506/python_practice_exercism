#include <array>
#include <string>
#include <vector>
#include <iostream>

using namespace std;
// Round down all provided student scores.
vector<int> round_down_scores(vector<double> student_scores) {
    vector<int> result;
    int i = 0;    
    while(student_scores.size() > i){
        int temp = student_scores.at(i);
        result.push_back(temp);
        i++;}
    return result;}

// Count the number of failing students out of the group provided.
int count_failed_students(std::vector<int> student_scores) {
    // TODO: Implement count_failed_students
    int i = 0;
    int count = 0;
    while(student_scores.size() > i){
        if(student_scores.at(i) <= 40){
            count++;
        } 
        i++;
    }
    return count;
}

// Create a list of grade thresholds based on the provided highest grade.
std::array<int, 4> letter_grades(int highest_score) {
    // TODO: Implement letter_grades
    int leftover = (highest_score - 40)/4;
    array<int,4> scoreList{};
    scoreList[0] = 41;
    for(int i= 1; i < 4; i++){
    scoreList[i] = scoreList[i-1] + leftover;
    }
    return scoreList;
}

// Organize the student's rank, name, and grade information in ascending order.
std::vector<std::string> student_ranking(
    std::vector<int> student_scores, std::vector<std::string> student_names) {
    // TODO: Implement student_ranking
    vector<string> result;
    string temp = "";
    int i =0 ;
    while(student_names.size() > i){
        temp = temp + to_string(i+1) + ". " + student_names.at(i) + ": " + to_string(student_scores.at(i));
        result.push_back(temp);
        temp = "";
        i++;
    }
    return result;
}

// Create a string that contains the name of the first student to make a perfect
// score on the exam.
std::string perfect_score(std::vector<int> student_scores,
                          std::vector<std::string> student_names) {
    // TODO: Implement perfect_score
    for(int i =0; i < student_scores.size();i++){
         if(student_scores.at(i) == 100 ){
             return student_names.at(i);
         }
    }
    return "";
}
