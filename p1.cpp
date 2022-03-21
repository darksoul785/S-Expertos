#include <iostream>
#include <map>
#include <vector>
#include <iterator>

using std::cout;
using std::map; 
template <typename Map>
void printMap(Map &m)
{
    std::cout << "[";
    for (auto &item : m)
    {
        cout << item.first << ":" << item.second << " ";
    }
    std::cout << "]\n";
}

int main()
{
    map<int, std::string> lista = {{1, "ABC"},
                                   {2, "AMY"},
                                   {3, "ABD"},
                                   {4, "DXC"}};

    int counter = 0;
    bool flag = false;
    map<int, std::string>::iterator it = lista.begin();
    while (it != lista.end())
    {
        for (int i = 0; i < it->second.size(); i++)
        {
            char r;
            std::cout << "su lista tiene la letra " << it->second[i] << "?\nPresione 'Y' para si o 'N' para no\n";
            std::cin >> r;
            if(r == 'Y' || r == 'y'){
                counter += 1;
            }
            else{
                break;
            }
        }
        if (counter == 3){
            std::cout << "Tu objeto es el: " << it->first << std::endl;
            flag = true;
            break;
        }
        else{
            counter = 0;
        }
        it++;
    }

    if (flag == false){
        std::cout << "No se encontro tu objeto" << std::endl;
    }
    else{
        std::cout << "Se encontro el objeto con exito" << std::endl;
    }
    return 0;
}
