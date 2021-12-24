#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  int a = strtol(argv[1], NULL, 10);
  int b = strtol(argv[2], NULL, 10);

  long a_score = 0;
  long b_score = 0;
  int turn = 0;
  long dice = 1;
  long t = 0;

  while (a_score < 1000 && b_score < 1000) {
    t += 3;
    long roll = 3 * dice + 3;
    dice += 3;
    if (!turn) {
      a = (a + roll) % 10;
      if(!a){
        a = 10;
      }
      a_score += a;
      turn++;
    }
    else{
      b = (b + roll)%10;
      if(!b){
        b = 10;
      }
      b_score += b;
      turn--;
    }
  }
  long min;
  if (a_score < b_score){
    min = a_score;
  }
  else{
    min = b_score;
  }
  printf("%ld \n",min*t);
  return 0;
}
