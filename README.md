# PyPasGen
![CodeFactor](https://www.codefactor.io/repository/github/elitejake/pypassgen/badge?s=be530c11c919e0528667025dca77e651afcc326f)

**PyPassGen** is an easy-to-use password generator which can produce [cryptographically strong passwords](https://docs.python.org/3/library/secrets.html), made using Python 3.

## Getting Started
The most basic requirement is an installation of **Python 3.6** or newer. If you haven't got Python on your device, get it from [their official downloads page](https://www.python.org/downloads/). 

*Note that Python 3.6's end of support is on 23<sup>rd</sup> December 2021.*

### Get PyPassGen
Clone the repository by 
```
git clone https://github.com/elitejake/PyPassGen.git
```
*or* download the zipped repository [here](https://github.com/elitejake/PyPassGen/archive/main.zip) and extract it.

## Usage
### Using PyPassGen-cli.py
Usage:
```
PyPassGen-cli.py [arguments]
```
#### Password Configurations
| Argument | Description |
|--|--|
| `-l` | Disables upper-case characters in generated passwords |
| `-n` | Disables numbers (1, 2, 3, etc...) in generated passwords |
| `-s` | Disables symbols (!, @, $, etc...) in generated passwords |
| `-L <length>` | Length (integer) of generated passwords |
| `-C` | Uses `config.txt` to get parameters. It will override other parameters |
#### Output
| Argument | Description |
|--|--|
| `-N <number>` | Number of passwords to generate |
| `-o <file>` | Outputs the passwords to a file |
| `-c` | Copies the passwords to a clipboard (is broken) |
| `-p` | Disables output of passwords to the terminal |
| `-S` / `-strong`| Uses the secrets module to produce cryptographically strong password |
#### Examples

 - ```PyPassGen-cli.py -l -n -s``` <br>
 This will produce passwords which won't have upper-case characters (`-l`), numbers (`-n`) or symbols (`-s`).
 - ```PyPassGen-cli.py -p -N 500 -S -o passwords.txt``` <br>
This will produce 500 (`-N`) passwords using secrets module (to generate cryptographically random passwords) (`-s`) and outputs them on `passwords.txt` (`-o`). Passwords won't be printed on the terminal (`-p`).

## License
Distributed under the MIT License. See [`LICENSE.md`](https://github.com/elitejake/PyPassGen/blob/main/LICENSE.md) for more information.
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
> IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
> CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
> TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
> SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
