#include<cmath>
#include<iostream>
double daily_rate(double hourly_rate) {
    return 8 * hourly_rate;
}
double apply_discount(double before_discount, double discount) {
    return (before_discount - (before_discount * (discount / 100)));
}
int monthly_rate(double hourly_rate, double discount) {
    return ceil(apply_discount( 22 * daily_rate(hourly_rate), discount ));
}
int days_in_budget(int budget, double hourly_rate, double discount) {
    double mon = budget / apply_discount(daily_rate(hourly_rate), discount);
    return int(mon);
}
