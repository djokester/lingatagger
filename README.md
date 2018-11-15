# lingatagger: A Hindi Gender Tagger! 
## **_लिंग_** _(hindi, pron. linga): gender_

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

[![Codeship Status for djokester/lingatagger](https://app.codeship.com/projects/80bdb6c0-c769-0136-99fa-02b711961e9b/status?branch=master)](https://app.codeship.com/projects/314691)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/85e6e68340a44709ab5cbd6148eb90af)](https://www.codacy.com/app/djokester/lingatagger?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=djokester/lingatagger&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/85e6e68340a44709ab5cbd6148eb90af)](https://www.codacy.com/app/djokester/lingatagger?utm_source=github.com&utm_medium=referral&utm_content=djokester/lingatagger&utm_campaign=Badge_Coverage)

![GitHub open pull requests](https://img.shields.io/github/issues-pr/djokester/lingatagger.svg) 
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/djokester/lingatagger.svg)
![GitHub closed issues](https://img.shields.io/github/issues-closed/djokester/lingatagger.svg)
![GitHub open issues](https://img.shields.io/github/issues/djokester/lingatagger.svg)



## Display Corpus
Displaying a list of sentences, there are a total of 19522 sentences!
``` python
>>> import lingatagger.sentence as sents
>>> sentences = sents.drawlist()
>>> sentences[:3]
['विश्व भर में करोड़ों टीवी दर्शकों की उत्सुकता भरी निगाह के बीच मिस ऑस्ट्रेलिया जेनिफर हॉकिंस को मिस यूनिवर्स-२००४ का ताज पहनाया गया।', 'करीब दो घंटे चले कार्यक्रम में विभिन्न देशों की ८० सुंदरियों के बीच २० वर्षीय हॉकिंस को सर्वश्रेष्ठ आंका गया।', 'मिस अमेरिका शैंडी फिनेजी को प्रथम उप विजेता और मिस प्यूरेटो रिको अल्बा रेइज द्वितीय उप विजेता चुनी गई।']
```
Displaying a list of words with their respective genders. There are a total of 21460 such instances!
```python
>>> import lingatagger.genderlist as gndr
>>> genders = gndr.drawlist()
>>> genders = [string.split("\t") for string in genders]
>>> genders[:5]
[['विश्व', 'm'], ['भर', 'm', 'any'], ['में', 'any'], ['करोड़ों', 'm', 'any'], ['टीवी', 'm']]

```

## Tokenizer

Hindi tokenizer of three kinds simple, word, and sentence tokenizer!
```python
>>> import lingatagger.sentence as sents
>>> import lingatagger.tokenizer as tokenizer
>>> sentences = " ".join(sents.drawlist()[:5])

>>> tokenizer.tokenize(sentences)
['विश्व', 'भर', 'में', 'करोड़ों', 'टीवी', 'दर्शकों', 'की', 'उत्सुकता', 'भरी', 'निगाह', 'के', 'बीच', 'मिस', 'ऑस्ट्रेलिया', 'जेनिफर', 'हॉकिंस', 'को', 'मिस', 'यूनिवर्स', '-', '२००४', 'का', 'ताज', 'पहनाया', 'गया।', 'करीब', 'दो', 'घंटे', 'चले', 'कार्यक्रम', 'में', 'विभिन्न', 'देशों', 'की', '८०', 'सुंदरियों', 'के', 'बीच', '२०', 'वर्षीय', 'हॉकिंस', 'को', 'सर्वश्रेष्ठ', 'आंका', 'गया।', 'मिस', 'अमेरिका', 'शैंडी', 'फिनेजी', 'को', 'प्रथम', 'उप', 'विजेता', 'और', 'मिस', 'प्यूरेटो', 'रिको', 'अल्बा', 'रेइज', 'द्वितीय', 'उप', 'विजेता', 'चुनी', 'गई।', 'भारत', 'की', 'तनुश्री', 'दत्ता', 'अंतिम', '१०', 'प्रतिभागियों', 'में', 'ही', 'स्थान', 'बना', 'पाई।', 'हॉकिंस', 'ने', 'कहा', 'कि', 'जीत', 'के', 'बारे', 'में', 'उसने', 'सपने', 'में', 'भी', 'नहीं', 'सोचा', 'था।']

>>> tokenizer.wordtokenize(sentences)
['विश्व', 'भर', 'में', 'करोड़ों', 'टीवी', 'दर्शकों', 'की', 'उत्सुकता', 'भरी', 'निगाह', 'के', 'बीच', 'मिस', 'ऑस्ट्रेलिया', 'जेनिफर', 'हॉकिंस', 'को', 'मिस', 'यूनिवर्स-२००४', 'का', 'ताज', 'पहनाया', 'गया', 'करीब', 'दो', 'घंटे', 'चले', 'कार्यक्रम', 'में', 'विभिन्न', 'देशों', 'की', '८०', 'सुंदरियों', 'के', 'बीच', '२०', 'वर्षीय', 'हॉकिंस', 'को', 'सर्वश्रेष्ठ', 'आंका', 'गया', 'मिस', 'अमेरिका', 'शैंडी', 'फिनेजी', 'को', 'प्रथम', 'उप', 'विजेता', 'और', 'मिस', 'प्यूरेटो', 'रिको', 'अल्बा', 'रेइज', 'द्वितीय', 'उप', 'विजेता', 'चुनी', 'गई', 'भारत', 'की', 'तनुश्री', 'दत्ता', 'अंतिम', '१०', 'प्रतिभागियों', 'में', 'ही', 'स्थान', 'बना', 'पाई', 'हॉकिंस', 'ने', 'कहा', 'कि', 'जीत', 'के', 'बारे', 'में', 'उसने', 'सपने', 'में', 'भी', 'नहीं', 'सोचा', 'था']

>>> tokenizer.sentencetokenize(sentences)
['विश्व भर में करोड़ों टीवी दर्शकों की उत्सुकता भरी निगाह के बीच मिस ऑस्ट्रेलिया जेनिफर हॉकिंस को मिस यूनिवर्स-२००४ का ताज पहनाया गया। ', 'करीब दो घंटे चले कार्यक्रम में विभिन्न देशों की ८० सुंदरियों के बीच २० वर्षीय हॉकिंस को सर्वश्रेष्ठ आंका गया। ', 'मिस अमेरिका शैंडी फिनेजी को प्रथम उप विजेता और मिस प्यूरेटो रिको अल्बा रेइज द्वितीय उप विजेता चुनी गई। ', 'भारत की तनुश्री दत्ता अंतिम १० प्रतिभागियों में ही स्थान बना पाई। ', 'हॉकिंस ने कहा कि जीत के बारे में उसने सपने में भी नहीं सोचा था।']
```

## Gender Tagger
```python
>>> import lingatagger.sentence as sents
>>> import lingatagger.tagger as tagger
>>> sentence = " ".join(sents.drawlist()[:2])
>>> sentence
'विश्व भर में करोड़ों टीवी दर्शकों की उत्सुकता भरी निगाह के बीच मिस ऑस्ट्रेलिया जेनिफर हॉकिंस को मिस यूनिवर्स-२००४ का ताज पहनाया गया। करीब दो घंटे चले कार्यक्रम में विभिन्न देशों की ८० सुंदरियों के बीच २० वर्षीय हॉकिंस को सर्वश्रेष्ठ आंका गया।'

>>> gender = tagger.Tagger(sentence)
>>> gender
[('विश्व', 'm'), ('भर', 'any'), ('में', 'any'), ('करोड़ों', 'any'), ('टीवी', 'm'), ('दर्शकों', 'm'), ('की', 'any'), ('उत्सुकता', 'f'), ('भरी', 'f'), ('निगाह', 'f'), ('के', 'any'), ('बीच', 'any'), ('मिस', 'any'), ('ऑस्ट्रेलिया', 'm'), ('जेनिफर', 'f'), ('हॉकिंस', 'f'), ('को', 'any'), ('मिस', 'any'), ('यूनिवर्स', 'm'), ('-', 'any'), ('any', 'num'), ('का', 'any'), ('ताज', 'm'), ('पहनाया', 'm'), ('गया।', 'any'), ('करीब', 'any'), ('दो', 'any'), ('घंटे', 'm'), ('चले', 'any'), ('कार्यक्रम', 'm'), ('में', 'any'), ('विभिन्न', 'any'), ('देशों', 'm'), ('की', 'any'), ('any', 'num'), ('सुंदरियों', 'f'), ('के', 'any'), ('बीच', 'any'), ('any', 'num'), ('वर्षीय', 'any'), ('हॉकिंस', 'f'), ('को', 'any'), ('सर्वश्रेष्ठ', 'any'), ('आंका', 'any'), ('गया।', 'any')]

```
_______________________
