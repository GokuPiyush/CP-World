# Overview
CP World produces a plot of programmers of any rank on a world map. It gives an idea of, level of awarensess of Competitive Programming in different parts of the world.

# Guide
This program can:
- Either fetch the fresh data and than do the plotting
```bash
build {space seperated initals}
```
- or, can plot existing data
```bash
plot {space seperated initals}
```
Type ```exit ``` to exit the program.

<br />

Refer the following dictionary to get hint of initals of a particular rank..
```python
initials = {
  'lg': 'legendary grandmaster', 
  'ig': 'international grandmaster', 
  'g': 'grandmaster', 
  'im': 'international master', 
  'm': 'master', 
  'cm': 'candidate master', 
  'e': 'expert', 
  's': 'specialist', 
  'p': 'pupil', 
  'n': 'newbie'
}
```

And the color of the marker would be same as color code in codeforces for any particular rank.
Refer the following dictionary to get hint of color codes..
```python
color = {
  'legendary grandmaster': 'r',
  'international grandmaster': 'r',
  'grandmaster': 'r',
  'international master': 'y',
  'master': 'y',
  'candidate master': 'm',
  'expert': 'b',
  'specialist': 'c',
  'pupil': 'g',
  'newbie': 'w'
}
```

<br />
<br />

# Examples
```cmd
plot lg ig g
```
![Figure_1](https://user-images.githubusercontent.com/44301840/94146691-ee4da380-fe91-11ea-85d7-a684d2845733.png)

```cmd
plot e
```
![Figure_1](https://user-images.githubusercontent.com/44301840/94144649-0ec82e80-fe8f-11ea-9b12-16eb87f59a1f.png)

```cmd
plot lg ig g im
```
![Figure_1](https://user-images.githubusercontent.com/44301840/94147473-f22df580-fe92-11ea-8d3f-02ca8291dfc4.png)


