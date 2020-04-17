#include <stdio.h>

void main(void) {
    {
      int i;
      double result = 0;
      double step = 0.5;
      for(i = 0; i < 10000; i++) result += step;
      printf("%10.24lf\n", result);
    }
    {
      int i;
      double result = 0;
      double step = 0.4;
      for(i = 0; i < 10000; i++) result += step;
      printf("%10.24lf\n", result);
    }
    {
      int i;
      double result = 0;
      double step = 0.7;
      for(i = 0; i < 10000; i++) result += step;
      printf("%10.24lf\n", result);
    }
    printf("%20.34lf\n", 0.7 * 10000);
}
