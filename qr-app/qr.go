package main

import qrcode "github.com/skip2/go-qrcode"

func main() {
	qrcode.WriteFile("https://www.google.com", qrcode.Medium, 256, "qrcode.png")
}



