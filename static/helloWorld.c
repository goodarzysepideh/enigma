#include <stdio.h>
#include <string.h>

int check_string(char* input){
  return !strcmp(input, "apdnarG");
}

int main(int argc, char const *argv[]) {
  char input[20];
  scanf("%s", input);
  if (check_string(input) == 1) {
    printf("Hey, you got it! just read it backwards!\n");
  }
  else {
    printf("Try till you get the answer!\n");
  }
  return 0;
}
