#include "my_lib.h"
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

float omean (int v[], int x)
{
  int sum = 0;
  for(int i = 0; i<x ; i++)
  {
    sum += v[i];
  }
  float mean = (sum/x);
  return mean;
}

float omax (int v[], int x)
{
  int i;
  float mx = v[0];
  for (i = 1; i<x; i++)
  {
    if (v[i]>mx)
    {
      mx = v[i];
    }
  }
  return mx;
}

float osd  (int v[], int x)
{
  float mean = opmean (v, x);
  float arr[x];
  float sum = 0;
  float variance;
  float sd;
  for (int i = 0; i<x; i++)
  {
    arr[i] = (v[i]-mean) * (v[i])-mean);
  }
  for (int i = 0; i<x; i++)
    {
      sum += arr[i];
    }
    variance = sum/x;
    sd = sqrt(variance);
    return sd;
  }
