#include <iostream>
#include <stack>
#include <cctype>
using namespace std;

int precedence(char op)
{
    if (op == '+' || op == '-')
    {
        return 1;
    }
    else if (op == '*' || op == '/')
    {
        return 2;
    }
    else if (op == '^')
    {
        return 3;
    }
    return 0;
}

string infix_postfix(string exp)
{
    stack<char> operators;
    string postfix = "";

    for (int i = 0; i < exp.length(); i++)
    {
        char c = exp[i];
        if (isalnum(c))
        {
            postfix += c;
        }
        else if (c == '(')
        {
            operators.push(c);
        }
        else if (c == ')')
        {
            while (!operators.empty() && operators.top() != '(')
            {
                postfix += operators.top();
                operators.pop();
            }
            operators.pop();
        }
        else
        {
            while (!operators.empty() && precedence(operators.top()) >= precedence(c))
            {
                postfix += operators.top();
                operators.pop();
            }
            operators.push(c);
        }
    }

    while (!operators.empty())
    {
        postfix += operators.top();
        operators.pop();
    }
    cout << postfix;
    return postfix;
}

bool isop(char c)
{
    if (c == '+' || c == '-' || c == '*' || c == '/')
    {
        return 1;
    }
    return 0;
}
int eval(string exp)
{
    stack<int> s;
    for (int i = 0; i < exp.length(); i++)
    {
        if (isop(exp[i]))
        {
            int a = s.top();
            s.pop();
            int b = s.top();
            s.pop();
            int result;
            if (exp[i] == '+')
            {
                result = a + b;
            }
            else if (exp[i] == '-')
            {
                result = b - a;
            }
            else if (exp[i] == '*')
            {
                result = a * b;
            }
            else
            {
                result = b / a;
            }
            s.push(result);
        }
        else
        {
            s.push(exp[i]);
        }
    }
    return s.top();
}
int main()
{
    string exp = "2+3*4";
    string postfix = infix_postfix(exp);
    cout << eval(postfix);
}