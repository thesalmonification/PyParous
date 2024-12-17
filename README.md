<!--
Hey, thanks for using the pyparous template.  
If you have any enhancements, then fork this project and create a pull request 
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->
<div align="center">

  <h1>PyParous</h1>
  
  <p>
    Easily perform arithmetic for gestational and fetal ages used in OBGYN. 
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/thesalmonification/pyparous/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/thesalmonification/pyparous" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/thesalmonification/pyparous" alt="last update" />
  </a>
  <a href="https://github.com/thesalmonification/pyparous/network/members">
    <img src="https://img.shields.io/github/forks/thesalmonification/pyparous" alt="forks" />
  </a>
  <a href="https://github.com/thesalmonification/pyparous/stargazers">
    <img src="https://img.shields.io/github/stars/thesalmonification/pyparous" alt="stars" />
  </a>
  <a href="https://github.com/thesalmonification/pyparous/issues/">
    <img src="https://img.shields.io/github/issues/thesalmonification/pyparous" alt="open issues" />
  </a>
  <a href="https://github.com/thesalmonification/pyparous/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/thesalmonification/pyparous.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/thesalmonification/pyparous/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/thesalmonification/pyparous">Documentation</a>
  <span> · </span>
    <a href="https://github.com/thesalmonification/pyparous/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/thesalmonification/pyparous/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents


- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

  



<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

There are no required prerequisites! It only uses built-in Python methods.

<!-- Installation -->
### :gear: Installation

Installation is recommended through the pip command.

```bash
  pip install pyparous
```
   

<!-- Usage -->
## :eyes: Usage

The PyParous project relies on the "age" object. The age object takes in a single float value representing the weeks and days the patient is currently pregnant. For example, a patient who is 39 weeks and 4 days age will be declared as follows:


```python
from pyparous import age

>>>myAge = age(39.4)
>>>print(myAge)
>>>age('39.4')
```

The age object only takes positive float values. Furthermore, the decimal portion my be a value of 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, or 0.6 to properly represent the number of days.

After declaring an object, you are able to perform arithmetic operations of addition and subtraction. 

```python
from pyparous import age

>>>A = age(39.4)
>>>B = age(1.1)
>>>print(A + B)
>>>age('40.5')
>>>print(A - B)
>>>age('38.3')
```

<!-- Roadmap -->
## :compass: Roadmap

* [x] Complete age definition and basic arithmetic
* [ ] Perform age calculations based on a certain day or due date.


<!-- Contributing -->
## :wave: Contributing

<a href="https://github.com/thesalmonification/pyparous/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=thesalmonification/pyparous" />
</a>


<!-- Code of Conduct -->
### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/thesalmonification/pyparous/blob/master/CODE_OF_CONDUCT.md)


<!-- License -->
## :warning: License

Distributed under the MIT License. See LICENSE.txt for more information.


<!-- Contact -->
## :handshake: Contact

Duncan Salmon - drsalmon@tamu.edu

Project Link: [https://github.com/thesalmonification/pyparous](https://github.com/thesalmonification/pyparous)


<!-- Acknowledgments -->
## :gem: Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

 - [Shields.io](https://shields.io/)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
 - [Readme Template](https://github.com/othneildrew/Best-README-Template)