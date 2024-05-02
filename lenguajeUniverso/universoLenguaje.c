#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

/**
 * @brief Convierte un número decimal a binario
*/
char* decimalToBinary(int num, int size) {
  char *binary = (char *)calloc(size, sizeof(char)); // Se asume un entero de 32 bits
  int i = 0;

  // Verifica si se pudo reservar memoria
  if(binary == NULL){
    printf("No se pudo reservar memoria\n");
    exit(1);
  }

  // Convierte el número decimal a binario
  while (num > 0) {
      binary[i] = num % 2;
      num = num / 2;
      i++;
  }
  return binary;
}

/**
 * @brief Limpia el archivo antes de escribir
*/
void cleanFile(char* filename){
  FILE *file = fopen(filename, "w");
  if(file == NULL){
    printf("No se pudo abrir el archivo\n");
    exit(1);
  }
  fclose(file);
}

/**
 * @brief Genera todas las combinaciones posibles de un lenguaje binario con los simbolos de longitud k
*/
void generateCombinations(int posiciones, char *symbols, int size, char *filename, int start){
  int k = 1 << posiciones;  // Calcula 2^posiciones de manera eficiente
  // Limpiamos el archivo
  cleanFile(filename);
  // Abrimos el archivo en modo append
  FILE *registerFile = fopen(filename, "a+");

  if(registerFile == NULL){
    printf("No se pudo abrir el archivo\n");
    exit(1);
  }
  // Agregamos un encabezado
  fprintf(registerFile, "combination\n");

  // Reservamos memoria para el buffer
  char *buffer = (char *)calloc(posiciones, sizeof(char));
  if (buffer == NULL) {
      printf("No se pudo reservar memoria para el búfer\n");
      exit(1);
  }

  // Contamos hasta el numero k-esimo
  for (int i = start; i < k; i++){
    // Obtenemos su binario 
    char *binary = decimalToBinary(i, size);
    // Transformamos el binario a los simbolos
    for(int j = 0; j < posiciones; j++){
      // Escribimos en el regsitro
      buffer[j] = symbols[binary[j]];
    }
    buffer[posiciones] = '\0';
    // Escribimos el bufer en el archivo
    fputs(buffer, registerFile);
    // Agregamos un salto de linea
    fputc('\n', registerFile);
    // Liberamos la memoria
    free(binary);
  }
  fclose(registerFile);
  free(buffer);
  printf("Se han generado todas las combinaciones posibles\n");
}

int main() {
  // Registra el tiempo de inicio
  clock_t inicio = clock();

  int numeroPosiciones = 28; // Número de posiciones
  int strLenght = 32; // Longitud de la cadena en bits
  int start = 0; // Número de combinación inicial
  char symbols[] = "*.";
  char filename[] = "combinations.csv";

  generateCombinations(numeroPosiciones, symbols, strLenght, filename, start);

  // Registra el tiempo de finalización
  clock_t fin = clock();

   // Calcula el tiempo transcurrido en segundos
  double tiempo_transcurrido = ((double)(fin - inicio)) / CLOCKS_PER_SEC;

  printf("\nEl tiempo de ejecución fue %.4f segundos.\n", tiempo_transcurrido);

  return 0;
}