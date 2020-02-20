# Base 64 API

> In computer science, Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding. Each Base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit Base64 digits.

> Common to all binary-to-text encoding schemes, Base64 is designed to carry data stored in binary formats across channels that only reliably support text content. Base64 is particularly prevalent on the World Wide Web where its uses include the ability to embed image files or other binary assets inside textual assets such as HTML and CSS files."
> (Wikipedia)

This API would let you encode any file into a base64 string.

## Usage
1. On a terminal go to the folder, `./src/app` 
2. Run `python main.py`.
3. On a browser: `0.0.0.0:8080`
4. Select any file that you want to encode to base64 encoding.
5. Download the json file with the shape { file_name : file_base64_encoding }