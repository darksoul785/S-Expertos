#include <iostream>
#include <string>
#include <map>
#include <iterator>

using std::map;
using std::string;

int main()
{
    map<int, string> lista = {{1, "ABC"},
                              {2, "AMY"},
                              {3, "DXC"},
                              {4, "ABD"}};

    string nope = "";
    string yep = "";
    int counter = 0;
    map<int, std::string>::iterator it = lista.begin();

    while (it != lista.end())
    {
        string arreglo;
        for (int i = 0; i < lista.size(); i++)
        {
            arreglo = it->second;
            std::cout << arreglo << std::endl;
        }
        it++;
    }

return 0;
}