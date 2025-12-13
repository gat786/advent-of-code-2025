package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	// Open the file
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// Create a new scanner to read the file line by line
	scanner := bufio.NewScanner(file)

	// var startingPoint int16 = 50
	// var nozs = 0
	// Loop through the file and read each line
	var biggestNumber = 0
	for scanner.Scan() {
		line := scanner.Text() // Get the line as a string
		number := line[1:]
		parsedNumber, err := strconv.ParseInt(number, 2, 16)
		if err != nil {
			fmt.Printf("Failed parsing int: {number}")
		}
		if parsedNumber > int64(biggestNumber) {
			biggestNumber = int(parsedNumber)
		}
		// if strings.HasPrefix(line, fmt.Sprint("L")) {

		// } else {

		// }

	}

	fmt.Println("Biggest number: ", biggestNumber)
	// Check for errors during the scan
	if err := scanner.Err(); err != nil {
		log.Fatalf("error reading file: %s", err)
	}
}
