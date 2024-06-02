# Verncrypt-VernamCipher

The Vernam Cipher is a method of encrypting alphabetic text. It is a symmetric key cipher where the same key is used for both encryption and decryption. This implementation in Python allows you to encrypt and decrypt text using the Vernam Cipher method.




## Table of contents

* [Prerequisites](##Prerequisites)
* [Installation](##Installation)
* [Usage](##Usage)
* [Examples](##Examples)
* [Contributing](##Conributing)


## Prerequisites
Before you begin, ensure you have met the following requirements:

* You have installed Python 3.x.
* You have a basic understanding of Python programming.



## Installation
To install and set up the Vernam Cipher, follow these steps:

* Clone the repository
    ```sh
    https://github.com/snadeem03/Verncrypt-VernamCipher
     ```
* Add the executable path to environment variables
* Run the executable. 



## Usage
To use the Vernam Cipher, follow these steps:

* Open the terminal
* Run the executable with appropriate arguments
    ```sh
    verncyrpt -e "yourplaintext" "yourkey"

    ```
    or

    ```sh
    verncrypt -d "yourencryptedtext" "yourkey"
    ```

* The script will output the encrypted or decrypted text.



## Examples
Here are some examples of how to use the Vernam Cipher:

#### Encrypting text

```sh
verncrypt -e hello madee

```

*Output*

```mathematica
Encrypted Text: teops
Key: madee
```

#### Decrypting text

```sh
verncrypt -d teops madee
```

*Output*

```mathematica
Decrypted Text: hello
```


## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

* Fork this project
* Create your Feature Branch (git checkout -b feature/AmazingFeature)
* Commit your Changes (git commit -m 'Add some AmazingFeature')
* Push to the Branch (git push origin feature/AmazingFeature)
* Open a Pull Request





## Acknowledgements

 - [Vernam-Cipher](https://patents.google.com/patent/US20170180117A1/en)


