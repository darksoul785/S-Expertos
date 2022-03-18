#include <iostream>
#include <map>
#include <vector>

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

    std::cout << " - ";
    printMap(lista);
    return 0;
}
