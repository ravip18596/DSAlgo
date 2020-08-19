```text
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.
     
    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".
     
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

```
`Time - O(N) Space - O(N)`

```go
package main
import "strings"
//strings are immutable in Golang/Java/Python
// everyTime we use + operator, new memory is allocated and copied from old string
// use string Builder or use join operation
func toGoatLatin(S string) string {
    word := strings.Split(S," ")
    for i:=0;i<len(word);i++{
        if word[i][0]=='a' || word[i][0]=='A' || word[i][0]=='e' || word[i][0]=='E' || word[i][0]=='i' || word[i][0]=='I' || word[i][0]=='o' || word[i][0]=='O' || word[i][0]=='u' || word[i][0]=='U'{
            word[i] = vowel(word[i],i+1)
        }else{
            word[i] = consanant(word[i],i+1)
        }
    }
    return strings.Join(word," ")
}

func vowel(word string,wordcnt int) string{
    var str strings.Builder
    str.WriteString(word)
    str.WriteString("ma")
    chars := make([]rune,wordcnt,wordcnt)
    for i:=0;i<wordcnt;i++{
        chars[i] = 'a'
    }
    str.WriteString(string(chars))
    return str.String()
}

func consanant(word string,wordcnt int) string{
    wordRune := []rune(word)
    if len(wordRune)>1{
        wordRune = append(wordRune[1:],wordRune[0])
    }
    wordRune = append(wordRune,[]rune{'m','a'}...)
    for i:=0;i<wordcnt;i++{
        wordRune = append(wordRune,'a')
    }
    return string(wordRune)
}
```