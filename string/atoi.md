`Implement atoi which converts a string to an integer.`

```text

 Only the space character ' ' is considered as whitespace character.
 Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

`Solution`

```go
package main
func myAtoi(str string) int {
    x := int64(1<<31)
    INT_MAX := int(x-1)
    INT_MIN := int(-1*x)
    i:=0
    for i<len(str) && str[i]==' '{
        i++
    }
    var ans int
    var sign int
    sign = 1
    if i<len(str) && (str[i]=='+' || str[i]=='-'){
        if str[i]=='-'{
            sign=-1
        }
        i++
    }
    for ;i<len(str);i++{
        if str[i]>='0' && str[i]<='9'{
            ans = ans*10 + int(str[i]-'0')
            if ans*sign >=INT_MAX {
                return INT_MAX
            }
            if ans*sign <=INT_MIN {
                return INT_MIN
            }
        }else{
            break
        }
    }

    return ans*sign
}
```