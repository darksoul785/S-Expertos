#include <iostream>
#include <map>
#include <vector>
#include <string>

using std::map;
using std::string;

int main()
{
    map<int, string> lista{{1, "ABC"}, {2, "AMY"}, {3, "DXC"}, {4, "ABD"}};
    string entrada;
    std::cout << "ingrese los hechos en MAYUSCULAS" << std::endl;
    getline(std::cin, entrada);
    map<int, std::string>::iterator it = lista.begin();
    int counter = 0;
    while (it != lista.end())
    {
        for (int j = 0; j < it->second.size(); j++)
        {
            if (entrada[j] == it->second[j])
            {
                counter += 1;
            }
            else{
                counter = 0;
                j=0;
                break;
            }
        }
        if (counter == 3){
            std::cout << "Tu objeto es el " << it->first << std::endl;
        }
        it ++;
    }
    return 0;
}