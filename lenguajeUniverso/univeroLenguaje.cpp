#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>

void generateCombinations(int k, const std::vector<std::string>& symbols, const std::string& filename = "combinations.txt") {
    std::ofstream file(filename, std::ios::app);
    
    for (int i = 0; i < (1 << k); ++i) {
        // Convertir el número a binario y rellenarlo con ceros
        std::string binary_str = std::bitset<32>(i).to_string().substr(32 - k);

        // Convertir el número a una palabra
        std::string word;
        for (char digit : binary_str) {
            word += symbols[digit - '0'];
        }

        // Imprimir y escribir en el archivo
        std::cout << word << std::endl;
        file << word << std::endl;
    }
}

int main() {
    std::vector<std::string> symbols = {"*", "."};
    generateCombinations(20, symbols);

    return 0;
}
