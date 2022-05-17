#include <iostream>
#include <map>
#include <chrono>
#include <fstream>
#include <cmath>

int main(){

    std::map<int, int> mp;
    std::ofstream output("cpp_data.dat");

    std::chrono::system_clock::time_point start;
    std::chrono::system_clock::time_point end;
    int count = 0;
    for (int i = 1; i <= std::pow(10, 8); i *= 10)
    {
        mp.clear();
        start = std::chrono::system_clock::now();
    
        for (int j = 0; j < i; j++){
            mp.insert(std::pair<int, int>(j, j));
        }
        end = std::chrono::system_clock::now();
        output << "10^" << count << '\t' << std::chrono::duration<double, std::milli>(end - start).count()
               << '\t' << ((sizeof(int) + sizeof(int)) * mp.size()) + sizeof(std::map<int, int>) << '\n';

        count++;
    }

    output.close();
    return 0;
}
