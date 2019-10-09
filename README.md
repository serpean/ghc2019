# Online Qualification Round of Google Hash Code 2019

This repo host our solution for the Online Qualification Round of Google Hash Code 2019. 

## Description

The problem statement can be found inside of the docs folder. As a summary, we had to do the following:

_Given a list of photos and the tags associated with each photo, arrange the photos into a slideshow that is as 
interesting as possible (the scoring section below explains what we mean by “interesting”)._

## Run

**Clone the repo**

```bash
git clone https://github.com/serpean/ghc2019.git
```

**Move to the project**

```bash
cd ghc2019
```

**Run it**

```bash
python3 main.py
```

**Show results**

Results are going to be shown after execution in this fashion (As they can be variable, this is just an example):

```
----------  SCORES ----------
d_pet_pictures.txt 181893
c_memorable_moments.txt 752
a_example.txt 2
b_lovely_landscapes.txt 6906
e_shiny_selfies.txt 118409

Total 307962
```

_Note_: You can add custom valid use cases to the folder _input/_ and they are also going to be processed.

## Our approach

As the time was limited and the sets were not that big, we decided to follow a greedy approach to obtain a valid 
solution before the time ran out. We used randomization for better sorting, so results my vary a lot between different
runs. However, and for some reason, punctuation was always inside of the 300000 - 320000 range.

## Our team

Out team was called Bieren lager and formed by four Computer Science students of the Universitat Politènica de València:

- Bogdan Baghiu, _bogdanbaghiu_ - https://github.com/bogdanbaghiu
- Bullcaos, _bullcaos_ - https://github.com/bullcaos
- Marc Solé, _msolefonte_ - https://github.com/msolefonte
- Sergio Pérez, _serpean_ - https://github.com/serpean

## Results

We scored 312351 points with this approach, resulting in the 140th team from Spain and the 2726 worldwide.

https://codingcompetitions.withgoogle.com/hashcode/archive/2019

## Acknowledgments

Thanks to all the members of [ACM UPV Chapter](https://acmupv.webs.upv.es/) for allowing us spending that day together.
