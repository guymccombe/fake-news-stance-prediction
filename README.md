# Detection of Fake News by Stance Prediction

Fourth year coursework at Durham University: Using natural language processing to detect fake news by predicting the stance associated to news articles.

Original dataset from [FakeNewsChallenge](https://github.com/FakeNewsChallenge/fnc-1) ([original task](FakeNewsChallenge.org))

The data provided is `(headline, body, stance)` instances, where `stance` is one of `{unrelated, discuss, agree, disagree}`. The dataset is provided as two CSVs:


### `train_bodies.csv`

This file contains the body text of articles (the `articleBody` column) with corresponding IDs (`Body ID`)

### `train_stances.csv`

This file contains the labeled stances (the `Stance` column) for pairs of article headlines (`Headline`) and article bodies (`Body ID`, referring to entries in `train_bodies.csv`).

### Distribution of the data

The distribution of `Stance` classes in `train_stances.csv` is as follows:

|   rows |   unrelated |   discuss |     agree |   disagree |
|-------:|------------:|----------:|----------:|-----------:|
|  49972 |    0.73131  |  0.17828  | 0.0736012 |  0.0168094 |


### Dataset credits:

- Edward Misback
- Craig Pfeifer
