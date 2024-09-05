package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

// Hello returns a greeting for a specific person.
func Hello(name string) (string, error) {
	// if no name is given, return an error with a message
	if name == "" {
		return "", errors.New("empty name")
	}

	message := fmt.Sprintf(randomFormat(), name)
	// message := fmt.Sprintf(randomFormat(), "Fred")

	return message, nil
}

func Hellos(names []string) (map[string]string, error) {
	// a map to associate names with messages
	messages := make(map[string]string)
	// loop through the received slice of names,
	// calling the Hello function to get a message
	// for each name.
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			// cascade the error outwards
			return nil, err
		}
		// in the map, associate the retrieved
		// message with the name.
		messages[name] = message
	}
	return messages, nil
}

// randomFormat returns one of a set of greeting messages.
// The returned message is selected at random.
func randomFormat() string {
	// a slice of message formats.
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}
	count := len(formats)
	index := rand.Intn(count)
	return formats[index]
}

