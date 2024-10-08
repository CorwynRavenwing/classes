package main

import (
	"fmt"
	"log"

	"example/greetings"
)

func main() {
    // Set properties of the predefined Logger, including
    // the log entry prefix and a flag to disable printing
    // the time, source file, and line number.
    log.SetPrefix("greetings: ")
    log.SetFlags(0)

    // request a greeting message
    // message, err := greetings.Hello("Gabriel")
    // message, err := greetings.Hello("")
    // names := []string {"Harry", "Hermione", "", "Ron", "Neville"}
    names := []string {"Harry", "Hermione", "Ron", "Neville"}
    messages, err := greetings.Hellos(names)
    // If an error was returned, print it to the console and
    // exit the program.
    if err != nil {
        log.Fatal(err)
    }

    // If no error was returned, print the returned message
    // to the console.
    // fmt.Println(message)
    fmt.Println(messages)
}

