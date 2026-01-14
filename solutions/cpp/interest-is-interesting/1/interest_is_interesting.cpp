// interest_rate returns the interest rate for the provided balance.
double interest_rate(double balance) {
    double percentage{};
    if(balance < 0){
        percentage = 3.213;
    }else if(balance >= 0 && balance < 1000){
        percentage = 0.5;
    }else if(balance >= 1000 && balance < 5000){
        percentage = 1.621;
    } else {
        percentage = 2.475;
    }
    return percentage;
}

// yearly_interest calculates the yearly interest for the provided balance.
double yearly_interest(double balance) {
    if(balance < 0)
    {return (balance * (interest_rate(balance)/100)) ;}
    return balance * (interest_rate(balance)/100);
}

// annual_balance_update calculates the annual balance update, taking into
// account the interest rate.
double annual_balance_update(double balance) {
    double result = yearly_interest(balance) + balance;
    return result;
    
}

// years_until_desired_balance calculates the minimum number of years required
// to reach the desired balance.
int years_until_desired_balance(double balance, double target_balance) {
    int count{};
    while(balance < target_balance){
        balance = annual_balance_update(balance);
        count++;
    }
    return count;
}
