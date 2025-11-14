#include <string>

namespace log_line {
std::string message(std::string line) {
    int gap_index = line.find(" ");
    std::string res = line.substr(gap_index+1);
    return res;
}

std::string log_level(std::string line) {
    int brace_start = line.find("[");
    int brace_end = line.find("]");
    std::string res = line.substr(brace_start+1,brace_end-1);
    return res;
}

std::string reformat(std::string line) {
    // return the reformatted message
    std::string message_part = log_line::message(line);
    std::string log_part = log_line::log_level(line);
    std::string res = message_part + " (" + log_part + ")" ;  
    return res;
    
}
}  // namespace log_line
