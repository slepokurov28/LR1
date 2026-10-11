#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;


double readNumber(string name) {
    while (true) {
        cout << "Введите " << name << ": ";
        string line;
        if (!getline(cin, line)) exit(0);   

        stringstream ss(line);
        double x;
        string rest;
        if (ss >> x && !(ss >> rest)) {
            return x;
        }
        cout << "Ошибка: нужно ввести число. Попробуйте ещё раз." << endl;
    }
}

class Biquadratic {
private:
    double a, b, c;

public:
    Biquadratic(double a, double b, double c) {
        this->a = a;
        this->b = b;
        this->c = c;
    }


    int printX(double t) {
        if (t > 0) {
            cout << sqrt(t) << " " << -sqrt(t) << " ";
            return 2;
        }
        if (t == 0) {
            cout << 0 << " ";
            return 1;
        }
        return 0;   
    }

    void findRoots() {

        double D = b * b - 4 * a * c;

        if (D < 0) {
            cout << "Корней нет" << endl;
            return;
        }

        double t1 = (-b + sqrt(D)) / (2 * a);
        double t2 = (-b - sqrt(D)) / (2 * a);

        cout << "Корни: ";
        int count = printX(t1);
        if (D > 0) count += printX(t2);   
        if (count == 0) cout << "нет";
        cout << endl;
    }
};

int main() {
    double a = readNumber("a");
    while (a == 0) {
        cout << "a не может быть 0, иначе уравнение не биквадратное." << endl;
        a = readNumber("a");
    }
    double b = readNumber("b");
    double c = readNumber("c");

    Biquadratic eq(a, b, c);
    eq.findRoots();

    return 0;
}
