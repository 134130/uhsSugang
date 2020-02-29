#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<locale>

int foo(char c) {
    if (c >= '0' && c <= '9') {
        return c - '0';
    }
    return c - 'a' + 10;
}

int main(void)
{
    std::wcout.imbue(std::locale("kor"));
    char src[] = "453475b440155404250534c41405a0156585354464f1d544c464e1";
    char key2[] = "1581905149865"; //time stamp?

    std::vector<char> byte_list;

    for (int i = strlen(src) - 1; i >= 0; i--) {
        byte_list.push_back(src[i]);
    }

    for (int i = 0; i < byte_list.size(); i+=2) {
        unsigned char ch = foo(byte_list.at(i)) << 4 | foo(byte_list.at(i + 1));
        unsigned char key = key2[i / 2];

        unsigned char xored = ch ^ key;
        printf("%c", xored);
    }
}