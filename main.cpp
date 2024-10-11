#include <iostream>
#include <stdlib.h>
#include <time.h>
#include "_dot.h"

int main(){
    const int M =3;
    const int N =2;

    float * w = new float[N];
    for (int i=0;i<N;i++)
        w[i] = (i+0.0)/N;
    

    _Dot D(N,w);

    float ** in_ = new float*[M];
    for (int i = 0; i<M;i++){
        in_[i] = new float[N];
        for (int j = 0;j<N;j++){
            in_[i][j] = ((float)rand() / RAND_MAX);
        }
    }
    
    float * out = new float[M];
    
    D._dot(in_,out,M);

    for (int i = 0; i<M;i++){
        std::cout<<out[i]<<" "<<std::endl;
    }

    return 0;
}