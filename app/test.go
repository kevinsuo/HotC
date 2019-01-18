package main
import "fmt"

/*
 * go build test.go
 * ./test
 */

func main() {
    var sum,i int64
    sum=0
    for i=0;i<10000000;i++{
        sum+=i
    }
    fmt.Printf("%d",sum)
}


