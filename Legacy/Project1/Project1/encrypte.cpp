#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
int main(void)
{

    char src[] = "/stud/?cmd=ls";
    char key2[] = "1581879035863"; //time stamp?

    std::vector<unsigned char> byte_list;

    for (int i = 0; i < strlen(src); i++)
    {
        unsigned char xored = src[i] ^ key2[i % strlen(key2)];
        unsigned char high = xored >> 4;
        unsigned char low = xored & 0xf;
        xored = (low << 4) | high;
        byte_list.push_back(xored);
    }
    std::reverse(byte_list.begin(), byte_list.end());
    for (auto i : byte_list)
    {
        printf("%02x", i);
    }

}