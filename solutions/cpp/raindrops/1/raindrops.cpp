#include<string>
#include "raindrops.h"

namespace raindrops {
    std::string convert(int number){
        std::string result = "";
        if(number == 1){
            result += std::to_string(number);
        }
        else if(number%3 == number%5 && number%3 == number%7){
            result += "PlingPlangPlong";
        }else if (number%3 == number%5 && number%5 == 0){
            result += "PlingPlang";
        }else if (number%3 == number%7 && number%3 == 0){
            result += "PlingPlong";
        }else if(number%5 == number%7 && number%5 == 0){
            result += "PlangPlong";
        }else if(number%3 == 0){
            result += "Pling";
        }else if (number%5 == 0){
            result += "Plang";
        }else if (number%7 == 0){
            result += "Plong";
        }else{
            result += std::to_string(number);
        }
        return result;
    }
    

}  // namespace raindrops
