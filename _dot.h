#ifndef _DOT_H
#define _DOT_H

// 定义一个类_Dot
class  _Dot{
private:
    // 定义一个指向float类型的指针W
    float* w;
    // 定义一个整数n
    int n;
public:
    // 构造函数，无参数
    _Dot();
    // 构造函数，有参数
    _Dot(int n, float* w);
    // 定义一个函数_dot，参数为指向float类型的指针in_，一个float类型的指针out，一个整数m
    void _dot(float** in_, float* out, int m);
};

#endif