package main
import "fmt"

/*
 * go build test.go
 * ./test
 *
 * for edge linux: apk add --no-cache git make musl-dev go
 */

func main() {
    var sum,i int64
    sum=0
    for i=0;i<10000000;i++{
        sum+=i
    }
    fmt.Printf("%d",sum)
}


