#include <iostream>

static int dayArr[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

// SUN;0 MON: 1
int main() {
    int month, day;
    int day_count = 0;

    scanf("%d %d", &month, &day);
    if(month < 1 || month > 12)
    {
        printf("Wrong month input\n");
        return -1;
    }
    if(day < 1 || day > 31)
    {
        printf("Wrong day input\n");
        return -1;
    }

    for(int i = 1; i < month; i++) {
        day_count += dayArr[i];
    }
    day_count += day;

    day_count %= 7;

    if(day_count == 0)
        printf("SUN\n");
    else if(day_count == 1)
        printf("MON\n");
    else if(day_count == 2)
        printf("TUE\n");
    else if(day_count == 3)
        printf("WED\n");
    else if(day_count == 4)
        printf("THU\n");
    else if(day_count == 5)
        printf("FRI\n");
    else if(day_count == 6)
        printf("SAT\n");
    else
        printf("WRONG Calculation\n");

    return 0;
}
