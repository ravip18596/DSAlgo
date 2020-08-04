```go
package main
/*
a) There is only one bit set in the binary representation of n (or n is a power of 2)
b) The bits don’t AND(&) any part of the pattern 0xAAAAAAAA

0xAAAAAAAA - is 32 bit binary of even placed set bits - 1010 1010 1010 1010 1010 1010 1010 1010
0x55555555 - is 32 bit binary of odd  placed set bits - 0101 0101 0101 0101 0101 0101 0101 0101

and since 4 16 64 have single set bit at odd place so 16(0001 0000) & 0xAAAAAAAA has be to zero
*/
func isPowerOfFour(num int) bool {
    if num != 0 && (num & (num-1) == 0) && (num & 0xAAAAAAAA == 0){
        return true
    }
    return false
}
```